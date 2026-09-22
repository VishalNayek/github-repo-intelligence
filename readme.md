# GitHub Repository Intelligence API

A FastAPI-based backend that integrates with the GitHub REST API to retrieve and expose repository information through clean, structured API endpoints.

This project is being built as a learning project focused on **backend engineering, external API integration, API design, and eventually AI-powered repository analysis**.

## 🚀 Current Features

* FastAPI REST API
* GitHub REST API integration
* GitHub API authentication using a personal access token
* Environment variable management with `.env`
* Service-layer architecture
* Pydantic response models
* Repository information endpoint
* Repository statistics endpoint
* HTTP error handling
* Request timeout handling
* Clean separation between API, service, and external API client

## 🏗️ Architecture

```text
                    Client
                      │
                      ▼
                  FastAPI
                      │
                      ▼
              RepositoryService
                      │
                      ▼
                GithubClient
                      │
                      ▼
                 GitHub API
```

### Components

**FastAPI**

Handles HTTP requests and exposes the application's REST endpoints.

**RepositoryService**

Contains application-level logic and translates GitHub API errors into application-specific exceptions.

**GithubClient**

Responsible for communicating with the GitHub REST API, including authentication, HTTP requests, timeouts, and response handling.

**Pydantic Schemas**

Define the structure of the data returned by the API.

## 📁 Project Structure

```text
github-repo-intelligence/
│
├── main.py
├── github_client.py
├── service.py
├── schemas.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

> `.env` and `.venv` should not be committed to GitHub.

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/github-repo-intelligence.git
cd github-repo-intelligence
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure GitHub authentication

Create a `.env` file in the project root:

```env
GITHUB_TOKEN=your_github_token
```

The token is used to authenticate requests made by the application to the GitHub API.

**Never commit your `.env` file.**

### 5. Run the application

```bash
uvicorn main:api --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available through FastAPI's Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## 🔌 API Endpoints

### Get Repository Information

```http
GET /repositories/{owner}/{repo}
```

Example:

```http
GET /repositories/VishalNayek/task-manager
```

Returns structured repository information such as:

* Repository name
* Full repository name
* Description
* Primary language
* Topics
* Stars
* Forks
* Open issues
* Default branch

### Get Repository Statistics

```http
GET /repositories/{owner}/{repo}/stats
```

Example:

```http
GET /repositories/VishalNayek/task-manager/stats
```

Example response:

```json
{
    "name": "task-manager",
    "stars": 2,
    "forks": 0,
    "open_issues": 0,
    "language": "Python"
}
```

## 🛡️ Error Handling

The application handles common GitHub API failures and converts them into appropriate API responses.

For example:

```text
Repository not found
        ↓
404 Not Found
```

GitHub/API failures are translated into application-level errors rather than exposing low-level implementation details directly to the API consumer.

## 🔐 Environment Variables

The application currently uses:

```env
GITHUB_TOKEN=your_github_token
```

Environment variables are loaded using `python-dotenv`.

Secrets are excluded from version control using `.gitignore`.

## 🧠 What I'm Learning

This project is designed to practice real-world backend concepts:

* Python application architecture
* FastAPI
* REST API design
* External API integration
* Authentication
* Environment variables
* HTTP status codes
* Exception handling
* Pydantic
* Service-layer architecture
* API response transformation
* Testing external dependencies
* PostgreSQL persistence

## 🛣️ Roadmap

The project will evolve beyond simply retrieving GitHub data.

### Backend improvements

* [ ] Add automated tests
* [ ] Mock GitHub API calls
* [ ] Improve API error handling
* [ ] Add caching
* [ ] Add PostgreSQL persistence
* [ ] Improve API documentation
* [ ] Dockerize the application

### Repository Intelligence

The next major goal is to turn repository data into meaningful insights.

```text
GitHub Repository
        │
        ▼
Repository Data
        │
        ▼
Analysis Layer
        │
        ▼
AI / LLM
        │
        ├── Repository Summary
        ├── Architecture Explanation
        ├── Codebase Insights
        └── Improvement Suggestions
```

Eventually, the project will evolve into an **AI-powered GitHub Repository Intelligence API** capable of analyzing repositories rather than simply retrieving their metadata.

## 🎯 Project Goal

The long-term goal of this project is to combine **backend engineering + external APIs + databases + LLMs** into a practical AI engineering project.

The project will progressively introduce concepts such as:

```text
FastAPI
   ↓
External APIs
   ↓
PostgreSQL
   ↓
LLM APIs
   ↓
Embeddings
   ↓
RAG
   ↓
AI-powered Repository Intelligence
```

## 📚 Status

**Current status:** 🚧 In development

The current version focuses on the backend foundation and GitHub API integration. AI-powered repository analysis will be added in later stages.
