# To setup PMS Project Guide

This README provides instructions for setting up and running a Django project on your local machine.

---

## Prerequisites

Before starting, ensure you have the following installed on your system:

- Python (>= 3.8)
- pip (Python package manager)
- Virtualenv (optional but recommended)
- Git
- A database system (e.g., SQLite, PostgreSQL, MySQL)

---

## Installation

Follow these steps to set up the project:

### 1. Clone the Repository

```bash
$ git clone https://github.com/AmritSingtan2001/RealState.git
$ cd RealState
```

### 2. Create and Activate a Virtual Environment (Optional but Recommended)
#### On Windows:
```bash
$ python -m venv env
$ .\env\Scripts\activate
```

### 3. Install Dependencies

Install the required packages listed in `requirements.txt`:
```bash
$ pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory and set up the following environment variables:

```plaintext
SECRET_KEY=<your_secret_key>
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=<your_database_url>
```

For database setup, you can use .

### 5. Apply Migrations

Run the following commands to set up the database:
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### 6. Create a Superuser (Optional)

Create an admin user to access the Django admin interface:
```bash
$ python manage.py createsuperuser
```

### 7. Run the Development Server

Start the server using:
```bash
$ python manage.py runserver
```

The project will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Contributing

If you wish to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request.

---

## Troubleshooting

- **Database Errors:** Ensure your database is running and correctly configured in the `.env` file.
- **Dependency Issues:** Check `requirements.txt` for any package version conflicts.

Feel free to open an issue if you encounter problems.
