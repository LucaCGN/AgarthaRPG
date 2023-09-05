from flask import Flask, redirect, url_for  # Added redirect, url_for
from config import *

def create_app():
    app = Flask(__name__)
    # Initialize MySQL configurations
    app.config['MYSQL_HOST'] = MYSQL_HOST
    app.config['MYSQL_DB_NAME'] = MYSQL_DB_NAME
    app.config['MYSQL_TABLE_NAME'] = MYSQL_TABLE_NAME
    app.config['MYSQL_USER'] = MYSQL_USER
    app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD

    @app.route('/')
    def index():
        return redirect(url_for('login_page'))  # Redirect to login page if not logged in

    from .routes import api as api_blueprint  # Move the import here to avoid circular import
    app.register_blueprint(api_blueprint, url_prefix='/api')  # Register the blueprint

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
