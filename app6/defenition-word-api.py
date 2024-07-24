from flask import Flask, render_template

definition_app = Flask(__name__)


@definition_app.route("/")
def home_page():
    return render_template("defenition-word.html")


@definition_app.route("/api/ver1/<word>")
def word_api(word):
    value = word.upper()
    return {
        "Definition": value,
        "Word": word
    }


definition_app.run(debug=True, port=5001)
