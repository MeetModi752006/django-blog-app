Django Blog Application

Authentication, Role Management & Content System
Built with Python and Django 4.2

Overview

This project is a fully functional web application developed using Django. It demonstrates how modern web platforms manage user authentication, authorization, and content creation within a secure environment.

The system allows users to register, create blog posts, manage their profiles, and reset passwords through an email-based workflow. It also implements role-based access control, where administrators have broader permissions compared to standard users.

Key Features
User registration with automatic profile creation
Secure login and logout using Django’s built-in authentication system
Password reset via email with time-sensitive tokens
Role-based permissions (Admin and Regular User)
Complete blog post management (create, update, delete with access control)
User profile editing with bio and avatar image
Integrated Django admin panel for managing users and posts
Getting Started
1. Create a Virtual Environment

Set up an isolated Python environment:

python -m venv venv

Activate it:

macOS/Linux:
source venv/bin/activate
Windows:
venv\Scripts\activate
2. Install Dependencies
pip install -r requirements.txt
3. Set Up the Database
python manage.py makemigrations accounts blog
python manage.py migrate
4. Create a Superuser
python manage.py createsuperuser
5. Run the Development Server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/
Project Structure
django_auth_app/
│
├── django_auth_app/        # Core project configuration
│   ├── settings.py
│   └── urls.py
│
├── accounts/               # Authentication and profile management
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── blog/                   # Blog functionality
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── templates/              # HTML templates
│   ├── base.html
│   ├── registration/
│   ├── accounts/
│   └── blog/
│
├── manage.py
└── requirements.txt
User Roles & Permissions
Role	Create Posts	Edit/Delete Any Post	Admin Access
Regular User	Yes	Only own posts	No
Admin	Yes	Yes (all posts)	Yes

Role Management:
Admins can update user roles through the /admin/ dashboard by modifying the UserProfile model.

Password Reset System

The password recovery process includes:

User submits their email
A secure reset link is generated
User sets a new password via the link
User logs in with updated credentials

During development, emails are printed in the console using:

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

For production, configure SMTP settings using environment variables.

Application Routes
URL Path	Description
/	Displays all blog posts
/accounts/register/	User registration page
/accounts/login/	Login page
/accounts/profile/	Profile management
/accounts/password_reset/	Password reset
/blog/post/new/	Create a new post
/admin/	Admin dashboard
Technology Stack
Python 3.12
Django 4.2
SQLite (development database)
Pillow (image processing)
python-decouple (environment variable management)