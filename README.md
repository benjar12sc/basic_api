# FastAPI Project

WIP, just a simple project getting back to the basics of development. This meant to show
development in progress.

## Project Structure

- **client/**: (Optional) Frontend or client-side code.
- **data/**: Contains the SQLite database and CSV data files.
- **server/**: Backend FastAPI application and supporting modules.
  - **requirements.txt**: Python dependencies.
  - **src/**: Main source code for the FastAPI app.
    - **config.py**: Configuration and database setup.
    - **main.py**: FastAPI application entry point.
    - **populate_database.py**: Script to populate the database from CSV.
    - **dal/**: Data Access Layer modules.
    - **model/**: SQLAlchemy models and related code.
    - **router/**: FastAPI routers for API endpoints.
    - **service/**: (Optional) Business logic/services.

## TODOs

- Convert to CBR (Class Based Routers) to make authorization and dependency injection easier.
- Finish test DB initialization and destruction, and ensure it is always separate from the application DB.
- Move Pydantic schemas out of routers and into a dedicated schemas module.
- Add more comprehensive unit and integration tests, including for user authentication and session management.
- Refactor DALs and routers for better separation of concerns and reusability.
- Add proper error handling and logging throughout the backend.
- Move configuration (API version, DB URL, etc.) to environment variables and .env files where not already done.
- Implement user authentication and session token logic in the user router.
- Add frontend validation and error handling for all forms.
- Add pagination, filtering, and sorting to all list endpoints.
- Improve Docker and deployment setup for production readiness.
