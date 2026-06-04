# Django Authentication & Blog Platform

A Django-based web application that combines secure user authentication with a blogging platform. Users can create accounts, manage their profiles, publish blog posts, and recover forgotten passwords. The system also includes role-based permissions to ensure proper access control.

---

## Project Overview

This project was developed to gain hands-on experience with core Django concepts and real-world web application development. It focuses on two key areas:

### User Authentication

Users can register, log in, update their profiles, upload profile pictures, and reset their passwords through an email-based recovery system.

### Blog Management

Authenticated users can create and manage their own blog posts, while administrators have additional privileges to manage content across the platform.

---

## Key Features

### User Accounts

* Secure user registration and login
* Logout functionality using Django's authentication system
* Automatic profile creation for new users
* Password reset via email with secure, time-limited links

### Profile Management

* Update personal information
* Upload and manage profile avatars
* Store additional user-related details separately from the default User model

### Blog System

* Create, view, update, and delete blog posts
* Users can edit or remove only their own posts
* Administrators can manage all posts on the platform

### Administration

* Full access through Django's built-in admin panel
* Manage users, profiles, and blog content efficiently

---

## Technologies Used

| Component             | Technology      |
| --------------------- | --------------- |
| Programming Language  | Python 3.12     |
| Web Framework         | Django 4.2      |
| Database              | SQLite          |
| Image Processing      | Pillow          |
| Environment Variables | python-decouple |

---

## Installation Guide

### Clone the Repository

```bash
git clone https://github.com/your-username/django-auth-blog.git
cd django-auth-blog
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

### Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create an Administrator Account

```bash
python manage.py createsuperuser
```

### Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## Project Structure

```text
django_auth_app/
│
├── django_auth_app/
│   ├── settings.py
│   └── urls.py
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── templates/
│   ├── base.html
│   ├── registration/
│   ├── accounts/
│   └── blog/
│
├── media/
├── manage.py
└── requirements.txt
```

---

## Application Routes

| URL                         | Description                     |
| --------------------------- | ------------------------------- |
| `/`                         | Displays all blog posts         |
| `/accounts/register/`       | Create a new account            |
| `/accounts/login/`          | Sign in to an existing account  |
| `/accounts/profile/`        | View and update profile details |
| `/accounts/password_reset/` | Request a password reset        |
| `/blog/post/new/`           | Create a new blog post          |
| `/blog/post/<id>/`          | View a specific post            |
| `/blog/post/<id>/edit/`     | Edit a post                     |
| `/blog/post/<id>/delete/`   | Delete a post                   |
| `/admin/`                   | Django administration panel     |

---

## Permission Levels

### Regular User

* Create blog posts
* Edit own posts
* Delete own posts

### Administrator

* All regular user permissions
* Edit any post
* Delete any post
* Access the Django admin dashboard

User roles can be modified through the admin panel by updating the associated profile.

---

## Password Reset Configuration

For development purposes, password reset emails are displayed directly in the terminal rather than being sent to a real email address.

```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

When deploying the application, this setting should be replaced with a proper SMTP email service and sensitive credentials should be stored using environment variables.

---

## About the Developer

**Meet**

BCA Graduate and Python/Django Developer with an interest in building practical web applications and continuously improving backend development skills.

---

## License

This project is distributed under the MIT License and is available for educational and personal use.
