from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'my secret key'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_pass(username, password):
    if users.get(username) and check_password_hash(users.get(username)["password"], password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return 'Basic Auth: Access Granted'

@app.post('/login')
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users and check_password_hash(users[username]["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return "error: invalid username or password", 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()