# GIS-Web-App

This repository contains the codebase for the GIS Survey Application, organized into separate folders for backend (`gis-backend`) and (in the future) frontend (`gis-frontend`).

---

## Backend (`gis-backend`)

The backend is implemented using **FastAPI**, **SQLAlchemy (async)**, and **Pydantic v2**, and connects to a PostgreSQL database hosted on Supabase.

### Features

- Async RESTful APIs for survey, property, owner, location, ward, mohalla, and other details
- Supabase PostgreSQL integration
- Automatic table creation on startup
- Pydantic v2 schema validation
- CORS enabled for frontend integration

### Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy (async)
- Pydantic v2
- Supabase (PostgreSQL)
- Uvicorn

### Getting Started

#### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/GIS-Web-App.git
cd GIS-Web-App/gis-backend
```

#### 2. Install Dependencies

It is recommended to use a virtual environment:

```sh
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Linux/Mac

pip install -r requirements.txt
```

#### 3. Configure Environment Variables

Create a `.env` file in the `gis-backend` folder with the following content:

```
DATABASE_URL=postgresql+asyncpg://<user>:<password>@<host>:<port>/<database>
SUPABASE_URL=https://<your-supabase-project>.supabase.co
SUPABASE_KEY=<your-supabase-service-role-key>
```

> **Note:** Replace the placeholders with your actual Supabase credentials.

#### 4. Run the Backend Server

```sh
uvicorn app.main:app --reload
```

The API will be available at [http://localhost:8000](http://localhost:8000).

#### 5. API Documentation

Once the server is running, you can access the interactive API docs at:

- [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)
- [http://localhost:8000/redoc](http://localhost:8000/redoc) (ReDoc)

### Project Structure

```
gis-backend/
│
├── app/
│   ├── api/           # FastAPI routers
│   ├── auth/          # Authentication logic
│   ├── core/          # Config and database setup
│   ├── crud/          # CRUD operations
│   ├── models/        # SQLAlchemy models
│   └── schemas/       # Pydantic schemas
├── .env               # Environment variables
├── requirements.txt   # Python dependencies
└── README.md
```

---

## Frontend (`gis-frontend`)

*The frontend implementation will be added in the future. This folder will contain all client-side code and instructions for running and building the frontend application.*

---

## License

This project is licensed under the MIT License.

