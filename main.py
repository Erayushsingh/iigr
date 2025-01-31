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
    # Get 'name' query parameter
    names = request.args.getlist('name')  # Get all 'name' query parameters
    if names:
        # If 'name' is provided, return marks for the specified students
        marks = []
        for name in names:
            student = next((student for student in students_marks if student['name'] == name), None)
            marks.append(student['marks'] if student else None)
        return jsonify({"marks": marks})
    else:
        # If no 'name' is provided, return all student marks
        return jsonify({"students_marks": students_marks})

if __name__ == '__main__':
    app.run(debug=True, port=5002)
