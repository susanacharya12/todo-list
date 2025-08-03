
 ##  To-Do List Project
 
A simple, user-authenticated To-Do List web application built with Django. Users can register, log in, and manage their personal tasks with a clean and responsive interface.

---

##  Features

-  User registration and login/logout
-  Add, view, complete, delete, and search tasks
-  Each user has a private task list
-  Task creation and completion tracking
-  Responsive and user-friendly UI

---
##  Project Structure
```
todo-list/
├── manage.py
├── db.sqlite3
├── screenshots/
│ ├── login.png
│ └── todo-list.png
├── todo/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
│ ├── migrations/
│ └── templates/
└── todo_project/
├── init.py
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py
```





---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/susanacharya12/todo-list.git
cd todo-list


2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install django

4. Apply Migrations

python manage.py migrate

5. Run the Development Server

python manage.py runserver

Visit  http://127.0.0.1:8000/ in your browser.




##  Screenshots

### Login Page
![Login Page](screenshots/login.png)

###  To-Do List Page
![To-Do List Page](screenshots/todo-list.png)



Usage
Register for a new account or log in with existing credentials.
Add tasks using the input form.
Mark tasks as complete/incomplete by clicking the checkmark.
Delete tasks using the delete icon.
Search tasks using the search bar.


Code Overview
models.py – Defines the Task model with user, title, completed status, and creation date.
forms.py – Contains forms for user registration and task creation.
views.py – Handles user authentication and task CRUD operations.
templates/ – Contains HTML files like login.html, register.html, todo_list.html, etc.


 License
This project is created for Project purposes only.


 Author
Susan Acharya

