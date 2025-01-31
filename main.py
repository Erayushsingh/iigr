from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load student marks from the JSON file
with open('q-vercel-python.json', 'r') as file:
    students_marks = json.load(file)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')  # Get all 'name' query parameters
    marks = []

    # Loop through the names and find matching students in the list
    for name in names:
        # Search for the student by name in the list
        student = next((student for student in students_marks if student['name'] == name), None)
        marks.append(student['marks'] if student else None)

    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True,port=5001)