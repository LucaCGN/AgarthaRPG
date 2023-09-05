from flask import Flask, redirect, url_for, request, session
from config import *

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key_here'  # Add this line

    # Initialize MySQL configurations
    app.config['MYSQL_HOST'] = MYSQL_HOST
    app.config['MYSQL_DB_NAME'] = MYSQL_DB_NAME
    app.config['MYSQL_TABLE_NAME'] = MYSQL_TABLE_NAME
    app.config['MYSQL_USER'] = MYSQL_USER
    app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD

    @app.before_request
    def require_login():
        print(f"Endpoint: {request.endpoint}")
        print(f"Session: {session}")
        allowed_routes = ['index', 'api.api_login', 'api.api_register']
        if request.endpoint not in allowed_routes and 'email' not in session:
            print("Redirecting to index")
            return redirect(url_for('index'))

    @app.route('/')
    def index():
        print("Inside index")
        if 'email' in session:
            print("Email found in session, redirecting to some_logged_in_page")
            return redirect(url_for('some_logged_in_page'))
        print("Redirecting to api_login")
        return redirect(url_for('api.api_login'))

    from .routes import api as api_blueprint  # Make sure this import is correct
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
