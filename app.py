from flask import Flask, jsonify
from data_dict_simple import students
from data_dict import random_users
from students import create, read_all

app = Flask(__name__)

create()

@app.route('/')
def index():
    return jsonify({'name':'Claus'})

@app.route('/api/students', methods=['GET'])
def read():
    return jsonify(read_all())

@app.route('/api/students', methods=['POST'])
def create():
    #random_users.append({'id':3, 'name': 'Pia'})
    return jsonify(None)

app.run()