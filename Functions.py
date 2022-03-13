import json


# Загрузка кандидатов
def load_candidates():
    file = open("candidates.json", encoding='UTF-8')
    candidates_list = json.load(file)
    file.close()
    return candidates_list
