"""
Flask Application
"""

from dataclasses import asdict

from flask import Flask, jsonify, request
from models import Experience, Education, Skill


app = Flask(__name__)

data = {
    "experience": [
        Experience(
            1,
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
        data_experiences = data["experience"]
        data_experiences_response = [asdict(exp) for exp in data_experiences]
        return jsonify(data_experiences_response), 200

    if request.method == "POST":
        user_input = request.get_json()
        required_fields = [
            "title",
            "company",
            "start_date",
            "end_date",
            "description",
            "logo",
        ]
        # Validating User Input
        if not all(field in user_input for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        # Create a new Experience instance
        # Using the length of the of the experience list and the index of the new experience
        user_input["id"] = len(data["experience"]) + 1
        new_experience = Experience(**user_input)
        data["experience"].append(new_experience)
        return jsonify({"index": new_experience.id - 1}), 201

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


@app.route("/resume/skill", methods=["GET", "POST"])
def skill():
    """
    Handles Skill requests
    """
    if request.method == "GET":
        return jsonify({})

    if request.method == "POST":
        return jsonify({})

    return jsonify({})
