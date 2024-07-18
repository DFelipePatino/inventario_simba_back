Requisitos Previos

Python: Asegurarse de tener Python instalado en el sistema.
pip: Administrador de paquetes de Python.
Django: Framework de desarrollo web para Python.
PostgreSQL: Base de datos.

Clona el repositorio:
git clone https://github.com/DFelipePatino/inventario_simba_back.git


Al iniciar con el proyecto

Crea un entorno virtual:
python -m venv venv

Activa el entorno virtual:
.\venv\Scripts\activate

Instala las dependencias:
pip install -r requirements.txt

Configura las variables de entorno:
Crea un archivo .env en la raíz del proyecto y agrega las variables necesarias (ejemplo para base de datos PostgreSQL):SECRET_KEY=tu_secreto
SECRET_KEY=tu_secreto
DEBUG=True
DATABASE_URL=postgres://usuario:contraseña@localhost:5432/nombre_de_la_base_de_datos

Realiza las migraciones y crea el superusuario:
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

Ejecuta el servidor de desarrollo:
python manage.py runserver
