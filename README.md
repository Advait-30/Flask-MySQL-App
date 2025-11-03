

# Flask + MySQL Docker Example

This is a simple example Flask application using MySQL as the database, containerized with Docker Compose.

## Features
- REST API with Flask (Python)
- MySQL 8 database
- Dockerized (multi-container)

## Requirements
- Docker
- Docker Compose

## Usage
1. Clone this repo:
    ```
    git clone <repo-url>
    cd flask-mysql-app
    ```
2. Start the services:
    ```
    docker-compose up --build
    ```
3. The Flask app will be running at [http://localhost:5001](http://localhost:5001)

## API Endpoints
- `GET /users` — List all users
- `POST /users` — Add a user (expects JSON: `{"name": "Your Name"}`)

Example:
```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"name":"Alice"}' \
     http://localhost:5001/users
```

## Configuration
The database credentials are set in `docker-compose.yml` and passed via environment variables:
- DB Name: `flaskdb`
- User: `flaskuser`
- Password: `flaskpass`

## Development
You can edit the Flask app in the `app/` directory and changes will be reflected immediately.

## License
MIT