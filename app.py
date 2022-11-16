from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('jets', user='tiramisu',
                        password='cake', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Jet(BaseModel):
    name = CharField()
    manufacturer = CharField()
    status = CharField()
    introduction = IntegerField()
    numberBuilt = IntegerField()


db.connect()
db.drop_tables([Jet])
db.create_tables([Jet])

Jet(name='F-22', manufacturer='Lockheed Martin Aeronautics',
    status='in service', introduction=2005, numberBuilt=195).save()
Jet(name='F-18', manufacturer='McDonnell Douglas',
    status='in service', introduction=1983, numberBuilt=1480).save()

app = Flask(__name__)


@app.route('/')
def index():
    return "Jets go zoom zoom"


@app.route('/jet/', methods=['GET', 'POST'])
@app.route('/jet/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Jet.get(Jet.id == id)))
        else:
            jet_list = []
            for jet in Jet.select():
                jet_list.append(model_to_dict(jet))
            return jsonify(jet_list)

    if request.method == 'PUT':
        body = request.get_json()
        Jet.update(body).where(Jet.id == id).execute()
        return "Jet " + str(id) + " has been updated."

    if request.method == 'POST':
        new_person = dict_to_model(Jet, request.get_json())
        new_person.save()
        return jsonify({"success": True})

    if request.method == 'DELETE':
        Jet.delete().where(Jet.id == id).execute()
        return "Jet " + str(id) + " deleted."


app.run(debug=True, port=9000)
