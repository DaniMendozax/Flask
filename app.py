from flask import Flask 
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_UTI

app = Flask(__name__)

app.secret_key = "secret key" 
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_UTI
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = True
SQLAlchemy(app)


app.register_blueprint(contacts)





