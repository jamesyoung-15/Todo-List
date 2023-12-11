# To-Do List with Django
![](./src/screenshot.png)

Created a To-Do List Application with Django. Users can create an account to create, read, update, and delete different tasks. Purpose is for learning basics of Django framework and hosting an application on a VPS. Link to demo of project [here](https://todo.jamesyy.info/).

## Application Tech Stack
- Front-end: HTML/CSS
- Back-end: Postgresql
- Framework: Django
- Others: AWS EC2 (Ubuntu VPS), Docker, Letsencrypt (SSL certs), Nginx-proxy (proxy manager)
## Application Hosting Structure

The Django application is Dockerized with Gunicorn (to connect Django to Nginx), nginx-proxy (for reverse proxy), and Postgres (for database) with a structure similar to the diagram below. This container is deployed on an EC2 instance on AWS with a domain pointing to that instance. The container also includes Letsencrypt (using nginx-proxy-letsencrypt) for SSL certificates for HTTPS. Postgres database inside container rather than using AWS RDS as it is just a simple application.

![](./src/project-structure.jpg)

## Local Hosting Instructions
For testing on local development, clone this repo, use docker-compose build and up commands with the normal docker-compose.yml file (not staging or production). There is no need to change any .env configurations on local development.

## VPS Hosting
Refer to the guide below. I used an AWS EC2 Ubuntu server instance but any VPS can do (like Oracle free tier). Make sure to use a real domain and register an A-record to point the domain to the VPS IP address. Then Nginx handles the request to serve the web application. Must define .env production files as written in the docker-compose.production.yml file. To run this on the VPS, make sure to run `commands.sh` (or `commands-legacy.sh` for older docker compose) to generate static files otherwise Nginx won't be able to find the static files.

## Resources
[Docker+Django Guide](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#static-files)