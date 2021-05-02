# Pizza Ordering

**Pizza Ordering** REST APIs made with Django REST Framework.

API documentation for the project is available [here](docs/rest_api.md).

Swagger documentation: [http://localhost:8000/api/v1/docs/](http://localhost:8000/api/v1/docs/)

Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

### Requirements
- Python (3.7)
- Django (2.2)
- Django REST Framework (3.9)

### Installation - Docker

```
git clone git@github.com:solaman-raji/pizza-ordering.git
cd pizza-ordering

docker-compose -f local.yml build
docker-compose -f local.yml up
```

### Run Test

```
docker-compose -f local.yml run django pytest -s
```

### Create Superuser

```
docker-compose -f local.yml run django python manage.py createsuperuser
```

## Built With

* [Python 3.7](https://docs.python.org/3.7/) - Python version 3.7
* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST Framework](http://www.django-rest-framework.org/) - Used to generate RESTful API
