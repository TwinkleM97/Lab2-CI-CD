# Flask Contact Form CI/CD Pipeline

This project demonstrates a complete CI/CD pipeline for a simple Flask contact form application using **Jenkins**.

## Technologies Used
- **Flask** – lightweight Python web framework
- **Pytest** – for unit testing
- **Jenkins** – for CI/CD automation
- **GitHub** – source code repository

## Project Structure
```
flask-contact-app/
│
├── app.py                 # Main Flask application
├── test_app.py            # Pytest unit tests
├── requirements.txt       # Python dependencies
├── Jenkinsfile            # Pipeline script
├── templates/form.html    # HTML form template
├── static/style.css       # Basic styling
└── venv/                  # Virtual environment (local only)
```

## Pipeline Stages
The Jenkins pipeline automates the following stages:
1. **Checkout** – Fetch the latest code from GitHub
2. **Install Dependencies** – Install required Python packages
3. **Build** – Import Flask and check app integrity
4. **Test** – Run Pytest test cases
5. **Notify** – Print success/failure message

## Output
- The app runs on `http://127.0.0.1:5000`
- Users can submit contact form data and receive a success message
- Jenkins verifies all code updates via automated tests and reports status