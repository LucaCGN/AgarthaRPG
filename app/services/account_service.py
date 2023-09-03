from flask import jsonify, request, make_response
from models import AccountInfo as User, db_session  # Replace with your actual import
import hashlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import jwt
import datetime
import configparser  # Importing configparser

# Initialize the Config Parser
config = configparser.ConfigParser()

# Read the config file
config.read('path/to/config.ini')

# Get the JWT secret key
SECRET_KEY = config.get('JWT', 'SECRET_KEY')


# Function to encrypt password using SHA-256
def encrypt_password_sha(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(request):
    try:
        user_name = request.json['user_name']
        user_surname = request.json['user_surname']
        user_birthday = request.json['user_birthday']
        user_email = request.json['user_email']
        user_password = request.json['user_password']
        
        encrypted_password = encrypt_password_sha(user_password)
        
        user_code = random.randint(100000, 999999)
        
        new_user = User(
            user_name=user_name,
            user_surname=user_surname,
            user_birthday=user_birthday,
            user_email=user_email,
            user_password=encrypted_password,
            user_verified='no',
            user_code=user_code
        )
        db_session.add(new_user)
        db_session.commit()
        
        send_verification_email(user_email, user_code)
        
        return jsonify({"message": "User registered successfully"})
    
    except Exception as e:
        return jsonify({"message": str(e)})

def verify_email(request):
    try:
        email = request.json['email']
        verification_code = request.json['verification_code']
        
        user = db_session.query(User).filter_by(user_email=email).first()
        
        if user and user.user_code == int(verification_code):
            user.user_verified = 'yes'
            db_session.commit()
            return jsonify({"message": "Email verified"})
        
        return jsonify({"message": "Invalid verification code"})
    
    except Exception as e:
        return jsonify({"message": str(e)})

def login_user(request):
    try:
        email = request.json['email']
        password = request.json['password']
        encrypted_password = encrypt_password_sha(password)
        
        user = db_session.query(User).filter_by(user_email=email, user_password=encrypted_password).first()
        
        if user:
            token = jwt.encode({'user_id': user.user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, "SECRET_KEY")
            return make_response(jsonify({"token": token.decode('UTF-8')}), 200)
        
        return make_response(jsonify({"message": "Invalid email or password"}), 401)
    
    except Exception as e:
        return make_response(jsonify({"message": str(e)}), 500)

def send_verification_email(email, user_code):
    try:
        # Initialize the Config Parser
        config = configparser.ConfigParser()
        
        # Read the config file
        config.read('path/to/config.ini')
        
        # Get the email password
        email_password = config.get('Email', 'EmailPassword')
        
        msg = MIMEMultipart()
        msg['From'] = 'agartha.ai.rpg@gmail.com'
        msg['To'] = email
        msg['Subject'] = 'Agartha RPG: Email Verification'
        
        body = f'Your verification code is {user_code}'
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(msg['From'], email_password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        
        return jsonify({"message": "Verification email sent"})
    
    except Exception as e:
        return jsonify({"message": str(e)})

def send_reset_password_email(request):
    try:
        # Initialize the Config Parser
        config = configparser.ConfigParser()
        
        # Read the config file
        config.read('path/to/config.ini')
        
        # Get the email password
        email_password = config.get('Email', 'EmailPassword')
        
        email = request.json['email']
        
        # Generate a unique token for password reset (you can use JWT or any other method)
        reset_token = "some_unique_token"
        
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = 'agartha.ai.rpg@gmail.com'
        msg['To'] = email
        msg['Subject'] = 'Agartha RPG: Password Reset'
        body = f'Click the link to reset your password: http://66.94.118.226/reset_password/{reset_token}'
        msg.attach(MIMEText(body, 'plain'))
        
        # Send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(msg['From'], email_password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        
        return jsonify({"message": "Password reset link sent"})
    except Exception as e:
        return jsonify({"message": str(e), "status": "error"}), 500
        
def update_password(request):
    try:
        email = request.json['email']
        new_password = request.json['new_password']
        
        # Encrypt the new password
        encrypted_password = encrypt_password_sha(new_password)
        
        # Find the user and update the password
        user = db_session.query(User).filter_by(user_email=email).first()
        if user:
            user.user_password = encrypted_password
            db_session.commit()
            return jsonify({"message": "Password updated successfully"})
        else:
            return jsonify({"message": "User not found", "status": "error"}), 404
    except Exception as e:
        return jsonify({"message": str(e), "status": "error"}), 500