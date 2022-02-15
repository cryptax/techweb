# Django

## manage.py commands

- Running the server: `python manage.py runserver`
- Handling database modifications: `python manage.py makemigrations appname` and then `python manage.py migrate`
- Viewing SQL commands: `python manage.py sqlmigrate appname 000x`
- Testing API: `python migrate.py shell`
- Create admin password (first time): `python manage.py createsuperuser`
- Modify admin password (forgotten): `python manage.py changepassword admin`
- Deploy static files: `python manage.py collectstatic`
- Squash migrations: `python3 manage.py squashmigrations blah 0006`

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


## Customizing the Django Admin Panel

- Change the URL: in `./mainproj/urls.py`

```python
urlpatterns = [
    path('otherpath/', admin.site.urls),
```

- Change the name: in `./app/admin.py`:

```python
admin.site.site_header = "Administration Panel"
```

- Create specific fields and actions: `./app/admin.py`

```python
from django.contrib import admin
from .models import Malware, Property
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

@admin.action(description="Mark selected items as checked i.e reviewed")
def mark_all_as_reviewed(modeladmin, request, queryset):
    queryset.update(to_check=False)

class MalwareAdmin(admin.ModelAdmin):
    list_display = ('sha256', 'filename', 'insertion_date', 'to_check')
    search_fields = ('sha256', 'filename', 'insertion_date', 'to_check')
    list_filter = ('to_check', )
    date_hierarchy = 'insertion_date'
    actions = [mark_all_as_reviewed]
```


## Database troubleshooting:

1. it is always possible to delete `db.sqlite3` (note this will erase the admin password)
2. and re-run `python manage.py makemigrations appname`
3. `python manage.py migrate`



