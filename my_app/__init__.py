from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "MySecretKey###321"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/schema'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

import my_app.employee_management.views
