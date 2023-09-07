from flask import Blueprint, request, jsonify, redirect, url_for, session
from app.services import account_service  # Assuming this is the correct import path

api = Blueprint('api', __name__)

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

@api.route('/login', methods=['GET', 'POST'])
def api_login():
    if request.method == 'POST':
        try:
            req_data = request.json
            if not req_data:
                return jsonify({"message": "No JSON received"}), 415
            email = req_data['email']
            password = req_data['password']
            user = account_service.login_user(email, password)
            session['email'] = email
            return jsonify(user)
        except Exception as e:
            return jsonify({"message": str(e)}), 400
    else:
        # Handle GET request here
        return "Login Page"


@api.route('/request-password-reset', methods=['POST'])
def api_request_password_reset():
    email = request.json['email']
    account_service.send_password_reset_email(email)
    return jsonify({"message": "Password reset email sent"})

@api.route('/reset-password', methods=['POST'])
def api_reset_password():
    email = request.json['email']
    new_password = request.json['new_password']
    reset_token = request.json['reset_token']
    account_service.reset_password(email, new_password, reset_token)
    return jsonify({"message": "Password reset successfully"})
