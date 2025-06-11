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
