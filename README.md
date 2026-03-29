# Notes Service Mongo

## Overview
This is a Python-based service for managing notes using MongoDB as the database.

## Features
- CRUD operations for notes.
- User authentication and authorization.
- API documentation with Swagger UI.

## Project Structure
```
notes_service_mongo/
├── src/
│   ├── app.py
│   ├── models/
│   │   └── note.py
│   ├── routes/
│   │   └── notes.py
│   └── utils/
│       └── auth.py
├── tests/
│   ├── test_app.py
│   └── test_notes.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Environment
- Python 3.8+
- MongoDB 4.0+

## Local Run
1. Activate the virtual environment:
   ```bash
   source D:\wrk\git\agentic\agenticvenv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the application:
   ```bash
   python src/app.py
   ```

## Tests
Run tests using pytest:
```bash
python -m pytest -q
```

## Docker Usage
Build the Docker image:
```bash
docker build -t notes_service_mongo .
```

Run the Docker container:
```bash
 docker run -p 5000:5000 notes_service_mongo
```

## Compose Usage
Start the application using Docker Compose:
```bash
 docker-compose up --build
```

## API Endpoints
- **GET /notes**: Retrieve all notes.
- **POST /notes**: Create a new note.
- **GET /notes/{id}**: Retrieve a specific note by ID.
- **PUT /notes/{id}**: Update a specific note by ID.
- **DELETE /notes/{id}**: Delete a specific note by ID.

## Troubleshooting Notes
- Ensure MongoDB is running and accessible.
- Check environment variables for correct configuration.
- Review logs for any errors or warnings.