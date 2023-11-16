Hola, soy Giuliano Herrera estudiantes de la carrera Desarrollo de Software, en esta oportunidad estoy realizando un trabajo practico para la materia de Practica Profesionalizante 1 de DevOps. Este blog contiene modelos de base de datos, schemas y vistas.

Requesitos previos:
Tener Instalados Docker y Docker-compose

Instrucciones para su uso:

1.Clona el repositorio

https://github.com/giulianoh/gestion_empleados.git

2.Crea tu archivo ".env"

3.Ejecuta la aplicacion con Docker Compose, esto creará contenedores para la aplicacion Flask y una Base de datos MySQL:

sudo docker-compose up -d

4. Una vez echo lo anterior, te dirigis al localhost.

5.con los siguientes comando podes ver:
sudo docker-compose ps (este comando muestra que contenedor esta en ejecucion)
sudo docker-compose down ( este comando lo detiene y elimina los contenedores)
