# Trading CRM Backend

Backend API for the Trading CRM application built with FastAPI.

## Features

* User Authentication (JWT)
* User Registration & Login
* Trade Management

  * Create Trade
  * Update Trade
  * Delete Trade
  * View Trades
* Dashboard Analytics
* Trade Statistics
* MySQL Database Integration
* REST API Architecture

---

## Tech Stack

* FastAPI
* SQLAlchemy
* MySQL
* Pydantic
* JWT Authentication
* Uvicorn
* Python

---

## Project Structure

```text
.
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── routers/
│   ├── users.py
│   ├── trades.py
│   └── dashboard.py
├── requirements.txt
└── .env
```

---

## Environment Variables

Create a `.env` file:

```env
MYSQL_USERNAME=your_username
MYSQL_PASSWORD=your_password
MYSQL_HOST=your_host
MYSQL_DATABASE=your_database

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Locally

Start the development server:

```bash
uvicorn main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```

---

## Authentication

Protected endpoints require a JWT token.

Example:

```http
Authorization: Bearer <token>
```

---

## Main Endpoints

### Authentication

```http
POST /register
POST /login
```

### Trades

```http
GET    /trades
GET    /trades/{id}
POST   /trades
PUT    /trades/{id}
DELETE /trades/{id}
```

### Dashboard

```http
GET /dashboard
```

### Recent Trades

```http
GET /trades/recent
```

---

## Deployment

Backend is deployed using Render.

Production URL:

```text
https://tradingcrmbackend-1.onrender.com
```

---

## Future Improvements

* Trade screenshots
* Trade tags
* Strategy analytics
* Risk-to-reward tracking
* Equity curve visualization
* Advanced performance metrics
* Multi-market support (Forex, Stocks, Crypto)

---

## Author

John Ang

Trading CRM – A personal trading journal and analytics platform for tracking and improving trading performance.
