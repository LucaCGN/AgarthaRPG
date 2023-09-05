from flask import Blueprint, request, jsonify, redirect, url_for, session
from app.services import account_service  # Assuming this is the correct import path

api = Blueprint('api', __name__)

@api.before_request
def require_login():
    allowed_routes = ['api_login', 'api_register']
    if request.endpoint not in allowed_routes and 'email' not in session:
        return redirect(url_for('index'))

@api.route('/register', methods=['POST'])
def api_register():
    user_details = request.json
    account_service.register_user(user_details)
    return jsonify({"message": "User registered successfully"})

@api.route('/email-verification', methods=['POST'])
def api_email_verification():
    email = request.json['email']
    account_service.send_verification_email(email)
    return jsonify({"message": "Verification email sent"})

@api.route('/verify-email', methods=['POST'])
def api_verify_email():
    email = request.json['email']
    verification_code = request.json['verification_code']
    account_service.verify_email(email, verification_code)
    return jsonify({"message": "Email verified"})

@api.route('/login', methods=['POST'])
def api_login():
    try:
        email = request.json['email']
        password = request.json['password']
        user = account_service.login_user(email, password)
        session['email'] = email
        return jsonify(user)
    except Exception as e:
        return jsonify({"message": str(e)}), 400
