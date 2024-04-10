# Install dependencies
pip install django djangorestframework djangorestframework-simplejwt django-rest-swagger django-mysql

# Project setup
django-admin startproject ecommerce_app

cd ecommerce_app

# App setup
python manage.py startapp core

python manage.py startapp users

python manage.py startapp products

python manage.py startapp orders

# Database migrations
python manage.py makemigrations

python manage.py migrate

# Run the Development Server
python manage.py runserver

# Create admin (aka super user)
python manage.py createsuperuser
