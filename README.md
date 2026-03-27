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

## ⚙️ CI/CD Pipeline & Enterprise Architecture Mapping

This project utilizes automated GitHub Actions workflows to enforce code quality and automate deployments. To demonstrate scalable DevOps knowledge, the architecture was designed with enterprise equivalents in mind:

| Capability | Portfolio Implementation | Enterprise Equivalent | Purpose |
| :--- | :--- | :--- | :--- |
| **Continuous Integration** | GitHub Actions | Jenkins, GitLab CI | Automates testing and linting on every push. |
| **Code Quality & Linting** | Flake8 & Pytest | SonarQube | Blocks merges if code is poorly formatted or fails unit tests. |
| **Secrets Management** | GitHub Secrets | **HashiCorp Vault**, AWS Secrets Manager | Prevents hardcoding passwords or API keys in the source code. |
| **Artifact Management** | GitHub Packages | **JFrog Artifactory**, Sonatype Nexus | Stores versioned software builds securely before deployment. |
| **Hosting & Orchestration** | Azure App Service | **OpenShift**, Kubernetes (AKS/EKS) | Scalable hosting environments for decoupled application tiers. |
| **Configuration Mgmt** | Azure Web App Action | **Ansible**, Chef, Puppet | Standardizes server/VM configuration (Note: Abstracted here via Azure PaaS). |
| **Observability & Logs** | Azure App Insights | **Datadog, New Relic**, Splunk | Monitors application health, tracks errors, and logs production traffic. |

### Branching Strategy
- **Feature Branches:** Pushing to `feature-**` triggers the CI pipeline (Linting & Testing).
- **Pull Requests:** Opening a PR to `main` requires passing CI checks before merging is allowed.
- **Main Branch:** Merging to `main` triggers the CD pipeline to automatically deploy to Azure.