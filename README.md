# Overview

This is a web application made with Django using Visual Studio Code. The website was created as a place for me to share all of my projects and thoughts about them. As such, the project has a page for my portfolio and a page for my thoughts in the form of a blog. 

I have always wanted to create a space to display my personal projects. I have also always wanted an opportunity at creating a website that handles back end server requests. 

This was also an opportunity for me to learn Django. After having used it for this project, I plan on creating more projects to hone my skills with this powerful tool. You can run the test server by typing "py manage.py runserver" in your terminal. The link to the website you need to go to is http://localhost:8000/projects/.

[Software Demo Video](https://youtu.be/zxGCrqi_Obw)

# Web Pages

This web app has 5 html pages. They are the Portfolio page, the Detailed Project Page, the Blog Post Page, the detailed Blog Post page, and the Blog Post by Category page. The first page is the Portfolio page that shows all of my projects as a card view. The cards are all placed on the page with a for loop with data pulled from the database. The Detailed project page can be reached by clicking Read More on any of the projects. There is a navigation Bar that takes you to the Blog Page. From the Blog Page you can select a specific blog post that will take you to a detailed view of the Blog Post. You can also see Categories listed by the Blog Posts. You can select a category and it will take you to a page with blog posts only in that category.

# Development Environment

This project was created in a Virtual Environment using Visual Studio Code. 

The programming language used was Python. I used Django and Pillow to create the website.

# Useful Websites

* [Django Tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-django)
* [Django File and Image Upload Tutorial](https://learndjango.com/tutorials/django-file-and-image-uploads-tutorial)

# Future Work

* Add a short description to the Projects Model for displaying on view of all projects
* Add the rest of my personal projects to the Database
* Embedded Youtube videos on the detailed Project Page