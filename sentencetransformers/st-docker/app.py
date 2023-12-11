from flask import Flask, request, jsonify
import json
import numpy as np
app = Flask(__name__)
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("/app/model")
score = 0

@app.route('/', methods=['POST'])
def hello_world():
    global model
    global score

    #preprocess data into array of criterias
    print("proecsss data")
    data = request.get_json()

    if len(data["criteria"]) == 0:
        return jsonify([0, "No sufficient graderinfo provided."])

    criterias = format_criterias(data)
    answer = delete_html_tags(data['answer'])
    print("answer: " + answer)

    print("evaluate")
    assessment = evaluate(criterias, answer)

    comment = ""
    if len(assessment[1]) > 0:
        comment += create_comment(assessment[1])   

    msg = "Model not loaded"
    if model is not None:
        msg = "Model loaded successfully"

    score = 0
    return jsonify([assessment[0], comment])


def format_criterias(data):

    print("in format_input")
    criterias = delete_html_tags(data['criteria']).split(";")
    criterias = [str(criteria) for criteria in criterias if criteria]
    criterias = [str(criteria) for criteria in criterias if criteria != ' ']
    criterias = [criteria.split(' - ') for criteria in criterias]

    for i in range(len(criterias)):
        criterias[i] = [criteria for criteria in criterias[i] if criteria]

    json_str = json.dumps(criterias)
    #print("json_str===============================================")
    #print(json_str)

    return criterias

def delete_html_tags(text):
    text = text.replace("&nbsp;", " ").replace("\r\n", " ").replace("\n", " ")
    return str(text)


def evaluate(criterias, answer):
    global score
    print("in evaluate")
    answer_chunks = split_into_clauses(answer)
    answer_chunks.append(answer)
    answer_embedding = model.encode(answer_chunks, convert_to_tensor=True)

    missing_information = []

    print(criterias)
    for criteria in criterias:
        contains = False
        print("========================================================")
        print("=====================comparison=========================")
        print("possible points: " + str(criteria[0]))
        #criteria_chunks = split_into_sentences(criteria[1])
        print("criteria_chunks: " + str(criteria[1]))
        print("answer_chunks: " + str(answer_chunks))
        criteria_embedding = model.encode(criteria[1], convert_to_tensor=True)

        cosine_scores = util.cos_sim(criteria_embedding, answer_embedding)
        print("cosine_scores: " + str(cosine_scores))

        for cos in cosine_scores:
            for c in cos:
                if c > 0.79:
                    contains = True
                    if score == -1:
                        score = 0
        
        if contains:
            print("contains")
            score += int(criteria[0])
            print("score: " + str(score))
        else:
            missing_information.append(str(criteria[1]))

    
    print("answer score: " + str(score))
    return [score, missing_information]


def split_into_sentences(text):
    sentences = text.split('.')
    filtered_list = [string for string in sentences if string]
    return filtered_list

def split_into_clauses(text):
    sentences = text.split('.')
    sentences = [string for string in sentences if string]
    strings = [s.split(',') for s in sentences]
    filtered_list = [e for e in strings if len(e) != 1 and e[0] != '']

    list = []
    for e in strings:
      for i in e:
        list.append(i)

    return list

def create_comment(missing_content):

    comment = "The following informations are fully, or partially missing"

    for point in missing_content:
        newpoint = " - " + str(point)
        newpoint = newpoint + ";"
        comment += newpoint

    return comment