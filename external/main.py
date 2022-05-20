from flask import Flask,render_template
import requests

INTERNAL_URL = "http://localhost:81"

app = Flask(__name__)

@app.route("/")
def default():
    return "this is external"

@app.route("/internal")
def get_internal():
    res = requests.get(INTERNAL_URL)
    return "response : " + res.text 

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=80)