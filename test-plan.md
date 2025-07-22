# Todo App Automation Tests

This repository contains automated tests for a simple Todo application with a React frontend and Node.js backend. The tests cover both UI and API functionality to validate key user flows and backend endpoints.

---

## Project Structure

- `frontend/` — React app (runs on http://localhost:3000)
- `backend/` — Node.js API server (runs on http://localhost:5000)
- `ui-tests/` — Selenium WebDriver tests using Python + Pytest
- `postman/` — Postman collection JSON for API tests

---

## Prerequisites

- Node.js and npm installed
- Python 3.7+ and pip installed
- Chrome browser installed
- ChromeDriver will be managed automatically by WebDriverManager
- Newman (for Postman CLI) — optional

---

## Setup and Run Application

### Backend

cd backend
npm install
npm start

### Frontend

cd frontend
npm install
npm start

## Running UI Tests
Create and activate a Python virtual environment (optional but recommended):

python3 -m venv .venv
source .venv/bin/activate   (Linux/macOS)
.venv\Scripts\activate      (Windows)

Install test dependencies:

pip install -r requirements.txt

Run tests with pytest:

pytest test_todo_crud.py

## Running API Tests
Using Postman
Import the collection JSON from postman/todo-api-tests.postman_collection.json.

Run the requests and tests inside Postman.



## Notes
UI tests cover login, adding, editing, and deleting todos.

API tests cover authentication and CRUD operations on todos with positive and negative scenarios.

Make sure both backend and frontend servers are running before starting tests.

ChromeDriver is automatically handled by the Selenium WebDriver manager.

Visual regression or code coverage reporting is not included but can be added.

