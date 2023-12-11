from flask import Flask, request, jsonify
import json
import numpy as np
app = Flask(__name__)

from model import Model
model = Model()

i = 0

@app.route('/', methods=['POST'])
def hello_world():
    global i
    log = str(i) + ". request received"
    print(log)
    i += 1

    #preprocess data into array of criterias
    data = request.get_json()
    data = format_input(data)

    return jsonify(data)


def format_input(data):

    #print(data['criteria'])
    criterias = data['criteria'].replace("&nbsp;", " ").split(";")
    criterias = [criteria for criteria in criterias if criteria]
    criterias = [criteria.split('-') for criteria in criterias]

    for i in range(len(criterias)):
        criterias[i] = [criteria for criteria in criterias[i] if criteria]

    json_str = json.dumps(criterias)

    return criterias
