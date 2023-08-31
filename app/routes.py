# routes.py

from flask import Flask, request, jsonify
from account_service import login_user, register_user, send_verification_email, verify_email

app = Flask(__name__)

@app.route('/api/login', methods=['POST'])
def api_login():
    email = request.json['email']
    password = request.json['password']
    user = login_user(email, password)
    return jsonify(user)

@app.route('/api/register', methods=['POST'])
def api_register():
    user_details = request.json
    register_user(user_details)
    return jsonify({"message": "User registered successfully"})

@app.route('/api/email-verification', methods=['POST'])
def api_email_verification():
    email = request.json['email']
    send_verification_email(email)
    return jsonify({"message": "Verification email sent"})

@app.route('/api/verify-email', methods=['POST'])
def api_verify_email():
    email = request.json['email']
    verification_code = request.json['verification_code']
    verify_email(email, verification_code)
    return jsonify({"message": "Email verified"})

if __name__ == '__main__':
    app.run(debug=True)
