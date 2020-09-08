# plantilla django docker-compose

Esta es una plantilla para armar proyectos usando:

- Python 3.8
- Pipenv
- Postgresql
- Django 3.1
- django-environ
- django-crispy-forms
- django-bootstrap4
- django-fontawesome-5

Y se despliega en docker-compose.


# Uso

Antes de empezar configurar el archivo .env, el archivo .env-sample contiene un ejemplo, luego:

    $ pipenv install --dev
    $ docker-compose up --build
    
Se incluye una aplicación simple (e incompleta) de gestión de posts en un blog.
    
# Licencia

Uso libre, django y los otros elementos usados en este proyecto tienen sus respectivas licencias.

2019 Eduardo Díaz

    
    
