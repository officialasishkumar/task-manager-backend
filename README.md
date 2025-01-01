# Task Manager API

## Overview
The **Task Manager API** is a RESTful application designed to manage tasks for authenticated users. It provides user authentication, task CRUD operations, and a summary of completed and pending tasks. The API is implemented using **FastAPI** and integrates with a **SQLAlchemy** database for persistence.

---

## Features
1. **User Management**:  
   - User sign-up with unique usernames and email addresses.
   - Authentication using JWT tokens.

2. **Task Management**:
   - Create, read, update, and delete tasks.
   - Retrieve all tasks or specific tasks owned by a user.
   - Generate a summary of completed and pending tasks.

3. **Security Features**:
   - Password hashing using **Passlib** with the Argon2 algorithm.
   - Authentication and authorization using **OAuth2** with bearer tokens.
   - Secure storage of sensitive keys using environment variables.

4. **Database**:
   - Relational database using SQLAlchemy ORM.
   - Supports SQLite and other databases configurable via environment variables.

---

## Security Implementation

### Password Security
- **Password Hashing**: Passwords are hashed using the Argon2 hashing algorithm before being stored in the database. This ensures passwords are not stored in plaintext.
- **Password Verification**: The hashed password is compared to the user-provided password during authentication.

### Token-Based Authentication
- **JWT Tokens**: Access tokens are generated using the **HS256 algorithm** with a secret key stored in environment variables.
- **Token Expiry**: Tokens are set to expire after 30 minutes by default to reduce risks of token misuse.
- **Validation**: Every request requiring authentication verifies the token using its signature and expiration timestamp.

### Environment Variables
- Sensitive data such as the **SECRET_KEY** and **SQLALCHEMY_DATABASE_URL** are stored in environment variables, ensuring they're not hardcoded in the codebase.

### Cross-Origin Resource Sharing (CORS)
- Configured to allow requests from specified frontend origins for secure communication.

---

## API Endpoints

### Authentication
| Endpoint         | Method | Description                             |
|------------------|--------|-----------------------------------------|
| `/auth/signup`   | POST   | Register a new user                    |
| `/auth/login`    | POST   | Authenticate a user and generate a token |
| `/auth/me`       | GET    | Retrieve details of the authenticated user |

### Tasks
| Endpoint           | Method   | Description                        |
|--------------------|----------|------------------------------------|
| `/tasks/`          | GET      | Retrieve all tasks of the user    |
| `/tasks/{task_id}` | GET      | Retrieve a specific task by ID    |
| `/tasks/`          | POST     | Create a new task                 |
| `/tasks/{task_id}` | PUT      | Update an existing task           |
| `/tasks/{task_id}` | DELETE   | Delete a task                     |
| `/tasks/summary`   | GET      | Get a summary of completed and pending tasks |

---

## Running Locally

### Prerequisites
- **Python 3.9 or higher** installed.
- **Poetry** for dependency management (optional, you can also use pip).
- **SQLite** (default database) or a supported database.

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/task-manager-api.git
   cd task-manager-api
   ```

2. **Set Up Environment Variables**
   Create a `.env` file in the `app` directory with the following:
   ```
   SQLALCHEMY_DATABASE_URL=sqlite:///./test.db
   SECRET_KEY=your_secret_key
   FRONTEND_URL=http://localhost:3001
   ```

3. **Install Dependencies**
   Using Poetry:
   ```bash
   poetry install
   poetry shell
   ```
   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database**
   ```bash
   python -m app.main
   ```

5. **Run the Application**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the API**
   - Open your browser or API testing tool (e.g., Postman).
   - Visit the Swagger documentation at:  
     [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Frontend Integration
- Update the `FRONTEND_URL` in the `.env` file to the URL of your frontend application.
- Ensure CORS is properly configured to allow requests from the frontend.

---

## Security Best Practices
- **Environment Secrets**: Always use a strong secret key and never expose it in your codebase.
- **Database**: Use a secure database connection (e.g., PostgreSQL or MySQL with TLS).
- **Token Expiry**: Keep the token expiry time short and refresh tokens as needed.
- **HTTPS**: Deploy the application behind an HTTPS server to encrypt communication.

---

## Future Enhancements
- Add **Refresh Tokens** for better token lifecycle management.
- Implement **role-based access control** for multi-user systems.
- Add rate-limiting to prevent brute force attacks.

---

Start managing your tasks efficiently and securely with the Task Manager API! 🚀