# Building_LLM_powered_apps_using_APIs_Short_Term_Module_4

# VMIS-APP (Visa Mock Interview System)

This project is a Flask-based web application designed to simulate visa mock interviews. It includes user registration, feedback submission, and an admin interface for reviewing user feedback.

## 🧰 Tech Stack

- Python 3.11  
- Flask  
- PostgreSQL  
- SQLAlchemy  
- HTML/CSS/JavaScript  

## 📁 Project Structure
```bash
VMIS-APP/
├── app/
│ ├── init.py # Initialize Flask app and DB
│ ├── config.py # Configuration settings
│ ├── db.py # Database setup
│ ├── models.py # SQLAlchemy models
│ ├── routes.py # Route handlers
│ ├── static/
│ │ ├── styles.css # Stylesheet
│ │ └── script.js # JavaScript file
│ └── templates/
│ ├── base.html
│ ├── index.html
│ └── feedback.html
├── run.py # Entry point
├── requirements.txt # Python dependencies
├── .env # Environment variables (PostgreSQL config)
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <repo_url>
cd VMIS-APP

```

### 2.Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate 
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL
Create a PostgreSQL database named vmis_db.

Update your .env file with database credentials:
```bash
DATABASE_URL=postgresql://<username>:<password>@localhost/vmis_db
```

### 5. Run the app
```bash
python run.py
```
The app will run on http://127.0.0.1:5000.

## ✅ Features
- User form for mock interview feedback

- Admin interface to view submissions

- Responsive front-end using HTML/CSS

- Secure database connection using .env

