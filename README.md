# REGISTRO USUARIOS PRUEBA

## Como ejecutar el proyecto:

### Frontend

1. `cd frontend` entramos en la carpeta frontend
2. `npm install` instalamos las dependencias (librerias)
3. `npm run dev` ejecutamos la aplicacion

### Backend

1. `cd backend` entramos en la carpeta backend
2. `pipenv shell` entramos en el entorno virtual (si no existe,se crea automaticamente)
3. `pipenv install` para instalar las dependencias
4. `flask db init` iniciar la base de datos
5. `flask db migrate` para detectar cambios en la base de datos
6. `flask db upgrade` aplicar los cambios en la base de datos
7. `pipenv run dev` ejecutar la aplicacion


## Tecnologias usadas:

### Frontend:
- ReactJS
- ReactRouter
- Css3
- Bootstrap
- SweetAlert2
- JavaScript

### Backend:
- Python
- Flask
- Flask Migrations
- Flask Cors
- SqLite
- SqlAlchemy
- Werkzeug
