'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill

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
        input = request.get_json()
        payload = {
            "course": input.get("course"),
            "school": input.get("school"),
            "start_date": input.get("start_date"),
            "end_date": input.get("end_date"),
            "grade": input.get("grade"),
            "logo": input.get("logo"),
        }

        for key in payload.keys():
            if payload[key] == None:
                message = f"{key} must not be empty"
                return jsonify(
                    {
                        "message": message,
                    }
                )

        newRecord = Education(
            payload[ "course" ],
            payload["school"],
            payload["start_date"],
            payload["end_date"],
            payload["grade"],
            payload["logo"],
        )

        existingEducationRecords = data["education"]
        lengthOfExisitingRecords = len(existingEducationRecords)
        existingEducationRecords.append(newRecord)

        return jsonify(
            {
                "message": "education added successfully",
                "data": lengthOfExisitingRecords,
            }
        )

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
