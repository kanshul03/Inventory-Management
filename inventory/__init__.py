from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DB_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from inventory import routes

db.create_all()
db.session.commit()
