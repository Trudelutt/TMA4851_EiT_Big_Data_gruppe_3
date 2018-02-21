# server.py
from flask import Flask, render_template
import json

app = Flask(__name__, static_folder="../frontend/dist", template_folder="../frontend/")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/testdata")
def testdata():
    return get_testdata()

def get_testdata():
  json_data= "{"name": "Rixos The Palm Dubai", "position": [25.1212, 55.1535]},{"name": "Shangri-La Hotel", "location": [25.2084, 55.2719]},{"name": "Grand Hyatt","location": [25.2285, 55.3273]}" 

if __name__ == "__main__":
    app.run()
