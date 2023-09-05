from flask import Flask, session
from config import *

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key_here'  # For session handling
    # Initialize MySQL configurations
    app.config['MYSQL_HOST'] = MYSQL_HOST
    app.config['MYSQL_DB_NAME'] = MYSQL_DB_NAME
    app.config['MYSQL_TABLE_NAME'] = MYSQL_TABLE_NAME
    app.config['MYSQL_USER'] = MYSQL_USER
    app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD

    from .routes import api as api_blueprint  # Move the import here to avoid circular import
    app.register_blueprint(api_blueprint, url_prefix='/api')  # Register the blueprint

    @app.route('/')
    def index():
        if 'email' in session:
            return redirect(url_for('some_logged_in_page'))
        return redirect(url_for('login_page'))

    return app
