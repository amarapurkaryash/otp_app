<h1 align="center">otp_app</h1>

<p align="center">A robust Django application for secure One-Time Password (OTP) generation and verification via email.</p>

<div align="center" class="gemini-badges">
<img src="https://img.shields.io/github/stars/amarapurkaryash/otp_app?style=for-the-badge&label=Stars&color=FBBF24&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBmaWxsPSJ3aGl0ZSI%2BPHBhdGggZD0iTTEyIDE3LjI3TDE4LjE4IDIybC0xLjY0LTcuMDNMMjIgOS4yNGwtNy4xOS0uNjFMMTIgMiA5LjE5IDguNjMgMiA5LjI0bDYuNDYgNS55NEw2LjgyIDIyIDEyIDE3LjI3eiIvPjwvc3ZnPg%3D%3D&logoColor=white" alt="Stars Badge">
<img src="https://img.shields.io/github/forks/amarapurkaryash/otp_app?style=for-the-badge&label=Forks&color=34D399&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBmaWxsPSJub25lIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjIuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48bGluZSB4MT0iNiIgeTE9IjMiIHgyPSI2IiB5Mj0iMTUiPjwvbGluZT48Y2lyY2xlIGN4PSIxOCIgY3k9IjYiIHI9IjMiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjYiIGN5PSIxOCIgcj0iMyI%2BPC9jaXJjbGU%2BPHBhdGggZD0iTTE4IDlhOSA5IDAgMCAxLTkgOSI%2BPC9wYXRoPjwvc3ZnPg%3D%3D&logoColor=white" alt="Forks Badge">
<img src="https://img.shields.io/github/issues-raw/amarapurkaryash/otp_app?style=for-the-badge&label=Issues&color=F87171&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBmaWxsPSJ3aGl0ZSI%2BPHBhdGggZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyczQuNDggMTAgMTAgMTAgMTAtNC40OCAxMC0xMFMxNy41MiAyIDEyIDJ6bTEgMTVoLTJ2LTJoMnYyem0wLTRoLTJWN2gydjZ6Ii8%2BPC9zdmc%2B&logoColor=white" alt="Issues Badge">
<img src="https://img.shields.io/github/watchers/amarapurkaryash/otp_app?style=for-the-badge&label=Watchers&color=60A5FA&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBmaWxsPSJ3aGl0ZSI%2BPHBhdGggZD0iTTEyIDQuNUM3IDQuNSAyLjczIDcuNjEgMSAxMmMxLjczIDQuMzkgNiA3LjUgMTEgNy41czkuMjctMy4xMSAxMS03LjVDMjIuMjcgNy42MSAxNyA0LjUgMTIgNC41ek0xMiAxN2E1IDUgMCAxIDEgMC0xMCA1IDUgMCAwIDEgMCAxMHptMC04YTMgMyAwIDEgMCAwIDYgMyAzIDAgMCAwIDAgLTZ6IiAvPjwvc3ZnPg%3D%3D&logoColor=white" alt="Watchers Badge">
<img src="https://img.shields.io/github/last-commit/amarapurkaryash/otp_app?style=for-the-badge&label=Last%20Commit&color=A78BFA&logo=git&logoColor=white" alt="Last Commit Badge">
<img src="https://img.shields.io/github/sponsors/amarapurkaryash?style=for-the-badge&label=Sponsors&color=EC4899&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBmaWxsPSJ3aGl0ZSI%2BPHBhdGggZD0iTTEyIDIxLjM1bC0xLjQ1LTEuMzJDNS40IDE1LjM2IDIgMTIuMjggMiA4LjVDMiA1LjQyIDQuNDIgMyA3LjUgM2MxLjc0IDAgMy40MS44MSA0LjUgMi4wOUMxMy4wOSAzLjgxIDE0Ljc2IDMgMTYuNSAzIDE5LjU4IDMgMjIgNS40MiAyMiA4LjVjMCAzLjc4LTMuNCA2Ljg2LTguNTUgMTEuNTRMMTIgMjEuMzV6Ii8%2BPC9zdmc%2B&logoColor=white" alt="Sponsors Badge">
<img src="https://img.shields.io/badge/Python-2DD4BF?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
<img src="https://img.shields.io/badge/Django-FB923C?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge">
<img src="https://img.shields.io/badge/HTML5-34D399?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5 Badge">
<img src="https://img.shields.io/badge/CSS3-FBBF24?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3 Badge">
<img src="https://img.shields.io/badge/DotEnv-F87171?style=for-the-badge&logo=dotenv&logoColor=white" alt="DotEnv Badge">
<img src="https://img.shields.io/badge/Gmail-60A5FA?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail Badge">
</div>

## Table of Contents

* [Overview](#overview)
* [Tech Stack](#tech-stack)
* [Key Features](#key-features)
* [Key Functions](#key-functions)
* [Important Files](#important-files)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Deployment](#deployment)
* [References](#references)
* [Acknowledgments](#acknowledgments)

## Overview

The `otp_app` project is a robust Django application designed to provide a secure and efficient One-Time Password (OTP) authentication system. It facilitates the generation, delivery via email, and verification of time-sensitive OTPs, making it suitable for implementing two-factor authentication or secure transaction confirmations. This application is built with Python and Django, emphasizing simplicity and functionality to help users quickly integrate OTP capabilities into their projects.

Whether you're looking to understand OTP mechanisms, integrate them into an existing Django project, or learn about secure email handling within a web application, `otp_app` offers a clear and functional example.

## Tech Stack

This project is built using a modern and robust set of technologies:

### Languages
*   Python
*   HTML
*   CSS

### Frameworks & Runtimes
*   Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.

### Libraries & Dependencies
*   asgiref: ASGI (Asynchronous Server Gateway Interface) reference implementation, enabling asynchronous capabilities in Django.
*   python-dotenv: Reads key-value pairs from a `.env` file and sets them as environment variables.
*   sqlparse: A non-validating SQL parser for Python.

### APIs & Services
*   Gmail SMTP: Used for sending One-Time Passwords via email.

## Key Features

This project provides a robust One-Time Password (OTP) system for secure authentication workflows. Here are its primary capabilities:

*   **Secure OTP Generation:** Generates unique, time-sensitive 6-digit OTPs for enhanced security.
*   **Email-Based Delivery:** Reliably sends OTPs to user-specified email addresses using SMTP.
*   **OTP Verification:** Allows users to submit their received OTP for validation against generated codes.
*   **Time-Limited Validity:** Ensures OTPs have a short expiration window (e.g., 5 minutes) to prevent misuse.
*   **Automatic OTP Invalidation:** Expired or successfully used OTPs are automatically invalidated and removed from the system.
*   **User Feedback:** Provides clear messages to users regarding OTP status (sent, verified, invalid, expired).

## Key Functions

Here are some of the core functions that drive the `otp_app` project:

### `index(request)`
This function serves as the entry point for the application's home page. It takes an HTTP request object and renders the `home/index.html` template, providing a simple landing page for users.

### `generate_code()`
This utility function is responsible for creating a 6-digit One-Time Password. It uses Python's `random` module to produce a secure, numeric code that is then used for verification.

### `secure_otp_home(request)`
This function handles the landing page specifically for the secure OTP functionality. It renders the `secure_otp/index.html` template, guiding users to either request or verify an OTP.

### `request_otp(request)`
This is a crucial view function that manages the request process for an OTP. When a user submits their email via a POST request, it validates the input, calls `generate_code()` to create an OTP, stores it in the database, and then sends the OTP to the provided email address. It then redirects the user to the OTP verification page.

### `verify_otp(request)`
This view function handles the verification of submitted OTPs. Upon receiving an email and OTP via a POST request, it retrieves the stored OTP entry, checks if the OTP matches, and importantly, verifies if the OTP has expired. If successful, the OTP entry is deleted for security; otherwise, appropriate error messages are displayed.

## Important Files

*   `.env.example`: An example file for setting up required environment variables, specifically for Gmail SMTP credentials.
*   `requirements.txt`: Lists all Python dependencies required for the project.
*   `manage.py`: Django's command-line utility for administrative tasks.
*   `otp_project/settings.py`: The main Django settings file, configuring the entire project.
*   `otp_project/urls.py`: The root URL configuration for the Django project.
*   `home/`: A Django app within the project, likely serving as the main entry point or generic pages.
*   `home/views.py`: Contains view functions for the `home` app.
*   `home/templates/home/index.html`: The main template for the home page.
*   `secure_otp/`: Another Django app responsible for OTP generation and verification logic.
*   `secure_otp/models.py`: Defines the database model for storing OTP entries.
*   `secure_otp/views.py`: Contains view functions for handling OTP requests and verification.

## Getting Started

To get a local copy of this project up and running, follow these simple steps.

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

*   Python 3.8+
*   pip (Python package installer)
*   Git

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/amarapurkaryash/otp_app.git
    cd otp_app
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment variables:**
    *   Copy the example environment file:
        ```bash
        cp .env.example .env
        ```
    *   Open the newly created `.env` file and fill in your Gmail SMTP credentials. You'll need to generate an App Password for your Gmail account if you have 2-Factor Authentication enabled.
        ```
        GMAIL_ADDRESS=yourgmail@gmail.com
        GMAIL_APP_PASSWORD=yourapppassword
        ```

5.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

Your application should now be running locally, typically accessible at `http://127.0.0.1:8000/`.

## Usage

Once the `otp_app` is set up and running, you can interact with it through your web browser.

1.  **Access the application:** Open your browser and navigate to the local server address (e.g., `http://127.0.0.1:8000/`).

2.  **Request an OTP:** On the application's interface, you will find a form to request an OTP. Enter the email address where you wish to receive the OTP.

3.  **Check your email:** After submitting your email, an OTP will be sent to the specified address. It will typically be a 6-digit code with a limited validity period (e.g., 5 minutes).

4.  **Verify the OTP:** Return to the application and enter the received OTP along with your email address into the verification form.

5.  **Receive feedback:** The system will inform you if the OTP was successfully verified, if it's invalid, or if it has expired. A successfully verified OTP is then invalidated.

## Deployment

This Django application can be deployed to various platforms. Here's a general guide for a platform like Render or Heroku, which are well-suited for Python/Django applications:

1.  **Prepare your application:**
    *   Ensure all dependencies are listed in `requirements.txt`.
    *   Make sure your `settings.py` is configured for production, including `DEBUG = False`, `ALLOWED_HOSTS`, and appropriate database settings.
    *   Collect static files: `python manage.py collectstatic`

2.  **Choose a platform (e.g., Render, Heroku):**
    *   **Render:** Connect your GitHub repository to Render. Configure a web service, specifying `Gunicorn` or `uWSGI` as your web server, and set your `start command` (e.g., `gunicorn otp_project.wsgi:application --bind 0.0.0.0:$PORT`). Set up environment variables as needed (e.g., `GMAIL_ADDRESS`, `GMAIL_APP_PASSWORD`).
    *   **Heroku:** Install the Heroku CLI. Create a Heroku app (`heroku create`). Push your code to Heroku (`git push heroku main`). Provision a PostgreSQL database addon (`heroku addons:create heroku-postgresql:hobby-dev`). Run migrations (`heroku run python manage.py migrate`). Set environment variables (`heroku config:set GMAIL_ADDRESS=yourgmail@gmail.com GMAIL_APP_PASSWORD=yourapppassword`).

3.  **Database Setup:** Configure your chosen platform's database (e.g., PostgreSQL for Render/Heroku) and update your `otp_project/settings.py` to connect to it.

4.  **Environment Variables:** Crucially, set your `GMAIL_ADDRESS` and `GMAIL_APP_PASSWORD` environment variables on the hosting platform to ensure email sending functionality works in production.

Remember to consult the specific documentation for your chosen hosting provider for detailed instructions.

## References

*   [Python Documentation](https://docs.python.org/3/) - The official documentation for the Python programming language.
*   [Django Documentation](https://docs.djangoproject.com/en/stable/) - Comprehensive guide to the Django web framework.
*   [HTML Living Standard](https://html.spec.whatwg.org/multipage/) - The current standard for HTML5.
*   [MDN Web Docs - CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - A rich resource for Cascading Style Sheets.
*   [python-dotenv GitHub](https://github.com/theskumar/python-dotenv) - Repository and documentation for the python-dotenv library.
*   [asgiref GitHub](https://github.com/django/asgiref) - The ASGI reference implementation, used by Django.
*   [sqlparse GitHub](https://github.com/andialbrecht/sqlparse) - Non-validating SQL parser for Python.
*   [Gmail Help](https://support.google.com/mail) - Support and guides for using Gmail, including generating App Passwords for SMTP.

## Acknowledgments

This README was generated with [Nolthren](https://github.com/amarapurkaryash/Nolthren) & Gemini AI.
