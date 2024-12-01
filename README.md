# Student Management System

A lightweight FastAPI backend for managing student records with MongoDB as the database.

## Features

- Create new student records
- Retrieve student information (all students or by specific criteria)
- Update existing student records
- Delete student records
- Comprehensive error handling and logging

## Technology Stack

- **Backend Framework**: FastAPI
- **Database**: MongoDB
- **ORM/Validation**: Pydantic
- **Logging**: Python logging module
- **Environment Management**: python-dotenv

## Getting Started

### Prerequisites

- Python 3.8+
- MongoDB
- pip or pipenv

### Installation

1. Clone the repository
```bash
git clone https://github.com/NayanPahuja/StudentManagementSystem
cd StudentManagementSystem
```

2. Install dependencies
```bash
pip install -r requirements.txt
# or
pipenv install
```

3. Set up environment variables
Create a `.env` file in the project root with:
```
MONGODB_URI=mongodb://localhost:27017
```
If you are using an Atlas Cluster, it will look like this:

```

MONGODB_URI=mongodb+srv://<username>:<db_password>@<cluster_address>.mongodb.net/?retryWrites=true&w=majority
```
### Running the Application

```bash
uvicorn app:app --reload
```

## API Endpoints

- `POST /students`: Create a new student
- `GET /students`: Retrieve students (with optional filtering by country and age)
- `GET /students/{id}`: Retrieve a specific student
- `PATCH /students/{id}`: Update a student's information
- `DELETE /students/{id}`: Delete a student record

### Query Parameters

- `GET /students?country=<country_name>`: Filter students by country
- `GET /students?age=<minimum_age>`: Filter students by minimum age

## Configuration

### Environment Variables

- `MONGODB_URI`: Connection string for MongoDB
- `DATABASE_NAME`: Name of the MongoDB database (default: studentsDB)

## Logging

The application uses a configured logger to track operations:
- Creates log entries for database operations
- Supports info and error level logging

## Docker Support

Dockerfile configuration added to containerize the application.

## Health Checks

- `/healthCheck`: Verifies application is running
- `/`: Welcome endpoint

## Error Handling

Comprehensive error handling with:
- 200 for Successfull responses
- 204 for No Content Response
- 404 for not found resources
- 400 for bad requests
- Detailed error messages

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
