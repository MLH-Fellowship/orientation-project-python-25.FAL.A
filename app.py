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
        
@app.route('/resume/skill/<int:skill_id>', methods=['GET'])
def get_skill(skill_id):
    try:
        skill = data["skill"][skill_id]
        return jsonify(skill.__dict__)
    except IndexError:
        return jsonify({"error": "Skill not found"}), 404
    except TypeError as e:
        return jsonify({"error": str(e)}), 400
