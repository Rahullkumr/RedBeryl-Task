# RedBeryl-Task
Task to be completed within 6 hours


## Task

build a system to take a file (image/pdf) of either aadhar card, passport or driving license as input from the ui and extract the details from it and store those details into a database.
must use OOP, solid principles, design patterns, REST api, FastAPI and any database

## How to run

1. Install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn jinja2
```

2. Install python multipart

```python
pip install python-multipart
```

3. Run the server

```python
uvicorn main:app --reload
```

4. Access the UI: Open http://127.0.0.1:8000/ in your browser.

## Folder structure

```
project/
├── app/
│   ├── main.py          # FastAPI app entry point
│   ├── routes.py        # API routes
│   ├── services.py      # Business logic and OCR processing
│   ├── models.py        # Database models
│   ├── database.py      # SQLite connection setup
│   ├── utils.py         # Utility functions
│   ├── templates/       # Frontend HTML templates
│   ├── static/          # Static files (CSS, JS)
├── tests/               # Test cases
├── README.md            # Documentation
├── requirements.txt     # Python dependencies

```