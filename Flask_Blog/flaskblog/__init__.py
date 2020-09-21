# Initialization file for flaskblog package, creating both app and database instances

from flask import Flask                    # Import the Flask class from flask package
from flask_sqlalchemy import SQLAlchemy    # Import database class from package
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)    # app variable is an instance of Flask(__name__)
                         # __name__ here is __main

app.config['SECRET_KEY'] = '51b9346f33bfa5a84da6367982937319'
# Set up a secret key for authentication of form submissions

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Give our database URI an address

db = SQLAlchemy(app)
# Set up database db, based off our app instance
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
