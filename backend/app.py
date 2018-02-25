from flask import Flask, render_template, jsonify, request
from json import dumps
from flask_cors import CORS
import retrieve_database_data as database_data

app = Flask(__name__, static_folder="../frontend/dist", template_folder="../frontend")
CORS(app)

@app.route("/testdata")
def testdata():
    return jsonify(get_testdata())

@app.route("/trades/<country1>/<country2>")
def tradeData(country1, country2):
    #return database_data.

def get_testdata():
    return {'name': 'Rixos The Palm Dubai', 'position': [25.1212, 55.1535]}

if __name__ == "__main__":
    app.run()
