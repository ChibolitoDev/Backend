from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

USER_DB = 'postgres'
PASS_DB = 'root'
URL_DB = 'localhost'
NAME_DB= 'CRUD-ITana'
DB_CONN= f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONN
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

migrate = Migrate()
migrate.init_app(app, db)

class DATA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(250))
    level_1= db.Column(db.String(250))
    level_2 = db.Column(db.String(250))
    value = db.Column(db.String(250))

    def __str__(self):
        return(
            f'Id: {self.id},'
            f'Year: {self.year},'
            f'Level_1: {self.level_1},'
            f'Level_2: {self.level_2},'
            f'Value: {self.value},'
        )