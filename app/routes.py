from app import app 
# routes.py

from flask import Flask, request, jsonify
from account_service import login_user, register_user, send_verification_email, verify_email
import configparser

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def api_register():
    user_details = request.json
    register_user(user_details)
    return jsonify({"message": "User registered successfully"})

@app.route('/email-verification', methods=['POST'])
def api_email_verification():
    email = request.json['email']
    send_verification_email(email)
    return jsonify({"message": "Verification email sent"})

@app.route('/verify-email', methods=['POST'])
def api_verify_email():
    email = request.json['email']
    verification_code = request.json['verification_code']
    verify_email(email, verification_code)
    return jsonify({"message": "Email verified"})

@app.route('/send-reset-password-email', methods=['POST'])
def api_send_reset_password_email():
    try:
        email = request.json['email']
        # Your logic to send reset password email
        return jsonify({"message": "Reset password email sent"})
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
@app.route('/login', methods=['POST'])
def api_login():
    try:
        email = request.json['email']
        password = request.json['password']
        user = login_user(email, password)
        return jsonify(user)
    except Exception as e:
        return jsonify({"message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)