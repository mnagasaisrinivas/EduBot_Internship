# Building_LLM_powered_apps_using_APIs_Short_Term_Module_1

## User Data Entry & Validation Script

This Python project is designed to accept user input (name, email, and age), validate it based on specific constraints, and log both valid entries and errors using Python's `logging` module.

---

## 🚀 Features

- Validates:
  - **Name** – Only alphabetical characters.
  - **Email** – Valid email format (e.g., user@example.com).
  - **Age** – Positive integers only.
- Logs:
  - Validation errors (logged as ERROR).
  - Successful data entries (logged as INFO).
  - Saves logs to a file at `./app_logs/app_logs.txt`.

---

## 📁 Files

- `main.py` – The core script that performs input, validation, and logging.
- `test_cases.txt` – Sample input/output examples for manual review and testing.
- `app_logs.txt` – Log file containing entries and errors.

---

## 🛠️ How to Run

1. Ensure you have Python 3 installed.
2. Open a terminal and navigate to the project directory.
3. Run the script:

```bash
python main.py
```
