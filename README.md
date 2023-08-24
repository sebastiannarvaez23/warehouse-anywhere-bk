# warehouse-anywhere-bk
Application that manages and controls the dispatches of a company's finished product (WMS - Warehouse Management System), this project focuses more on interactivity on the Backend side.

## Instalación
#### Entorno virtual y dependencias
1. Lo primero que deberás hacer es crear un entorno virtual de python que te encapsule las dependencias del proyecto, ejecuta `$ python -m venv venv`, hay otras personas utilizan `$ python3 -m venv venv`, revisa cual te funciona a ti.
2. Activa el entorno virtual con el comando:
  Linux o mac: `$ source venv/bin/activate`
  Windows: `$ venv/Scripts/activate`
3. Instala las dependencias del proyecto las cuales se encuentran el archivo `requiriments.txt`. Ubicate en el proyecto al nivel del archivo mencionado y ejecuta el comando `$ pip install -r requiriments.txt`, cabe aclarar que debes asegurarte de tener el entorno virtual activado, en la mayoria de las terminales va a aparecerte (venv) sobre la linea de comando en la que estés ubicado.

De esta forma tendras las dependencias correctamente instaladas en el entorno que creaste.

## Configuración
1. Inicialmente deberás crear una base de datos denominada `events` en tu servidor de base de datos Postgresql.
2. Ubica las variables de entorno que te compartí por el correo electronico, esto añade una capa de seguridad a la aplicación. Para ello deberas descargar el archivo `.env` del correo electronico y ubicarlo al nivel de la carpeta settings. Abre el archivo y edita las variables segun las credenciales de acceso, como el dominio/ip y/o puerto al que apunta tu SBD.
3. En la terminal anterior en la que gestionamos el entorno y las dependencias, dirigite al nivel del archivo `manage.py`.
4. Luego de tener la base de datos creada, deberás crear y ejecutar las migraciones. Ejecuta el comando `$ python manage.py makemigrations` este comando te creará las migraciones. Posteriormente ejecuta el comando `$ python manage.py migrate` esto hará que los modelos de datos migren a la base que creaste en el punto 1. 
5. Por ultimo deberas ejecutar el comando `$ python manage.py runserver`.
