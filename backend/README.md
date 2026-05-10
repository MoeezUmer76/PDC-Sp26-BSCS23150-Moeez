Moeez Umer - BSCS23150

# Building Resilient Distributed Systems
## Parallel and Distributed Computing Assignment

This project demonstrates how distributed systems can face synchronization problems when multiple users try to update shared data at the same time.

The assignment implements Optimistic Locking in a FastAPI application to prevent the Lost Update problem.

---

# Features

- FastAPI backend
- SQLite database using SQLAlchemy
- Optimistic Locking using version numbers
- Concurrent update simulation
- Custom middleware header:
  - `X-Student-ID: BSCS23150`

---

# Project Structure

```bash
backend/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── test_concurrent.py
├── requirements.txt
└── README.md


Setup Instructions
1. Clone Repository
git clone https://github.com/MoeezUmer76/PDC-Sp26-BSCS23150-Moeez.git
2. Move Into Backend Folder
cd PDC-Asm/backend
3. Create Virtual Environment
python3 -m venv venv
4. Activate Virtual Environment
Linux / WSL
source venv/bin/activate
Windows
venv\\Scripts\\activate
5. Install Dependencies
pip install -r requirements.txt

Run FastAPI Server
uvicorn main:app --reload
Swagger documentation:
http://127.0.0.1:8000/docs

Run Concurrency Simulation Test
Open a second terminal and run:
python test_concurrent.py

Expected Result

First user update succeeds

Second stale update fails with:
409 Conflict

This demonstrates the Optimistic Locking mechanism.

Middleware Requirement
Every API response includes the custom header:
X-Student-ID: BSCS23150

Technologies Used
Python
FastAPI
SQLAlchemy
SQLite
Requests


Author
Moeez Umer
BSCS23150
