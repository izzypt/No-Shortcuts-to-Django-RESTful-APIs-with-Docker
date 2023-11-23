# No_ShortCuts_Django

### What we are going to build

We are going to make a clone of medium (https://medium.com/flutter/whats-new-in-flutter-3-16-dba6cb1015d1), but just the API (exclude frontend/UI stuff).

Auth related functionality like :
- register
- login
- logout
- password
- reset
- verify user
- get acess
- refresh tokens

Article functionality:

- Search using elasticsearch
- Followers
- Article Date and read time
- Likes
- Responses

### Some of the concepts touched upon on this repo :

![image](https://github.com/izzypt/No-Shortcuts-to-Django-RESTful-APIs-with-Docker/assets/73948790/c954ee89-c3f5-42bb-9c1b-99a5872ab201)

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

### JWT
 - For authentication we are going to use ***JWT***(JSON web tokens)

### pytest
- For testing, a library that help us write test for Django, Flask, Fast API....

### Project setup steps

- Create a working dir and virtual env
- Install packages
- Django settings
- Django apps

### Logging in Django

Key components are:

- Log levels
  - **Describes the severity of the mesage**:
    - Error -> Major Problem occured
    - Warning -> Minor Problem occured
    - Info -> General system information
    - Debug -> Low level system information
    - Critical - Critical Problem
- Handlers
  - **Responsible for dispatching log message to the appropriate destination**:
    - Console
    - Files
    - e-Mail
- Formatters
  - Define the format of the log.
  - Logs are in a log record format and need to be converted before being sent.
- Filters
  - **Filter log messages based on some criteria**:
    - log levels for example
