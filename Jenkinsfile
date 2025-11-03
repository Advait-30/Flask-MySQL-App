pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        DOCKER_IMAGE = 'aathreya04/flask-mysql-app'
        COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/aathreya-sharma/flask-mysql-app.git'
            }
        }

        stage('Build') {
            steps {
                echo '🔧 Building Docker images...'
                // Retry 3 times if Docker Hub times out
                retry(3) {
                    sh '''
                        echo "⏳ Running docker-compose build..."
                        docker-compose build --progress=plain || (echo "⚠️ Build failed, retrying in 5s..." && sleep 5 && false)
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running container tests...'
                sh '''
                    docker-compose up -d
                    echo "⏳ Waiting for containers to initialize..."
                    sleep 15
                    curl --fail http://localhost:5001/ || (docker-compose logs && exit 1)
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo '📦 Pushing image to Docker Hub...'
                    sh '''
                        echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                        docker build -t $DOCKER_IMAGE:latest .
                        docker push $DOCKER_IMAGE:latest
                        docker logout
                    '''
                }
            }
        }

        stage('Cleanup') {
            steps {
                echo '🧹 Cleaning up containers and volumes...'
                sh 'docker-compose down -v'
            }
        }
    }

    post {
        success {
            echo '✅ Build, Test, and Push Successful!'
        }
        failure {
            echo '❌ Build Failed — Check Logs!'
        }
    }
}