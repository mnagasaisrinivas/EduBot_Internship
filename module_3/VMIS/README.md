# Building_LLM_powered_apps_using_APIs_Short_Term_Module_3

# VMIS - Virtual Mock Interview System

A simple Flask-based web application for collecting user feedback through a form and displaying flash messages. Designed with a clean UI and a sticky footer.

---

## 📦 Features

- Feedback submission form with Name, Email, and Feedback
- Form validation (frontend + backend)
- Flash messages for user notifications
- Sticky footer and centered form layout
- Dark mode toggle button

---

## 🚀 Tech Stack

- Python 3
- Flask
- HTML5, CSS3
- JavaScript (for validation and dark mode)
- Bootstrap (optional, if used)

---

## Project Structure

```
VMIS/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── db.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── feedback_form.html
│   │   ├── feedback_list.html
│   │   └── index.html
│   └── static/
│       └── style.css
│       └── script.js
│
├── run.py
├── feedback.db
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Dhanekula-Edubot/building-llm-po-module4-module3-assignm-mnagasaisrinivas-ca4e30cf-5afdb899.git
cd building-llm-po-module4-module3-assignm-mnagasaisrinivas-ca4e30cf-5afdb899
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python run.py
```