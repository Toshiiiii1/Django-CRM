# CRM procject with Django

Build a CRM (Customer Relationship Management) App with Django, Python, and MySQL.

Source: [![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/t10QcFx7d5k/0.jpg)](http://www.youtube.com/watch?v=t10QcFx7d5k)

## Installation & Setup

Create virtual enviroment in Python

```bash
python -m venv virt
```

Enable virtual environment

```bash
source virt/Scripts/activate
```

Install Django

```bash
pip install Django
```

Install mysql-connector and mysqlclient

```bash
pip install mysql-connector-python
pip install mysqlclient
```

Create project

```bash
django-admin startproject dcrm
```

Create app

```bash
python manage.py startapp website
```

## Usage

```bash
python manage.py runserver
```