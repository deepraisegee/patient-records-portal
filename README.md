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

## Installation

### Prerequisites

- Python 3.x
- Flask
- A database (SQLite by default, but you can change to PostgreSQL/MySQL if needed)
- Git (optional)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/deepraisegee/patient-records-portal.git
   cd patient-records-portal
   ```

2. **Set up a virtual environment:**
   ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/Mac
    # On Windows:
    # venv\Scripts\activate
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up the database:**
   Initialize your SQLite (or another database) and create the necessary tables.
   ```bash
    flask db init  # Initializes the database
    flask db migrate  # Creates migration scripts
    flask db upgrade  # Applies migrations to the database
   ```
5. **Run the Flask application:**
   ```bash
    flask run
   ```
   The app will be available at http://127.0.0.1:5000/.

## Usage

### User Registration

- Visit http://127.0.0.1:5000/register to register as a doctor or patient.
- Fill out the registration form with your credentials and role (either patient or doctor).

### User Login

- Visit http://127.0.0.1:5000/login to log in.
- Depending on your role, you will be redirected to the appropriate dashboard:
  - **Patient Dashboard** allows you to view your medical records.
  - **Doctor Dashboard** allows you to manage patients' medical records.

## API Endpoints

For advanced users, there are RESTful API endpoints to interact with patient data. You can use tools like Postman or curl to test the API.

- Get Patient Data: GET /api/patient/<id>
- Create Patient Record: POST /api/patient
- Update Patient Record: PUT /api/patient/<id>
- Delete Patient Record: DELETE /api/patient/<id>

## Contribution

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature (git checkout -b feature/my-feature).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature/my-feature).
5. Create a new Pull Request.

## Authors

**Agiande Beulah**

- GitHub: [MyssyB](https://github.com/MyssyB)
- LinkedIn: [Agiande Beulah](https://github.com/MyssyB)
- Email: [myssyb@gmail.com](mailto:myssyb@gmail.com)

**Adesanmi D. PraiseGod**

- GitHub: [deepraisegee](https://github.com/deepraisegee)
- LinkedIn: [Adesanmi Dayo PraiseGod](https://www.linkedin.com/in/praisegod/)
- Email: [deepraisegee@gmail.com](mailto:deepraisegee@gmail.com)
