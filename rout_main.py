from Functions import load_candidates
from flask import Flask

if __name__ == "__main__":
    # Загрузка запроса
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

    app = Flask(__name__)


    @app.route("/")
    def page_index():
        return f"<pre>{candidates_string}<pre>"


    app.run()
