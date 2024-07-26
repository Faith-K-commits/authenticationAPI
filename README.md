# User and Organisation management API Project

# Table of contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)

# Introduction
This project is a django based API with user authentication and organisation management features.

# Features
- User registration and login with JWT Authentication
- Fetching user records and organisations
- Creating and managing organisations
- Adding users to organisations

# Technologies used
- Django
- Django REST Framework
- JWT (JSON Web Token) for authentication

# Setup Instructions
## Prerequisites
- Python 3.x
- Django REST Framework
- Django Simple JWT

## Installation
1. Clone the repository
2. Create and activate a virtual environment
3. Install the dependencies
4. Apply the migrations
5. Run the development server

# API Endpoints
## User Endpoints
### Register user 
  - Method: POST 
  - Endpoint: `/auth/register`
  - Description: Registers a new user.
  - Example request: POST http://127.0.0.1:8000/auth/register
  ```json
        {
          "firstName": "Jane",
          "lastName": "Doe",
          "email": "jane.doe@test.com",
          "password": "password123",
          "phone": "0700000000"
        }
```
    
  - Example response:
  ```json
  {
    "status": "success",
    "message": "Registration successful",
    "data": {
        "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyMjU1NjQ0LCJpYXQiOjE3MjE5OTY0NDQsImp0aSI6ImZhY2U0OTI4YTljZTQwODc5NzM1YmQ0NjU0YjcxODE0IiwidXNlcl9pZCI6MTF9.L37asmGd3Esz0Ive6rX_AXoaH5FzG96Tc_ckH9I9VuY",
        "user": {
            "userId": "29b7bc0c-56f0-493b-bd14-72d5ac5f7e43",
            "firstName": "Jane",
            "lastName": "Doe",
            "email": "jane.doe@test.com",
            "phone": "0700000000"
        }
    }
  }
```
### Login user
  - Method: POST
  - Endpoint: `auth/login`
  - Description: Log in a user
  - Example request: POST http://localhost:8000/auth/login
  ```json
    {
      "email": "jane.doe@test.com",
      "password": "password123"
    }
  ```
  - Example response:
  ```json
    {
      "status": "success",
      "message": "Login successful",
      "data": {
          "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyMjU1NjQ0LCJpYXQiOjE3MjE5OTY0NDQsImp0aSI6ImZhY2U0OTI4YTljZTQwODc5NzM1YmQ0NjU0YjcxODE0IiwidXNlcl9pZCI6MTF9.L37asmGd3Esz0Ive6rX_AXoaH5FzG96Tc_ckH9I9VuY",
          "user": {
              "userId": "29b7bc0c-56f0-493b-bd14-72d5ac5f7e43",
              "firstName": "Jane",
              "lastName": "Doe",
              "email": "jane.doe@test.com",
              "phone": "0700000000"
          }
      }
    }
  ```

### Get user record
  - Method: POST
  - Endpoint: `api/users/<uuid:user_id>`
  - Description: Retrieve a user's record
  - Example request: `http://127.0.0.1:8000/api/users/29b7bc0c-56f0-493b-bd14-72d5ac5f7e43`
  - Example response:
```json
{
    "status": "success",
    "message": "User record retrieved successfully.",
    "data": {
        "userId": "29b7bc0c-56f0-493b-bd14-72d5ac5f7e43",
        "firstName": "Jane",
        "lastName": "Doe",
        "email": "jane.doe@test.com",
        "phone": "0700000000"
    }
}
```

### Get user organisation
- Method: GET
- Endpoint: `api/organisations`
- Description: Retrieve user organisations
- Example request: http://127.0.0.1:8000/api/organisations
- Example response:
```json
{
    "status": "success",
    "message": "Organisations retrieved successfully",
    "data": {
        "organisations": [
            {
                "orgId": "d04ddeaa-65d6-4e6b-9528-8b89f2283271",
                "name": "Jane's Organisation",
                "description": "Default Organization"
            },
            {
                "orgId": "38847369-651f-4d9a-929a-47510e31cc74",
                "name": "My organisation",
                "description": "Jane's created organization"
            }
        ]
    }
}
```

## Organisation Endpoints
### Get organisation record
- Method: GET
- Endpoint: `api/organisations/<uuid:org_id>`
- Description: Retrieve organisation record
- Example Request: http://127.0.0.1:8000/api/organisations/d04ddeaa-65d6-4e6b-9528-8b89f2283271
- Example Response:
```json
{
    "status": "success",
    "message": "Organisation details retrieved successfully",
    "data": {
        "orgId": "d04ddeaa-65d6-4e6b-9528-8b89f2283271",
        "name": "Jane's Organisation",
        "description": "Default Organization"
    }
}
```
### Create organisation
- Method: POST
- Endpoint: `api/organisations/create`
- Description: Create custom organisation
- Example request: http://127.0.0.1:8000/api/organisations/create
- Example Response:
```json
{
    "status": "success",
    "message": "Organisation created successfully",
    "data": {
        "orgId": "0a2f5254-0991-4865-bb84-942331f7d6f0",
        "name": "Third organisation",
        "description": "My third organisation"
    }
}
```
### Add user to organisation
- Method: POST
- Endpoint: `api/organisations/<uuid:org_id>/users`
- Description: Add user to an organisation
- Example request: http://127.0.0.1:8000/api/organisations/0a2f5254-0991-4865-bb84-942331f7d6f0/users
- Example response:
```json
{
    "status": "success",
    "message": "user added to organisation successfully"
}
```

