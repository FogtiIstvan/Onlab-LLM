from flask import Flask, request, jsonify
import json
import numpy as np
app = Flask(__name__)
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("/app/model")
score = 0

@app.route('/', methods=['POST'])
def rootfunction():
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
    answer_chunks = split_into_clauses(answer)
    answer_chunks.append(answer)
    answer_embeddings = model.encode(answer_chunks, convert_to_tensor=True)
    missing_information = []

    for criteria in criterias:
        contains = False
        criteria_clauses = split_into_clauses(criteria[1])
        cosine_scores = util.cos_sim(criteria_embedding, answer_embeddings)

        numofclauses = len(criteria_clauses)
        NumOfCorrectClauses = 0   
        for crit_clause in criteria_clauses:
            criteria_embedding = model.encode(crit_clause, convert_to_tensor=True)
            euclidean_dist_arr = []

            for ans in answer_embeddings:
                crit_arr = criteria_embedding.cpu().numpy()
                answ_arr = ans.cpu().numpy()
                dist = answ_arr - crit_arr
                euclidean_dist_arr.append(np.linalg.norm(dist))

            for cos in cosine_scores:
                for c in cos:
                    if c > 0.79:
                        for dist in euclidean_dist_arr:
                            if dist < 0.51:
                                NumOfCorrectClauses += 1
                                break
        
        if numofclauses == NumOfCorrectClauses:
            score += int(criteria[0])
        else:
            missing_information.append(str(criteria[1]))

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

