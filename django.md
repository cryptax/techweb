# Django

## manage.py commands

- Running the server: `python manage.py runserver`
- Handling database modifications: `python manage.py makemigrations appname` and then `python manage.py migrate`
- Viewing SQL commands: `python manage.py sqlmigrate appname 000x`
- Testing API: `python migrate.py shell`
- Create admin password (first time): `python manage.py createsuperuser`
- Modify admin password (forgotten): `python manage.py changepassword admin`


## Creating a new model

- Create a new model in `models.py`
- If you want the table to be managable by the admin website, add it to `admin.py`

```python
from .models import Malware, Packer

admin.site.register(Malware)
admin.site.register(Packer)
```

- Initialize its database: see [here](https://izziswift.com/django-1-7-no-migrations-to-apply-when-run-migrate-after-makemigrations/)


```
python manage.py makemigrations appname
python manage.py migrate
```

To create initial data in the db: [here](https://docs.djangoproject.com/en/3.2/topics/migrations/#data-migrations).

## Favicon

- Adding favicon: https://simpleit.rocks/python/django/django-favicon-adding/

## Database troubleshooting:

1. it is always possible to delete `db.sqlite3` (note this will erase the admin password)
2. and re-run `python manage.py makemigrations appname`
3. `python manage.py migrate`



