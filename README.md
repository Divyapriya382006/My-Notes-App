# No-Login Web App (Minimal Authentication System)

## Background / Motivation

During a college laboratory session, I was unable to log in to my Google account because my phone was not available for OTP or second-factor verification. As a result, I could not access my notes, copy lab materials, or save required files during the session.

To avoid complete dependency on OTP-based or multi-factor authentication for low-risk usage, I decided to build a minimal authentication system that allows access to less important content without second verification.

This project is intended only for low-security use cases and is not meant for handling sensitive or critical data.

---

## Project Description

This project is a simple web-based login system built using Flask, HTML, and CSS. It allows users to access basic content using only credentials, without OTP or additional verification layers.

The main focus of the project is simplicity, accessibility, and learning backend fundamentals using Flask.

---

## Features

- Basic login and signup functionality
- No OTP or second-factor authentication
- Simple and clean user interface
- Flask-based backend
- Static CSS styling
- Lightweight and easy to deploy

---

## Tech Stack

- Backend: Flask (Python)
- Frontend: HTML, CSS
- Templating Engine: Jinja2
- Deployment: Render / Localhost

---

## Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS (Jinja2 templates)
- **Authentication:** Supabase Authentication (Email & Password)
- **Database:** Supabase PostgreSQL
- **Environment Management:** python-dotenv
- **Version Control:** Git & GitHub
- **Deployment:** Render

---

## Project Structure

NO LOGIN/
│
├── app.py
├── templates/
│ ├── landing.html
│ ├── login.html
│ ├── signup.html
│ ├── inputpg.html
│ └── contentspg.html
├── static/
│ └── style.css
├── .env
└── README.md


## Conclusion

This project demonstrates how a minimal authentication system can be built to handle low-security use cases when traditional multi-factor authentication is not feasible. By using Flask and simple credential-based access, the application provides a lightweight and accessible solution for scenarios where convenience is prioritized over strict security.

Through this project, I gained hands-on experience with backend development, routing, template rendering, and real-world problem solving under constraints. While this system is not suitable for sensitive data, it serves as an effective learning tool and a practical workaround for limited-access environments such as college lab sessions.



