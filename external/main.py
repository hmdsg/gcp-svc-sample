from flask import Flask,render_template
import requests
import os

def get_internal_url():
    return os.getenv('INTERNAL_URL', 'http://localhost')

app = Flask(__name__)

@app.route("/")
def default():
    return "this is external"

@app.route("/internal")
def get_internal():
    internal_url = get_internal_url()
    res = requests.get(internal_url)
    return "response : " + res.text 

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=80)