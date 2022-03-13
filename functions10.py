import json


# Загрузка кандидатов
def load_candidates():
    file = open("candidates.json", encoding='UTF-8')
    candidates_list = json.load(file)
    file.close()
    return candidates_list


# Создание полного списка кандидатов
def make_candidate_list():
    candidates_func = load_candidates()
    candidates_string = ""

    for candidate in candidates_func:
        candidates_str = f"id: {candidate['id']}\n" \
                         f"name: {candidate['name']}\n" \
                         f"picture: {candidate['picture']}\n" \
                         f"position: {candidate['position']}\n" \
                         f"gender: {candidate['gender']}\n" \
                         f"age: {candidate['age']}\n" \
                         f"skills: {candidate['skills']}\n\n"

        candidates_string += candidates_str

    return f"<pre>{candidates_string}<pre>"
