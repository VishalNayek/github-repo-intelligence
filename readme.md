# GitHub Repository Intelligence API

A FastAPI-based backend that integrates with the GitHub REST API to retrieve repository information, expose structured API responses, and persist repository data in PostgreSQL.

This project was built to practice real-world **backend engineering concepts** including external API integration, authentication, service-layer architecture, testing, SQLAlchemy, and PostgreSQL.

## 🚀 Features

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
* API response transformation
* Unit testing with pytest
* Mocking external API dependencies
* PostgreSQL persistence
* SQLAlchemy ORM
* Repository pattern for database access
* Prevents duplicate repository records
* Updates existing repository data when fetched again

## 🏗️ Architecture

```text
                         Client
                           │
                           ▼
                        FastAPI
                           │
                           ▼
                  RepositoryService
                    │            │
                    │            │
                    ▼            ▼
              GithubClient   RepoRepository
                    │            │
                    ▼            ▼
                GitHub API   SQLAlchemy
                                 │
                                 ▼
                            PostgreSQL
```

### Components

#### FastAPI

Handles HTTP requests and exposes the application's REST API.

#### RepositoryService

Contains application-level logic and coordinates between the GitHub API client and database repository.

#### GithubClient

Responsible for communicating with the GitHub REST API.

Responsibilities include:

* Authentication
* HTTP requests
* Request timeouts
* HTTP error handling
* Parsing GitHub responses

#### RepoRepository

Handles PostgreSQL persistence using SQLAlchemy.

Responsibilities include:

* Finding repositories
* Creating repository records
* Updating existing repository records

#### Pydantic Schemas

Define the structure of API responses and provide response validation.

## 📁 Project Structure

```text
github-repo-intelligence/
│
├── main.py
├── github_client.py
├── service.py
├── repository.py
├── models.py
├── database.py
├── schemas.py
│
├── tests/
│   └── test_service.py
│
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

### 4. Configure PostgreSQL

Create a PostgreSQL database:

```sql
CREATE DATABASE github_intelligence;
```

The application expects PostgreSQL to be available on:

```text
localhost:5432
```

### 5. Configure GitHub authentication

Create a `.env` file in the project root:

```env
GITHUB_TOKEN=your_github_token
```

The token is used to authenticate requests made by the application to GitHub.

**Never commit your `.env` file.**

### 6. Run the application

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

Returns structured repository information including:

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

## 🗄️ PostgreSQL Persistence

Repository information retrieved from GitHub is persisted in PostgreSQL.

The application uses:

```text
SQLAlchemy ORM
       ↓
PostgreSQL
       ↓
github_intelligence
       ↓
repositories
```

The repository model stores:

* Owner
* Repository name
* Full name
* Description
* Language
* Topics
* Stars
* Forks
* Open issues
* Default branch

### Insert / Update Behavior

When a repository is requested:

```text
GitHub API
     ↓
RepositoryService
     ↓
Check PostgreSQL
     │
     ├── Repository exists
     │       ↓
     │     UPDATE
     │
     └── Repository doesn't exist
             ↓
           INSERT
```

This prevents duplicate records for the same repository.

## 🧪 Testing

The project uses **pytest** for unit testing.

Run the tests with:

```bash
python -m pytest
```

The service layer is tested independently from GitHub by using mocks.

### Current tests

The tests cover:

* Successful repository retrieval
* Repository-not-found handling
* Translation of GitHub HTTP errors into application-specific exceptions

External GitHub API calls are not required for these service tests.

Instead, `unittest.mock.Mock` is used to simulate the GitHub client:

```text
Test
  ↓
RepositoryService
  ↓
Mock GithubClient
  ↓
Fake response / simulated error
```

This makes the tests fast and independent of the GitHub API.

## 🛡️ Error Handling

The application translates low-level GitHub request errors into application-specific exceptions.

For example:

```text
GitHub 404
   ↓
RepositoryNotFoundError
   ↓
FastAPI
   ↓
HTTP 404
```

The project currently uses:

* `RepositoryNotFoundError`
* `GithubAPIError`

## 🔐 Environment Variables

The application currently uses:

```env
GITHUB_TOKEN=your_github_token
```

Environment variables are loaded using `python-dotenv`.

Secrets are excluded from version control using `.gitignore`.

## 🧠 Concepts Practiced

This project was built to practice:

### Backend

* Python
* Object-oriented programming
* FastAPI
* REST API design
* Pydantic
* Service-layer architecture
* Repository pattern
* Dependency injection

### External APIs

* HTTP requests
* GitHub REST API
* API authentication
* Bearer tokens
* HTTP status codes
* Request timeouts
* Exception handling

### Databases

* PostgreSQL
* SQLAlchemy
* SQLAlchemy ORM
* Database sessions
* Models
* CRUD operations
* Querying with `select()`
* Insert/update persistence

### Testing

* pytest
* Unit testing
* Mocking
* `unittest.mock`
* Testing exceptions
* Testing external dependencies without making real API calls

## 🛣️ Project Status

**Status: ✅ Complete**

The project currently provides a working backend that:

```text
Client
  ↓
FastAPI
  ↓
RepositoryService
  ↓
GitHub API
  ↓
Repository data
  ↓
PostgreSQL
```

It also includes unit tests for the service layer and prevents duplicate repository records by updating existing records when the repository has already been stored.

## 🔮 Future Direction

The original long-term idea for this project was to evolve it into an AI-powered GitHub Repository Intelligence system.

A possible future architecture would be:

```text
GitHub Repository
       ↓
Repository Data
       ↓
Code / Repository Analysis
       ↓
LLM
       ↓
AI-generated Insights
```

Potential future capabilities could include:

* Repository summaries
* Architecture explanations
* Codebase insights
* Improvement suggestions
* AI-powered repository analysis

These features are intentionally **outside the scope of the current project**.

## 🎯 What This Project Represents

This project was built as a practical backend engineering exercise and as a foundation for further AI engineering work.

The final stack is:

```text
Python
  ↓
FastAPI
  ↓
GitHub REST API
  ↓
Service Layer
  ↓
SQLAlchemy
  ↓
PostgreSQL
  ↓
pytest
```

**Project complete. 🚀**
