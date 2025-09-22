"""
Flask Application
"""

from dataclasses import asdict
from flask import Flask, jsonify, request

from models import Education, Experience, Skill

app = Flask(__name__)

data = {
    "experience": [
        Experience(
            "Software Developer",
            "A Cool Company",
            "October 2022",
            "Present",
            "Writing Python Code",
            "example-logo.png",
        )
    ],
    "education": [
        Education(
            "Computer Science",
            "University of Tech",
            "September 2019",
            "July 2022",
            "80%",
            "example-logo.png",
        )
    ],
    "skill": [Skill("Python", "1-2 Years", "example-logo.png")],
}


@app.route("/test")
def hello_world():
    """
    Returns a JSON test message
    """
    return jsonify({"message": "Hello, World!"})


@app.route("/resume/experience", methods=["GET", "POST"])
def experience():
    """
    Handle experience requests
    """
    if request.method == "GET":
        return jsonify()

    if request.method == "POST":
        return jsonify({})

    return jsonify({})


@app.route("/resume/experience/<int:pk>", methods=["GET"])
def get_single_experience(pk):
    """
    Retrieve a single experience based on the given id.
    """
    if request.method == "GET":
        experiences = data["experience"]
        try:
            return jsonify(asdict(experiences[pk])), 200
        except IndexError:
            return jsonify({"error": "No experience found with this index"}), 404
    return jsonify({})


@app.route("/resume/education", methods=["GET", "POST"])
def education():
    """
    Handles education requests
    """
    if request.method == "GET":
        return jsonify({})

    if request.method == "POST":
        return jsonify({})

    return jsonify({})


@app.route("/resume/education/<int:education_id>", methods=["GET"])
def get_education(education_id):
    '''
    Handles retrieving specific education 
    '''
    existing_education_records = data["education"]
    if education_id > len(existing_education_records) - 1  :
        return jsonify(
            {
                "message": "education does not exist",
            }
        ), 404

    record  = existing_education_records[education_id]
    return jsonify(
        {
            "message": "education record returned successfully",
            "data": record,
        }
    ), 200



@app.route("/resume/skill", methods=["POST"])
def skill():
        json_data = request.json
        try:
            name = json_data["name"]
            proficiency = json_data["proficiency"]
            logo = json_data["logo"]

            new_skill = Skill(name, proficiency, logo)

            data["skill"].append(new_skill)

            return jsonify(
                {"id": len(data["skill"]) - 1}
            ), 201

        except KeyError:
            return jsonify({"error": "Invalid request"}), 400

        except TypeError as e:
            return jsonify({"error": str(e)}), 400