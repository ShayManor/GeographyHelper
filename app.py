from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


import random

# Dictionary of US states and their capitals
states_capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

@app.route("/api/get_question", methods=["GET"])
def get_question():
    state = random.choice(list(states_capitals.keys()))
    return {"state": state}

@app.route("/api/check_answer", methods=["POST"])
def check_answer():
    data = request.json
    state = data.get('state')
    capital = data.get('capital')
    correct_capital = states_capitals.get(state)
    if correct_capital is None:
        return {"error": "Invalid state provided."}, 400
    is_correct = (capital.strip().lower() == correct_capital.lower())
    return {
        "is_correct": is_correct,
        "correct_capital": correct_capital
    }

@app.route("/api/get_all_states", methods=["GET"])
def get_all_states():
    return {"states": list(states_capitals.keys())}

@app.route("/api/get_capital", methods=["GET"])
def get_capital():
    state = request.args.get('state')
    if not state:
        return {"error": "State parameter is required."}, 400
    capital = states_capitals.get(state)
    if not capital:
        return {"error": "Invalid state provided."}, 400
    return {"capital": capital}


@app.route("/", methods=["GET"])
def index():
    return send_from_directory(".", "templates/index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
