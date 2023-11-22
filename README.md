# No_ShortCuts_Django

Build a functional API with Docker, Celery, Redis, Flower, Nginx, Nginx Proxy manager, Portainer and more...

Here are some of the concepts we will learn :

![image](https://github.com/izzypt/No-Shortcuts-to-Django-RESTful-APIs-with-Docker/assets/73948790/c954ee89-c3f5-42bb-9c1b-99a5872ab201)

### What I dive into on this project:

### Mailhog and Mailgun
- In development and testing purposes , I'am going to use mailhog, which is a web and API based SMTP testing tool (https://github.com/mailhog/MailHog)
- (Mailhog should not be used in production purposes, only development... on production we are going to use ***MailGun***, which is an email delivery service.)

### Docker
- For all our services in development and production , I'am going to be using ***Docker*** (To manage the containers on development environment we will use ***Docker Desktop*** and ***Portainer*** on production environment).

### Nginx
- In development and also in production , I'am going to be using Nginx as our web server and reverse proxy.
- In production we are going to be using an open source tool called Nginx proxy manager which will give us a nice GUI and help us to easily set up SSL certificates.

### Celery and Redis
- To make Django behave asyncronously we can use:
  - A package called ***django-channels*** .
  - Or , we can use ***celery*** in combination with ***Redis*** or ***RabbitMQ***.
