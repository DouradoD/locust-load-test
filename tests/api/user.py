# Flask for web framework, request for handling HTTP requests, jsonify for JSON responses
from flask import Flask, request, jsonify, abort
# SQLAlchemy for ORM (Object-Relational Mapping)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

# Initialize Flask application
app = Flask(__name__)

# Configure database - Using SQLite for simplicity (no additional server needed)
# SQLALCHEMY_DATABASE_URI specifies the database location
# SQLALCHEMY_TRACK_MODIFICATIONS is disabled to avoid overhead
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database file will be created in project directory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disables modification tracking as it's not needed here

# Initialize SQLAlchemy with Flask app
db = SQLAlchemy(app)


# Define User model - This represents the users table in the database
class User(db.Model):
    # Each class attribute represents a database column
    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing primary key
    name = db.Column(db.String(80), nullable=False)  # String column (max 80 chars), cannot be null
    email = db.Column(db.String(120), unique=True, nullable=False)  # Unique email, cannot be null

    # Method to convert User object to dictionary for JSON response
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }


# Create database tables before first request (if they don't exist)
@app.before_request
def create_tables():
    db.create_all()  # This creates all defined models in the database


# CREATE endpoint - Add a new user
@app.route('/users', methods=['POST'])
def create_user():
    # Get JSON data from request
    data = request.get_json()

    # Create new User instance
    user = User(name=data['name'], email=data['email'])

    # Add to database session and commit
    db.session.add(user)
    db.session.commit()

    # Return the created user with 201 Created status
    return jsonify(user.to_dict()), 201

def get_user_by(user_id):
    return db.session.get(User, user_id)

# READ (all) endpoint - Get all users
@app.route('/users', methods=['GET'])
def get_users():
    # Query all users from database
    users = db.session.scalars(select(User)).all()

    # Convert each user to dict and return as JSON array
    return jsonify([user.to_dict() for user in users])


# READ (single) endpoint - Get specific user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Get user by ID or return 404 if not found
    user = get_user_by(user_id)
    if user is None:
        abort(404)

    # Return user data as JSON
    return jsonify(user.to_dict())


# UPDATE endpoint - Modify existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Get user by ID or return 404
    user = get_user_by(user_id)

    # Get updated data from request
    data = request.get_json()

    # Update user attributes
    user.name = data['name']
    user.email = data['email']

    # Commit changes to database
    db.session.commit()

    # Return updated user data
    return jsonify(user.to_dict())


# DELETE endpoint - Remove user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Get user by ID or return 404
    user = get_user_by(user_id)

    # Delete user from database
    db.session.delete(user)
    db.session.commit()

    # Return success message
    return jsonify({'message': 'User deleted'}), 200



# Run the application if executed directly
if __name__ == '__main__':
    # debug=True enables auto-reload and better error messages
    app.run(host='0.0.0.0', port=5000, debug=True)