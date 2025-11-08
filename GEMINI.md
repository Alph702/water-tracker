# 💧 Water Tracker - Gemini Development Guide

This document provides a comprehensive overview of the Water Tracker application, its architecture, and instructions for development and execution. It is intended to be used as a primary context source for Gemini AI to assist in development tasks.

## 1. Project Overview

The Water Tracker is a simple web application designed to help users monitor their daily water intake. It features a visually interactive interface where a bottle fills up as the user logs their consumption.

- **Purpose:** Track daily water consumption, set goals, and receive reminders.
- **Frontend:** The user interface is built with standard HTML, CSS, and vanilla JavaScript. It features an SVG animation of a bottle filling with water to represent the user's progress towards their daily goal.
- **Backend:** The backend is a Python application built with the **Flask** framework. It provides a RESTful API for the frontend to store and retrieve water intake data.
- **Database:** A **SQLite** database (`data/user_data.db`) is used for data persistence. It stores the water intake history with date and amount.
- **Architecture:** The application follows a simple client-server model. The Flask backend serves the HTML, CSS, and JS files and exposes API endpoints. The frontend communicates with these endpoints to manage data.

## 2. Building and Running the Application

The project uses `uv` for dependency management and task execution.

### 2.1. Installing Dependencies

To install the necessary Python packages, run the following command in the project root:

```bash
uv sync
```

This command will create a virtual environment (`.venv`) and install the dependencies specified in `pyproject.toml`.

### 2.2. Running the Application

To run the Flask development server, use the following command:

```bash
uv run flask run
```

The application will be accessible at `http://127.0.0.1:5000`.

**Note:** The project includes `gunicorn` in its dependencies, but it is not compatible with Windows. For development, always use the Flask development server.

### 2.3. Testing

No explicit test commands or testing frameworks were found in `pyproject.toml`. If there are tests for this project, please add instructions on how to run them here.

## 3. Development Conventions

### 3.1. Project Structure

The project is organized as follows:

```
water_tracker/
│
├── app.py                # Main Flask application file
├── data/
│   └── user_data.db      # SQLite database file
├── static/
│   ├── style.css         # CSS for styling
│   └── script.js         # JavaScript for frontend logic
│   └── assets/
│       ├── bottle.svg
│       ├── Human-figure.svg
│       ├── Human-mask.svg
│       ├── Human.svg
│       └── wave.svg
├── templates/
│   └── index.html        # Main HTML file
├── pyproject.toml        # Project metadata and dependencies
└── GEMINI.md             # This file
```

### 3.2. Backend (Flask)

- The main application logic is in `app.py`.
- The database is initialized in `init_db()`. The database schema consists of a single table `water_intake` with the following columns:
  - `id`: INTEGER PRIMARY KEY AUTOINCREMENT
  - `date`: TEXT NOT NULL
  - `amount`: INTEGER NOT NULL
- A single API endpoint `/api/data` handles GET, POST, and DELETE requests for water intake data:
  - **GET `/api/data?date=<date>`**: Retrieves the total water intake for the specified date.
  - **POST `/api/data`**: Adds a new water intake record for a specified date with a given amount.
  - **DELETE `/api/data`**: Deletes all water intake records for a specified date.

### 3.3. Frontend (HTML/CSS/JS)

- The main page is `templates/index.html`.
- All frontend logic is contained in `static/script.js`.
- The UI consists of:
  - A daily goal input field.
  - A bottle animation that visually represents the water intake.
  - Buttons to add 200ml or 500ml of water.
  - A display for the total water intake.
  - A reset button to clear the daily intake.
  - A button to enable desktop reminders.
- The frontend communicates with the backend via `fetch` requests to the `/api/data` endpoint to:
  - Fetch the total intake for the day on page load.
  - Send new intake data to the server.
  - Reset the intake for the day.
- A water bottle SVG in `index.html` is animated using CSS transforms controlled by JavaScript to show the water level.
- Browser notifications are used for reminders.

## 4. How it Works

1.  **Initialization**: When the user opens the application, the frontend fetches the total water intake for the current day from the backend.
2.  **User Interaction**:
    *   The user can set a daily goal for water intake.
    *   The user can add water intake by clicking the "+200ml" or "+500ml" buttons. Each click sends a POST request to the backend to save the new intake amount.
    *   The frontend updates the total intake display and the water level in the bottle animation.
    *   The user can reset their daily intake by clicking the "Reset" button, which sends a DELETE request to the backend.
    *   The user can enable hourly reminders to drink water by clicking the "Enable Reminders" button.
3.  **Data Persistence**: The backend stores all water intake data in a SQLite database, so the user's progress is saved even if they close the application.

### 3.4. Code Style

The Python code generally follows PEP 8 standards. The JavaScript code is written in a modern style with `const` and `let`.
