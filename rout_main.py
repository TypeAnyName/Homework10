import functions10
from flask import Flask

app = Flask(__name__)


@app.route("/")
def page_index():

    return functions10.make_candidate_list()


app.run()
