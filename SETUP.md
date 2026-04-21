# Project Setup Guide: Student Organization Automated Voting System (SOAVS)

This guide will walk you through setting up and running the SOAVS application on your local machine.

## Prerequisites
Before you begin, ensure you have the following installed:
- **Python 3.11+**
- **Node.js (LTS version)**
- **MySQL Server** (XAMPP or MySQL Workbench)

---

## 1. Database Setup
The application uses a MySQL database named `voting`.

1. Start your MySQL server (via XAMPP or another service).
2. Create a database named `voting`.
3. Import the `voting.sql` file located in the root directory:
   ```bash
   mysql -u root -p voting < voting.sql
   ```
   *(Note: If you have no password, just omit `-p`)*

---

## 2. Backend Setup (Django)
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Activate the virtual environment:
   - **Windows:** `..\venv\Scripts\activate`
   - **macOS/Linux:** `source ../venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install django djangorestframework django-cors-headers mysqlclient djangorestframework-simplejwt
   ```
4. Run migrations (to ensure schema is up to date):
   ```bash
   python manage.py migrate
   ```
5. Start the backend server:
   ```bash
   python manage.py runserver
   ```
   The backend will be available at `http://127.0.0.1:8000/`.

---

## 3. Frontend Setup (Vue + Vite)
1. Open a new terminal and navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
   The frontend will be available at `http://localhost:5173/`.

---

## Accessing the Application
- **Main Portal:** `http://localhost:5173/`
- **Admin Dashboard:** `http://127.0.0.1:8000/admin/` (Requires a superuser)

### Creating an Admin User
If you need to access the Django admin, run this command in the `backend` directory:
```bash
python manage.py createsuperuser
```
Follow the prompts to set your username and password.
