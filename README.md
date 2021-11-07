# DJANGO BASIC PROJECT

El siguiente proyecto se puede utilizar como plantilla base para crear cualquier proyecto con el _framework_ de *Django*.

## Configuración básica

Para utilizar este proyecto debemos de seguir los siguientes pasos.

### 1. Descargar el proyecto desde este mismo repositorio

    git clone git@github.com:ServerJon/django-basic.git

O también puedes crear uno nuevo con la opción de `Usa esta plantilla`

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

### 3. Crear un fichero secret.json

En la raíz de nuestro proyecto debemos crear un fichero _secret.json_ y crear las variables de entorno para nuestro proyecto:

    {
        "FILENAME": "secret.json",
        "SECRET_KEY": "django-insecure-05)jvx573+7yi3(c8_8zlpu^!=wf=4c=_kk3c+lh!6j@yv^43b",
        "DB_NAME": "basicdb",
        "USER_DB": "ServerJon",
        "PWD_DB": "serverjon"
    }

Se recomienda modificar el SECRET_KEY para mayor seguridad.

### 3. Levantar el entorno de trabajo

El proyecto está configurado para trabajar con los contenedores de Docker:

    docker-compose up

Una vez levantado el entorno podríamos trabajar dentro del mismo contenedor con toda la configuración instalada como por ejemplo con PyCharm o VSCode.

Si por el contrario queremos trabajar desde un entorno en local se recomienda utilizar un entorno virtual para poder trabajar. Se recomienda seguir los siguientes pasos:

- Comprobar que se tiene instalado python en una de sus últimas versiones, el proyecto trabaja con python3.
- Se recomienda utilizar un gestor de versiones de python como por ejemplo [pyenv](https://github.com/pyenv/pyenv).
- Crear un entorno virtual de trabajo e instalar con pip los modulos del fichero _requirements.txt_.
- En caso de usar un entorno virtual solamente será necesario levantar el docker de la base de datos de mysql.
- Si en la instalación nos da un error el modulo de mysqlclient debemos instalar una serie de paquetes. En el siguiente tenemnos las diferentes opciones para Ubuntu, Mac o Windows: [pip install mysqlclient error](https://stackoverflow.com/questions/35190465/virtualenvpython3-4-pip-install-mysqlclient-error)

### 4. Realizar las migraciones minimas

Como primer comando a ejecutar una vez levantado todo el entorno de trabajo será crear la base de datos a trabajar. Para ello se ejecutarán el siguiente comando:

    python manage.py migrate

### 5. Crear un usuario super admin

Una vez tengamos el entorno de trabajo levantado y el servidor en marcha debemos crear un usuario super admin para poder acceder a la zona de administración de django. Para ello ejecutaremos el siguiente comando y rellenaremos los campos que nos pidan:

    python manage.py createsuperuser

Si estamos trabajando con Docker debemos ejecutar el comando a través del contenedor _web_.

### 6. Configuración pre-commit

Para poder trabajar de forma optima con nuestro proyecto se utilizarán los módulos de pre-commit y black. Para utilizarlos tan solo es necesario instalar el fichero de _requirements-dev.txt_. Una vez instalados todos los paquetes necesarios ejecutaremos el siguiente comando y estará todo listo:

    pre-commit install

Si no quisieramos que verificara nuestro código podremos añadir al comando de _git commit_ el argumento de _--no-verify_:

    git commit -m"mensaje" --no-verify

## Configuración a tener en cuenta

1. Cuando se crea una nueva aplicación desde el docker de django se crearán los permisos como usuario root por lo que deberemos de cambiarlos para poder trabajar con esos ficheros. El comando será:

    `sudo chown -R $USER:$USER .`

2. Eliminar repositorio para enlazar con el que queramos:

    `git remote remove origin`

    `git remote add origin your_git_project`

3. Se recomienda utilizar _[Docker secrets](https://docs.docker.com/engine/swarm/secrets/)_ para guardar información sensible como los datos de la base de datos del fichero docker-compose.
