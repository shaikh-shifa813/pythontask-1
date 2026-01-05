from flask import request, jsonify
from config import app, db
from models import Activity

# Create tables (first time only)
with app.app_context():
    db.create_all()

# 1. Create Activity
@app.route('/activity', methods=['POST'])
def create_activity():
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({'error': 'Activity name is required'}), 400

    new_activity = Activity(
        name=data['name'],
        description=data.get('description')
    )

    db.session.add(new_activity)
    db.session.commit()

    return jsonify({
        'id': new_activity.id,
        'name': new_activity.name,
        'description': new_activity.description
    }), 201

#2. Get All Activities
@app.route('/activity', methods=['GET'])
def get_all_activities():
    activities = Activity.query.all()
    result = []

    for activity in activities:
        result.append({
            'id': activity.id,
            'name': activity.name,
            'description':activity.description
        })
    return jsonify(result),200

#3. Get activity by ID
@app.route('/activity/<int:id>', methods=['GET'])
def get_activity_by_id(id):
    activity = Activity.query.get(id)   

    if not activity:
        return jsonify({'error': 'Activity not found'}), 404

    return jsonify({
        'id': activity.id,
        'name': activity.name,
        'description': activity.description
    }), 200

#4. Update Activity
@app.route('/activity/<int:id>', methods=['PUT'])
def update_activity(id):
    activity = Activity.query.get(id)

    if not activity:
        return jsonify({'error': 'Activity not found'}), 404

    data = request.get_json()

    if 'name' in data:
        activity.name = data['name']
    if 'description' in data:
        activity.description = data['description']

    db.session.commit()
    return jsonify({
        'id': activity.id,
        'name': activity.name,
        'description': activity.description
    }), 200

#5.Delete Activity
@app.route('/activity/<int:id>', methods=['DELETE'])
def delete_activity(id):
    activity = Activity.query.get(id)

    if not activity:
        return jsonify({'error': 'Activity not found'}), 404

    db.session.delete(activity)
    db.session.commit()

    return jsonify({'message': 'Activity deleted successfully'}), 200



if __name__ == '__main__':
    app.run(debug=True)

