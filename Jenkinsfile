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
                sh 'docker-compose build'
            }
        }

        stage('Test') {
            steps {
                sh 'docker-compose up -d'
                sh 'sleep 15'
                sh 'curl --fail http://localhost:5001/ || (docker-compose logs && exit 1)'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    sh 'docker build -t $DOCKER_IMAGE:latest .'
                    sh 'docker push $DOCKER_IMAGE:latest'
                }
            }
        }

        stage('Cleanup') {
            steps {
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