# 🧩 Django CRUD API with Django REST Framework

This is a simple **CRUD (Create, Read, Update, Delete)** API built using **Django** and **Django REST Framework**. It uses **function-based views** and demonstrates how to serialize, deserialize, and handle HTTP methods properly in a RESTful way.

---

## 🚀 Features

-  Create, Read, Update, Delete operations
-  Function-Based Views using `@api_view`
-  Serialization & Deserialization of data
-  Proper HTTP status handling (200, 201, 400, 404)
-  Tested thoroughly using Postman

---

##  API Endpoints (Example: Student API)

| Method | Endpoint                      | Description                 |
|--------|-------------------------------|-----------------------------|
| GET    | `/student-list/`              | List all students           |
| GET    | `/student-detail/<id>/`       | Get a single student        |
| POST   | `/student-create/`            | Create a new student        |
| PUT    | `/student-update/<id>/`       | Update an existing student  |
| DELETE | `/student-delete/<id>/`       | Delete a student            |

---

##  Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/susanacharya12/CRUD-API.git
cd CRUD-API

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt


If requirements.txt doesn’t exist, run
pip install django djangorestframework

Then
pip freeze > requirements.txt

4. Apply migrations
python manage.py migrate

5. Run the server
python manage.py runserver
Now visit http://127.0.0.1:8000/ in your browser or use Postman to test endpoints.

 Tech Stack
Python 3.x
Django
Django REST Framework
SQLite (default DB)
Postman (API testing)

 What I Learned
How REST APIs work in Django
Creating serializers and deserializers
Function-based API views with DRF
Using status codes for API responses
Testing endpoints via Postman

 GitHub Repo
https://github.com/susanacharya12/CRUD-API

 Contributions
If you'd like to contribute or suggest improvements, feel free to fork this repo and create a pull request!





