# GitHub Repository Intelligence API

A FastAPI-based backend that integrates with the GitHub REST API to retrieve and expose repository information through clean, structured API endpoints.

This project is being built as a learning project focused on **backend engineering, external API integration, API design, testing, and eventually AI-powered repository analysis**.

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
* Response transformation
* Unit testing with pytest
* Mocking external dependencies

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
├── tests/
│   └── test_service.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
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

Interactive API documentation:

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

## 🧪 Testing

The project uses **pytest** for unit testing.

Run the tests with:

```bash
python -m pytest
```

The service layer is tested independently from GitHub by using mocks.

### Current test coverage

The current tests verify:

* Successful repository retrieval
* Repository-not-found handling
* Translation of GitHub HTTP errors into application-specific exceptions

External GitHub API calls are **not made during these unit tests**.

Instead, `unittest.mock.Mock` is used to simulate the GitHub client.

```text
Test
  ↓
RepositoryService
  ↓
Mock GithubClient
  ↓
Fake response / simulated error
```

This keeps the tests fast, deterministic, and independent of the GitHub API.

## 🛡️ Error Handling

The application handles common GitHub API failures and converts them into application-level responses.

For example:

```text
Repository not found
        ↓
404 Not Found
```

The service layer translates low-level HTTP/request exceptions into application-specific exceptions such as:

* `RepositoryNotFoundError`
* `GithubAPIError`

## 🔐 Environment Variables

The application currently uses:

```env
GITHUB_TOKEN=your_github_token
```

Environment variables are loaded using `python-dotenv`.

Secrets are excluded from version control using `.gitignore`.

## 🧠 What I'm Learning

This project is designed to practice real-world backend and AI engineering concepts:

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
* pytest
* Unit testing
* Mocking external dependencies

## 🛣️ Roadmap

### Backend

* [x] FastAPI API
* [x] GitHub API integration
* [x] GitHub authentication
* [x] Service layer
* [x] Pydantic response models
* [x] Error handling
* [x] Unit testing
* [x] Mocking external dependencies
* [ ] PostgreSQL persistence
* [ ] Database repository layer
* [ ] Caching
* [ ] Docker
* [ ] Improve API documentation

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

## 🎯 Long-Term Goal

The goal of this project is to combine **backend engineering + external APIs + databases + LLMs** into a practical AI engineering project.

The planned progression is:

```text
FastAPI
   ↓
External APIs
   ↓
Testing
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

## 📚 Project Status

**Current status:** 🚧 In development

The current version has a working FastAPI backend, GitHub API integration, structured responses, error handling, and unit tests with mocked external dependencies.

The next development stage is **PostgreSQL persistence**.
