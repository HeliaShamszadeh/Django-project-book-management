# Django Book Borrowing Management System

This is a Django-based backend project that implements a basic system for managing books and their borrowing status. It was developed as a course project to gain hands-on experience with Django's MVT architecture, model design, and basic backend functionality.

---

## 🔧 Features

- Register, edit, delete, and view books
- User management through Django admin panel
- Borrow and return functionality for books
- Server-side form validation
- Admin interface for managing borrowing status

---

## 🧱 Tech Stack

- **Backend**: Python, Django
- **Database**: SQLite (default Django database for development)
- **Architecture**: MVT (Model-View-Template)
- **Admin Panel**: Django Admin
- **Frontend**: Basic Django templates (for testing only)

---

## 📂 Project Structure
├── manage.py 
├── db.sqlite3 
├── bookapp/ # Main Django app 
│ ├── models.py # Book and Borrow models 
│ ├── views.py # Logic and request handling 
│ ├── templates/ # Basic HTML templates 
│ └── admin.py # Admin interface registration 
├── BookManager/ # Main Django project settings 
│ ├── settings.py # Project settings 
│ └── urls.py # URL configuration
