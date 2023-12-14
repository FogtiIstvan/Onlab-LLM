import json
import numpy as np

score = 0

def delete_html_tags(text):
    text = text.replace("&nbsp;", " ").replace("\r\n", " ").replace("\n", " ")
    return str(text)


""" def evaluate(criterias, answer):
    global score
    answer_chunks = split_into_clauses(answer)
    answer_chunks.append(answer)
    answer_embedding = model.encode(answer_chunks, convert_to_tensor=True)
    missing_information = []

    for criteria in criterias:
        contains = False
        criteria_clauses = split_into_clauses(criteria[1])
        criteria_embedding = model.encode(criteria[1], convert_to_tensor=True)
        cosine_scores = util.cos_sim(criteria_embedding, answer_embedding)

        for crit_clause in criteria_clauses:
            criteria_embedding = model.encode(crit_clause, convert_to_tensor=True)

        for cos in cosine_scores:
            for c in cos:
                if c > 0.79:
                    contains = True
                    if score == -1:
                        score = 0
        
        if contains:
            score += int(criteria[0])
        else:
            missing_information.append(str(criteria[1]))

        return [score, missing_information] """


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



str1 = "The king of France is bald, and gay."
str2 = split_into_clauses(str1)
print(str2)