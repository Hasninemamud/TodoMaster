# TaskMaster

A personal task manager web application built with Django and TailwindCSS.

## Features

- User authentication (registration, login, logout)
- Task management (create, view, update, delete)
- Task filtering by completion status and priority
- Highlighting of overdue tasks
- Responsive UI with TailwindCSS
- User feedback using Django's messages framework

## Screenshots

### Registration Page
![Registration Page](TodoMaster/screenshots/registration.png)

### Login Page
![Login Page](TodoMaster/screenshots/Login.png)

### Task List
![Task List](TodoMaster/screenshots/task_list.png)

### Task Form
![Task Form](TodoMaster/screenshots/127.0.0.1_8000_task_new_.png)

### Task Detail
![Task Detail](TodoMaster/screenshots/127.0.0.1_8000_task_details.png)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8+ installed
- pip (Python package manager) installed

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/taskmaster.git
cd taskmaster
```

### 2. Create and activate a virtual environment

**On macOS/Linux:**

```bash
python -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root directory:

```bash
touch .env
```

Add the following content to the `.env` file:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Replace `your-secret-key-here` with a secure secret key. You can generate one using:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser (optional)

This step is optional but recommended if you want to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin user.

### 7. Start the development server

```bash
python manage.py runserver
```

### 8. Access the application

Open your web browser and navigate to `http://127.0.0.1:8000/`

## Usage

### Registering an Account

1. Click on the "Register" link in the navigation bar
2. Fill in the registration form with your username, email, and password
3. Click "Register" to create your account
4. You will be redirected to the login page

### Logging In

1. Click on the "Login" link in the navigation bar
2. Enter your username and password
3. Click "Login" to access your dashboard

### Managing Tasks

#### Creating a Task

1. Click on the "New Task" button in the navigation bar
2. Fill in the task details (title, description, due date, priority)
3. Click "Save Task" to create the task

#### Viewing Tasks

1. After logging in, you'll see your task list on the main page
2. Tasks are displayed in a table with their details
3. Overdue tasks are highlighted in red
4. You can filter tasks by completion status and priority using the filter form

#### Updating a Task

1. Click the edit icon (pencil) next to a task in the task list
2. Modify the task details as needed
3. Click "Save Task" to update the task

#### Deleting a Task

1. Click the delete icon (trash can) next to a task in the task list
2. Confirm the deletion on the confirmation page
3. The task will be permanently deleted

#### Viewing Task Details

1. Click the view icon (eye) next to a task in the task list
2. You'll see all the details of the task, including creation and update timestamps

### Logging Out

1. Click on the "Logout" link in the navigation bar
2. You will be logged out and redirected to the login page

## Project Structure

```
taskmaster/
├── taskmaster/          # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py     # Django settings
│   ├── urls.py         # Project URL patterns
│   └── wsgi.py
├── tasks/               # Main application
│   ├── migrations/      # Database migrations
│   ├── __init__.py
│   ├── admin.py         # Admin configuration
│   ├── apps.py          # Application configuration
│   ├── forms.py         # Form definitions
│   ├── models.py        # Data models
│   ├── tests.py         # Unit tests
│   ├── urls.py          # App URL patterns
│   └── views.py         # View functions
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   ├── registration/    # Authentication templates
│   └── tasks/           # Task-related templates
├── static/              # Static files
├── venv/                # Virtual environment
├── db.sqlite3           # SQLite database
├── .env                 # Environment variables
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Technologies Used

- **Backend**: Django 4.2
- **Frontend**: HTML5, TailwindCSS
- **Database**: SQLite (for development)
- **Authentication**: Django's built-in authentication system
- **Icons**: Font Awesome

## API Reference

### Models

#### Task Model

Fields:
- `title`: CharField (max length=200)
- `description`: TextField (blank=True)
- `due_date`: DateField
- `priority`: CharField with choices (LOW, MEDIUM, HIGH)
- `completed`: BooleanField (default=False)
- `user`: ForeignKey to User model (cascade delete)
- `created_at`: DateTimeField (auto_now_add=True)
- `updated_at`: DateTimeField (auto_now=True)

### Views

- `task_list`: Display a list of tasks with filtering options
- `task_detail`: Display details of a specific task
- `task_create`: Create a new task
- `task_update`: Update an existing task
- `task_delete`: Delete a task
- `register_view`: User registration
- `login_view`: User login
- `logout_view`: User logout

