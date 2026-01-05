# Enterprise REST API – Django & DRF

A production-style REST API built using **Django**, **Django REST Framework**, and **PostgreSQL**, featuring JWT authentication, role-based permissions, structured logging, clean API versioning, and a minimal client for API validation.

---

##  Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- PostgreSQL
- Simple JWT
- python-dotenv
- Git
- HTML, CSS, JavaScript (minimal API client)

---

##  Features

- Health check API
- JWT authentication (login & protected APIs)
- User registration using Django `User` model
- Message CRUD APIs with database persistence
- Role-based permissions (admin-only endpoints)
- API versioning (`/api/v1`)
- Service layer for business logic
- Centralized API error handling
- Structured logging (info / warning / error)
- PostgreSQL as production database
- Environment-based configuration using `.env`

---

## Project Structure (Simplified)

```
enterprise_rest_api/
├── config/
│   └── settings.py
├── core/
│   └── api/v1/
│       ├── views.py
│       ├── serializers.py
│       ├── urls.py
│       └── services.py
├── client/
│   ├── index.html
│   ├── app.js
│   └── style.css
├── manage.py
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd enterprise_rest_api
```

### 2️⃣ Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Create `.env` file (DO NOT COMMIT)

```env
SECRET_KEY=your_secret_key_here

DB_NAME=enterprise_db
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

The `.env` file is excluded from version control using `.gitignore`.

---

### 5️⃣ Apply migrations
```bash
python manage.py migrate
```

### 6️⃣ Create superuser
```bash
python manage.py createsuperuser
```

### 7️⃣ Run the server
```bash
python manage.py runserver
```

---

##  Authentication (JWT)

### Obtain Access Token
```http
POST /api/token/
```

Payload:
```json
{
  "username": "admin",
  "password": "password"
}
```

Use the token in headers:
```http
Authorization: Bearer <ACCESS_TOKEN>
```

---

## API Endpoints (v1)

| Method | Endpoint                          | Description             |
|------|-----------------------------------|-------------------------|
| GET  | `/api/v1/health/`                 | Health check            |
| POST | `/api/token/`                     | JWT login               |
| POST | `/api/v1/messages/`               | Create message          |
| PATCH| `/api/v1/messages/<id>/`          | Update message          |
| DELETE | `/api/v1/messages/<id>/delete/` | Delete message          |
| GET  | `/api/v1/messages/all/`           | Admin-only message list |

---

##  Minimal API Client

A lightweight **HTML, CSS, and JavaScript** client is included to manually test:

- JWT authentication flow
- Protected API endpoints
- Authorization using Bearer tokens

This client is intended only for **API validation**, not as a full frontend application.

---

##  Permissions

- Authenticated users can create, update, and delete their own messages
- Admin users (`is_staff=True`) can access admin-only endpoints
- Unauthorized access attempts are logged

---

## Logging

- **INFO** → Successful actions (create/update)
- **WARNING** → Unauthorized access attempts
- **ERROR / EXCEPTION** → Unexpected failures

---

##  Key Design Decisions

- Secrets and credentials managed using environment variables
- PostgreSQL used instead of SQLite for production-style configuration
- No virtual environment or local database committed
- Minimal client used instead of frontend frameworks to keep focus on backend

---

##  Status

 Status: Feature-complete (backend-focused)
  
 Backend-focused, interview-ready project  

---

## 👤 Author

**Gokul R Chandran**  
Backend Developer (Django / DRF)
