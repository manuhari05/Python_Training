### Basic Notes on Django Installation and Models

#### 1. Introduction to Django
- Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- It follows the Model-View-Template (MVT) architectural pattern.

#### 2. Installation

**Requirements:**
- Python (version 3.6 or later recommended)
- pip (Python package installer)

**Steps to Install Django:**
1. **Install Python:**
   - Download from the official [Python website](https://www.python.org/downloads/).
   - Ensure Python is added to your system's PATH.

2. **Install pip:**
   - Usually comes with Python. Check by running `pip --version` in the command line.

3. **Create a Virtual Environment (Optional but Recommended):**
   - Navigate to your project directory: 
     ```bash
     cd your_project_directory
     ```
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - Windows: `venv\Scripts\activate`
     - macOS/Linux: `source venv/bin/activate`

4. **Install Django:**
   - Use pip to install Django:
     ```bash
     pip install django
     ```

5. **Verify Installation:**
   - Check the installed Django version:
     ```bash
     python -m django --version
     ```

#### 3. Creating a New Django Project
1. **Start a Project:**
   ```bash
   django-admin startproject project_name
   ```
2. **Navigate into the Project Directory:**
   ```bash
   cd project_name
   ```

3. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
   - Access the development server at `http://127.0.0.1:8000/`.

#### 4. Creating Models in Django

**What are Models?**
- Models are Python classes that define the structure of your database. They represent the data you want to store.

**Steps to Create Models:**
1. **Create an App:**
   ```bash
   python manage.py startapp app_name
   ```

2. **Define Models:**
   - Open `models.py` in your app directory and define your model classes.
   ```python
   from django.db import models

   class MyModel(models.Model):
       field_name = models.CharField(max_length=100)
       another_field = models.IntegerField()
       created_at = models.DateTimeField(auto_now_add=True)
   ```

3. **Register the App:**
   - Add the app to `INSTALLED_APPS` in `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'app_name',
   ]
   ```

4. **Create and Apply Migrations:**
   - Create migrations for your model:
   ```bash
   python manage.py makemigrations
   ```
   - Apply migrations to the database:
   ```bash
   python manage.py migrate
   ```

5. **Using the Django Admin:**
   - Register your model in `admin.py` to manage it through the Django admin interface:
   ```python
   from django.contrib import admin
   from .models import MyModel

   admin.site.register(MyModel)
   ```

6. **Create a Superuser:**
   - Run the following command to create an admin user:
   ```bash
   python manage.py createsuperuser
   ```
   - Access the admin interface at `http://127.0.0.1:8000/admin/`.

#### 5. Conclusion
- Django simplifies web development and provides robust features for managing databases through models.
- Understanding installation and model creation is essential for building Django applications.

#### 6. Additional Resources
- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/) 

# Models