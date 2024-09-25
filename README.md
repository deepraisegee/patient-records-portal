# RECS Patient Records Portal

## Overview

This is a **Patient Records Portal** built with Flask (backend) and HTML, CSS, JavaScript, and jQuery (frontend). The portal allows patients and doctors to register, log in, and manage patient records. It includes authentication, role-based access (patients and doctors), and API communication via Flask.

## Features

- **User Registration and Login** for both patients and doctors.
- **Role-Based Access**:
  - Doctors can manage patient records.
  - Patients can view their records.
- **RESTful API** for CRUD operations (Create, Read, Update, Delete) on patient data.
- **Secure Authentication** using Flask sessions and decorators to protect routes.
- **Responsive Design** using HTML and CSS.
- **AJAX and jQuery** for a smooth user experience.

## Technologies Used

### Frontend:

- HTML, CSS for layout and design
- JavaScript and jQuery for dynamic interaction

### Backend:

- Flask (Python) for handling backend logic
- Jinja2 for templating
- SQLite/MySQL as the database
- Flask-Login for authentication management

## Project Structure

```
/patient-records-portal
│
├── /src
│   ├── /auth
│   │   ├── __init__.py
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── routes.py
│   ├── /static
│   │   ├── /css
│   │   │   ├── auth.css
│   │   │   └── general.css
│   │   ├── /img
│   │   │   ├── favicon.ico
│   │   │   └── logo.png
│   │   └── /js
│   │       └── script.js
│   ├── /templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   └── register.html
│   ├── /tests
│   │   └── __init__.py
│   ├── models.py
│   └── routes.py
├── .gitignore
├── config.py
├── main.py
├── README.md
└── requirements.txt
```
