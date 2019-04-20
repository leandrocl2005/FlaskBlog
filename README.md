# Flask simple Blog

Flask simple Blog is a project for the program of Nanodegree in Web Full-Stack Developer. Google Oauth, CRUD and Json endpoints are the requirements for this project.

# How to execute this project:

  - This project is a 3.7.2 Python project. So, you need install Python 3.7.2
  - Make download or clone this repository
  - Enter on *FlaskBlog* folder
  - Install the requirements
  - Replace the client_id and secret_id in init file. You will need get this credentials in Google Oauth.

Type the following commands in a windows terminal:

```sh
$ set FLASK_APP=agroblog.py
$ flask db init
$ flask db migrate -m 'first commit'
$ flask db upgrade
$ python filldatabase.py
$ flask run
```
  - Enter in localhost:5000 from your web navigator.

### Some important informations:

  - To create, delete and update a post, make login with you Google acount. The login link is in hamburguer menu. 
  - If you have logged, your hamburguer menu will show your posts link. Enter this link and you'll be able to create, delete and update a post.
  - You can acess a json from a post in following url: (localhost:5000/post/<int:post_id>/getJson)
  - Above, replace <int:post_id> by the post id required. 

# Credits

  - the HTML/CSS template was provided by Colorlib (https://colorlib.com/)
  - the images was provided by Pixabay (https://pixabay.com/pt/)
