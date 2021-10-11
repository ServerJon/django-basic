# DJANGO BASIC PROJECT

El siguiente proyecto se puede utilizar como plantilla base para crear cualquier proyecto con el _framework_ de *Django*.

## Configuración básica

Para utilizar este proyecto debemos de seguir los siguientes pasos.

### 1. Descargar el proyecto desde este mismo repositorio

    git clone git@github.com:ServerJon/django-basic.git

### 2. Cambiar el nombre del proyecto

Cambiar cualquier referencia de *django_basic* por el nombre de tu proyecto. Los ficheros a modificar son:

- [manage.py](https://github.com/ServerJon/django-basic/blob/main/manage.py)
- Dockerfile
- docker-compose.yml
- Carpeta raíz django_basic
- [asgi.py](https://github.com/ServerJon/django-basic/blob/main/django_basic/asgi.py)
- Carpeta settings (y cualquier fichero hijo de configuración: base, dev, prod, etc)
- [wsgi.py](https://github.com/ServerJon/django-basic/blob/main/django_basic/wsgi.py)

TODO: Crea un script para hacer esto de forma automática

### 3. Levantar el entorno de trabajo

El proyecto está configurado para trabajar con los contenedores de Docker:

    docker-compose up

Una vez levantado el entorno podríamos trabajar dentro del mismo contenedor con toda la configuración instalada como por ejemplo con PyCharm o VSCode.

Si por el contrario queremos trabajar desde un entorno en local se recomienda utilizar un entorno virtual para poder trabajar. Se recomienda seguir los siguientes pasos:

- Comprobar que se tiene instalado python en una de sus últimas versiones, el proyecto trabaja con python3.
- Se recomienda utilizar un gestor de versiones de python como por ejemplo [pyenv](https://github.com/pyenv/pyenv).
- Crear un entorno virtual de trabajo e instalar con pip los modulos del fichero _requirements.txt_.

## Configuración a tener en cuenta

1. Cuando se crea una nueva aplicación desde el docker de django se crearán los permisos como usuario root por lo que deberemos de cambiarlos para poder trabajar con esos ficheros. El comando será:

    sudo chown -R $USER:$USER .
