from flask import Flask, request, jsonify  # Flask-creates the app, jsonify-converts Python dict to JSON

app = Flask(__name__)  # __name__ helps Flask know where the app is running

# Mock users data
users = [
    {"id": 1, "name": "Ayaan"},
    {"id": 2, "name": "Sara"}
]

@app.route('/')  # when someone visits /
def home():  # function runs
    return jsonify({  # returns JSON response
        "message": "API is working"
    })

# GET API - Users List(task 2)
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({
        "status": "success",
        "count": len(users),
        "data": users
    })

# GET API - User by ID (Task 3)
@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    for user in users:
        if user["id"] == id:
            return jsonify(user), 200

    return jsonify({
        "error": "User not found"
    }), 404

# POST API - Add User (Task 4)
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json

    # Validation
    if not data:
        return jsonify({"error": "JSON body required"}), 400

    if not data.get("name"):
        return jsonify({"error": "Name cannot be empty"}), 400

    if not data.get("email"):
        return jsonify({"error": "Email is required"}), 400

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }

    users.append(new_user)

    return jsonify({
        "message": "User added successfully",
        "user": new_user
    }), 201

if __name__ == "__main__":  # Runs server only if file is main
    app.run(debug=True)
