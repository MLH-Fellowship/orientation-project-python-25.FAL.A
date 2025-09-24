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

    if request.method == 'GET':
        existing_education_records = data["education"]
        return jsonify(
            {
                "message": "list of education records returned successfully",
                "data": existing_education_records,
            }
        ), 200


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
        
@app.route('/resume/skill/<int:skill_id>', methods=['GET'])
def get_skill(skill_id):
    try:
        skill = data["skill"][skill_id]
        return jsonify(skill.__dict__)
    except IndexError:
        return jsonify({"error": "Skill not found"}), 404
    except TypeError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/resume/skill/<int:skill_id>', methods=['DELETE'])
def delete_skill(skill_id):
    try:
        if skill_id is None or skill_id < 0 or skill_id >= len(data["skill"]):
            return jsonify({"message": "Skill doesn't exist"}), 404
        else:   
            del data['skill'][skill_id]
            return jsonify({"message": "Skill Successfully Deleted"}), 200

    except Exception as e:      
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

