import json

from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
USER_DB = 'postgres'
PASS_DB = 'root'
URL_DB = 'localhost'
NAME_DB= 'CRUD-ITana'
DB_CONN= f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONN
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma= Marshmallow(app)

class DATA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(80))
    level_1= db.Column(db.String(80))
    level_2 = db.Column(db.String(80))
    value = db.Column(db.String(80))

    def __init__(self, year, level_1,level_2, value ):
        self.year = year
        self.level_1 = level_1
        self.level_2= level_2
        self.value= value

db.create_all()

class DATASchema(ma.Schema):
    class Meta:
        fields = ('id', 'level_1','level_2', 'value','year')

data_schema = DATASchema()
datas_schema = DATASchema(many=True)


@app.route('/', methods=['POST'])
def DataPost():
    year = request.json['year']
    level_1 =request.json['level_1']
    level_2 = request.json['level_2']
    value = request.json['value']
    new_data = DATA(year,level_1,level_2,value)
    db.session.add(new_data)
    db.session.commit()
    return data_schema.jsonify(new_data)
@app.route('/', methods=['GET'])
def DataGet():
    data = DATA.query.order_by(DATA.id).all()
    res = datas_schema.dump(data)
    return jsonify(res)
@app.route('/<id>', methods=['GET'])
def SingleGet(id):
    data = DATA.query.get(id)
    return data_schema.jsonify(data)

@app.route('/<id>', methods=['PUT'])
def DataPut(id):
    data = DATA.query.get(id)
    year = request.json['year']
    level_1 =request.json['level_1']
    level_2 = request.json['level_2']
    value = request.json['value']
    data.year = year
    data.level_1 = level_1
    data.level_2 = level_2
    data.value = value
    db.session.commit()

    return data_schema.jsonify(data)

@app.route('/<id>', methods=['DELETE'])
def DataDelete(id):
    data = DATA.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return data_schema.jsonify(data)
if __name__ == "__main__":
    app.run(debug=True)