What is Django?
Free and open-course framework for building web apps with Python
Less time and less code for building websites.

Django Features: 
1. Admin site.
2. Object Relational Mapper.
3. Authentication.
4. Caching.

How Django works?

URL -> Uniform Resourse Location 
This can be a page, image, video or pdf

As soon as the request from client comes to the server it is taken up and a response is sent. This is carried out by the HTTP (Hypertext Transfer Protocol).
For each page being navigated each HTTP request is sent.

Two ways to send a response:
1. To completely send a HTML (HyperText Markup Language) page everytime a request is received.
2. To send only the data while the HTML page already loads on the client end.

What is the use? -> By doing this, the server has freed up space and can have more pages data to serve different types of requests.

Storefront location: /home/pranavisai/.local/share/virtualenvs/storefront-U_4UcZmF

pipfile -> It has the details of which version of python the project needs and what packages the application is dependent upon.
if * then it meaks on all the versions.

To activate the virtual environment we will use the python interpreter inside the virtual environment and not the one that is installed globally on the machine. Hence we use pipenv shell to open the environment.

django-admin is a utility that comes with django. We can see all commands we can use if we run it.

    'django.contrib.admin', - admin interface
    'django.contrib.auth', -  for authenticating user
    'django.contrib.contenttypes', - later
    'django.contrib.messages', - which is used for diplaying one time notifications
    django.contrib.sessions' - legacy, we dont use session  as apis remove this part, its a temporary memory used for user data
    'django.contrib.staticfiles', - serving static file like images, pdfs