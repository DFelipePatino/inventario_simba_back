Live Demo Front: https://inventario-simba-front.onrender.com/

Live Demo Back: https://inventario-simba-back.onrender.com/inventario/productos/

BackEnd: https://github.com/DFelipePatino/inventario_simba_back.git


Prerequisites

Python: Make sure Python is installed on the system.
pip: Python package manager.
Django: Web development framework for Python.
PostgreSQL: Database.

Clone the repository:

git clone https://github.com/DFelipePatino/inventario_simba_back.git

Starting the project

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

.\venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Set up environment variables:
Create a .env file in the root of the project and add the necessary variables

Run migrations and create the superuser:

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

Run the development server:

python manage.py runserver



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
Crea un archivo .env en la raíz del proyecto y agrega las variables necesarias 

Realiza las migraciones y crea el superusuario:

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

Ejecuta el servidor de desarrollo:
python manage.py runserver

