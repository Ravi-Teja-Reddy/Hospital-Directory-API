#  Hospital Directory API

A RESTful API built with **FastAPI** to manage a directory of hospitals. This project demonstrates clean API design, database integration, pagination, robust error handling, testing, and containerization.

##  Features

- **FastAPI-based CRUD API** with automatic OpenAPI documentation
- **SQLite database** with SQLAlchemy ORM for data persistence
- **Pagination support** for efficient data retrieval
- **Comprehensive error handling** (404, 422, validation errors)
- **Input validation** with Pydantic schemas
- **Unit testing** with pytest
- **Docker containerization** for easy deployment
- **Interactive API documentation** with Swagger UI

##  Requirements

- **Python 3.8+**
- **pip** (Python package manager)
- **Docker** (optional, for containerized deployment)

##  Project Structure

```
Hospital-Directory-API/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application entry point
│   ├── routes.py        # API route definitions
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic request/response models
│   ├── database.py      # Database configuration and setup
│   └── storage.py       # Additional storage utilities
├── tests/
│   └── test_api.py      # Unit tests for API endpoints
├── Dockerfile           # Docker image configuration
├── docker-compose.yaml  # Docker Compose setup
├── requirements.txt     # Python dependencies
├── utils.py            # Utility functions
└── README.md           # Project documentation
```

##  Getting Started

### Option 1: Run Locally (Without Docker)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Hospital-Directory-API
   ```

2. **Create and activate virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the API server**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Access the API**
   - **API Root**: http://localhost:8000/
   - **Interactive Docs**: http://localhost:8000/docs
   - **ReDoc**: http://localhost:8000/redoc

### Option 2: Run with Docker

   ```bash
   # Build the image
   docker build -t hospital-api .
   
   # Run the container
   docker run -d -p 8000:8000 hospital-api
   ```

3. **Access the API**
   - **API Root**: http://localhost:8000/ (with docker-compose) or http://localhost:8000/ (manual)
   - **Interactive Docs**: http://localhost:8000/docs or http://localhost:8000/docs

##  API Endpoints

### Root Endpoint
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/`      | API welcome message and available endpoints |

### Hospital Management
| Method | Endpoint            | Description                        |
|--------|--------------------|------------------------------------|
| GET    | `/hospitals`       | List all hospitals (with pagination) |
| GET    | `/hospitals/{id}`  | Get specific hospital by ID        |
| POST   | `/hospitals`       | Create a new hospital              |
| PUT    | `/hospitals/{id}`  | Update existing hospital           |
| DELETE | `/hospitals/{id}`  | Delete a hospital                  |

### Example Requests

**List hospitals with pagination:**
```bash
GET /hospitals?skip=0&limit=10
```

**Create a new hospital:**
```bash
POST /hospitals
Content-Type: application/json

{
  "name": "General Hospital",
  "address": "123 Main St, City, State",
  "phone": "+1-555-0123",
  "email": "info@generalhospital.com"
}
```

**Update hospital information:**
```bash
PUT /hospitals/1
Content-Type: application/json

{
  "name": "Updated Hospital Name",
  "phone": "+1-555-9999"
}
```

##  Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=app
```

## 🗃️ Database

The application uses **SQLite** as the default database, which is automatically created as `hospitals.db` in the project root when you first run the application.

The database schema includes:
- **Hospital** table with fields: id, name, address, phone, email, created_at, updated_at


---





