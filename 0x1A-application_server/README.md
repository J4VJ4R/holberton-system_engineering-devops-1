# Application server
Your web infrastructure is already serving web pages via Nginx that you
installed in your first web stack project. While a web server can also serve
dynamic content, this task is usually given to an application server. In this
project you will add this piece to your infrastructure, plug it to your Nginx
and make is serve your Airbnb clone project.

## Topics
- Application server vs web server
- How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04
  (As mentioned in the video, do not install Gunicorn using virtualenv, just
  install everything globally)
- Running Gunicorn
- Be careful with the way Flask manages slash in route - strict_slashes
- Upstart documentation

## Context
![app_server.hpg](assets/app_server.jpg)
  
## Requirementes
- Linux Ubuntu 16.04 LTS
- Nginx
- Python3
- Flask
- Gunicorn

## Challenges

### 0. Set up development with Python

### 1. Set up production with Gunicorn

### 2. Serve a page with Nginx

### 3. Add a route with query parameters

### 4. Let's do this for your API

### 5. Serve your AirBnB clone

## Author
Gonzalo Gomez Millan | :octocat: [GutHub](https://github.com/gogomillan)
