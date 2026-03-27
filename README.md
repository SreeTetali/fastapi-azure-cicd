# 3-Tier Enterprise CI/CD Portfolio Architecture

This repository demonstrates a modern, decoupled 3-tier web application with automated CI/CD pipelines. It is designed to showcase enterprise DevOps practices, including automated testing, infrastructure separation, and continuous deployment.

## 🏗️ Architecture Overview

The application is split into three distinct layers, allowing for independent scaling and deployment:

1. **Tier 1: Presentation Layer (Frontend)**
   - **Tech:** Pure HTML, CSS, and Vanilla JavaScript.
   - **Target CD:** Azure Static Web Apps.
   - **Function:** A decoupled UI that fetches data asynchronously via REST APIs.

2. **Tier 2: Application Layer (Backend API)**
   - **Tech:** Python, FastAPI, Uvicorn.
   - **Target CD:** Azure App Service (PaaS).
   - **Function:** Handles business logic, CORS routing, and secure database connections.

3. **Tier 3: Data Layer (Database)**
   - **Tech:** SQLite (Local Dev) -> Azure Database for PostgreSQL (Production).
   - **Function:** Persistent data storage utilizing SQLAlchemy ORM.

## 🚀 How to Run Locally

If you want to pull this project down and run it on your local machine, follow these steps:

### 1. Start the Backend (API)
Open a terminal and navigate to the backend directory:

    cd backend
    python -m venv venv
    # Windows: venv\Scripts\activate | Mac/Linux: source venv/bin/activate
    pip install -r requirements.txt
    uvicorn main:app --reload

The API will now be running at http://127.0.0.1:8000.

### 2. Start the Frontend (UI)
1. Open the project in VS Code.
2. Install the "Live Server" extension (by Ritwick Dey).
3. Right-click `frontend/index.html` and select "Open with Live Server".
4. The web page will automatically open and fetch data from the local FastAPI backend.