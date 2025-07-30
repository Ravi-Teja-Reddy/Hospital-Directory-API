#  Hospital Directory API

A RESTful API built with **FastAPI** to manage a directory of hospitals. This project demonstrates clean API design, database integration, pagination, testing, and Dockerization.

---

##  Features

- FastAPI-based CRUD API
-  SQLite persistence with SQLAlchemy
-  Pagination support for listing hospitals
-  Robust error handling (404, 422, etc.)
-  Unit tested with pytest
-  Dockerized for easy deployment

---

##  Requirements

- Python 3.8+
- pip (Python package manager)
- Docker (optional for containerized usage)

---

## 📁 Project Structure

hospital_directory/
├── app/
│ ├── init.py
│ ├── main.py # FastAPI app entrypoint
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic models
│ ├── database.py # DB setup (SQLite or in-memory)
│ └── routes.py # API route definitions
├── tests/
│ └── test_api.py # Unit tests
├── Dockerfile
├── requirements.txt
└── README.md



---

##  Run Locally

### ▶️ Run without Docker

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/hospital_directory.git
cd hospital_directory

2. Create virtual environment

python3 -m venv myvenv
source myvenv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the API
uvicorn app.main:app --reload



Run with Docker

1. Build the image
docker build -t hospital-api .

2. Run the container
docker run -d -p 8000:8000 hospital-api


API Endpoints

| Method | Endpoint          | Description                      |
| ------ | ----------------- | -------------------------------- |
| GET    | `/hospitals`      | List hospitals (with pagination) |
| GET    | `/hospitals/{id}` | Get hospital by ID               |
| POST   | `/hospitals`      | Add new hospital                 |
| PUT    | `/hospitals/{id}` | Update hospital details          |
| DELETE | `/hospitals/{id}` | Delete a hospital                |



Example: Pagination
GET /hospitals?skip=0&limit=5



 Run Tests
 pytest



