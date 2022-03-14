import functions10
from flask import Flask

if __name__ == "__main__":
    app = Flask(__name__)


    @app.route("/")
    def page_index():
        return functions10.make_candidate_list()


    @app.route("/candidate/<id>")
    def page_profile(id):
        return f"{functions10.show_candidate_id(id)}"


    @app.route("/skill/<x>")
    def page_profiles_by_skills(x):
        return f"{functions10.show_profiles_with_skills(x.lower())}"


    app.run()
