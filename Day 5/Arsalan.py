from flask import Flask, jsonify

app = Flask(__name__)

# Sample student data
students = [
    {"id": 1, "name": "Arsalan Ansari", "course": "B.Tech CSE"},
    {"id": 2, "name": "Vansh Jain", "course": "B.Tech CSE"},
    {"id": 3, "name": "Mitali Kaushal", "course": "B.Tech AI ML"}
]

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
