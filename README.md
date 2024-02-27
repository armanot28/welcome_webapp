Welcome to the Web Application Docker Setup

This repository contains a web application built with Flask that serves HTML pages and data fetched from a PostgreSQL database. The application is containerized using Docker to ensure easy deployment and portability.

Requirements
Before running the web application, make sure you have the following packages installed:

Docker: Installation Guide https://docs.docker.com/engine/install/
Docker Compose: Installation Guide https://docs.docker.com/compose/install/

Steps to Run
1. Clone the Repository:
git clone git@github.com:armanot28/welcome_webapp.git
cd welcome_webapp
2. Build Docker Containers:
docker-compose build
3. Start Docker Containers:
docker-compose up
This command will start the Docker containers defined in the docker-compose.yml file.
4. Access the Web Application:
Once the containers are up and running, you can access the web application in your browser:
* Open http://localhost to access the main page.
* Open http://localhost/api to access the API page.

Testing
To test the web application, you can perform the following steps:
1. Verify that the containers are running:
docker ps
2. Check the logs to ensure there are no errors:
docker-compose logs
3. Access the main page and API page in your browser to ensure they load correctly.

Additional Notes
* The web application serves HTML pages located in the templates directory.
* PostgreSQL is used as the database backend. Ensure that the PostgreSQL container (db) is running and configured correctly.
* Nginx is used as a reverse proxy server to serve the web application on ports 80 and 443.
