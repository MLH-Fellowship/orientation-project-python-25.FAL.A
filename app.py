'''
Flask Application
'''
from flask import Flask, jsonify, request

from models import Education, Experience, Skill

app = Flask(__name__)

data = {
    "experience": [
        Experience("Software Developer",
                   "A Cool Company",
                   "October 2022",
                   "Present",
                   "Writing Python Code",
                   "example-logo.png")
    ],
    "education": [
        Education("Computer Science",
                  "University of Tech",
                  "September 2019",
                  "July 2022",
                  "80%",
                  "example-logo.png")
    ],
    "skill": [
        Skill("Python",
              "1-2 Years",
              "example-logo.png")
    ]
}


@app.route('/test')
def hello_world():
    '''
    Returns a JSON test message
    '''
    return jsonify({"message": "Hello, World!"})


@app.route('/resume/experience', methods=['GET', 'POST'])
def experience():
    '''
    Handle experience requests
    '''
    if request.method == 'GET':
        return jsonify()

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

@app.route('/resume/education', methods=['GET', 'POST'])
def education():
    '''
    Handles education requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == "POST":
        body = request.get_json()
        payload = {
            "course": body.get("course"),
            "school": body.get("school"),
            "start_date": body.get("start_date"),
            "end_date": body.get("end_date"),
            "grade": body.get("grade"),
            "logo": body.get("logo"),
        }

        for key, value in payload.items():
            if value is None:
                message = f"{key} must not be empty"
                return jsonify(
                    {
                        "message": message,
                    }
                ), 400

        new_record = Education(
            payload[ "course" ],
            payload["school"],
            payload["start_date"],
            payload["end_date"],
            payload["grade"],
            payload["logo"],
        )

        existing_education_records = data["education"]
        length_of_exisiting_records = len(existing_education_records)
        existing_education_records.append(new_record)

        return jsonify(
            {
                "message": "education added successfully",
                "data": length_of_exisiting_records,
            }
        ),201

    return jsonify({})


@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})
