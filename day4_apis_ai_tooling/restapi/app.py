from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample database
students = [
    {"id": 1, "name": "Tarun", "course": "Python"},
    {"id": 2, "name": "Rahul", "course": "Django"}
]

# GET API
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# POST API
@app.route('/students', methods=['POST'])
def add_student():
    data = request.json

    new_student = {
        "id": len(students) + 1,
        "name": data["name"],
        "course": data["course"]
    }

    students.append(new_student)

    return jsonify({
        "message": "Student added successfully",
        "student": new_student
    })

# PATCH API
@app.route('/students/<int:id>', methods=['PATCH'])
def update_student(id):

    data = request.json

    for student in students:
        if student["id"] == id:

            if "name" in data:
                student["name"] = data["name"]

            if "course" in data:
                student["course"] = data["course"]

            return jsonify({
                "message": "Student updated",
                "student": student
            })

    return jsonify({"error": "Student not found"}), 404

# DELETE API
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):

    for student in students:
        if student["id"] == id:
            students.remove(student)

            return jsonify({
                "message": "Student deleted"
            })

    return jsonify({"error": "Student not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)