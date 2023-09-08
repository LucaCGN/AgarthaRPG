from flask import Flask, redirect, url_for, request, session, render_template  # Added render_template
from config import *
import os



def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.secret_key = 'your_secret_key_here'  # Add this line
    print("Current Working Directory:", os.getcwd())
    print("Template Folder:", app.template_folder)
    # Initialize MySQL configurations
    app.config['MYSQL_HOST'] = MYSQL_HOST
    app.config['MYSQL_DB_NAME'] = MYSQL_DB_NAME
    app.config['MYSQL_TABLE_NAME'] = MYSQL_TABLE_NAME
    app.config['MYSQL_USER'] = MYSQL_USER
    app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD

    @app.route('/')
    def index():
        print("Inside index")
        if 'email' in session:
            print("Email found in session, redirecting to some_logged_in_page")
            return redirect(url_for('some_logged_in_page'))
        else:
            print("Staying on index")
            return render_template('index.html')  # Assuming you have an index.html template

    from .routes import api as api_blueprint  # Make sure this import is correct
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
