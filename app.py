# app.py

from flask import Flask
from config import *
# Import other modules here

app = Flask(__name__)

# Initialize MySQL configurations
app.config['MYSQL_HOST'] = MYSQL_HOST
app.config['MYSQL_DB_NAME'] = MYSQL_DB_NAME
app.config['MYSQL_TABLE_NAME'] = MYSQL_TABLE_NAME
app.config['MYSQL_USER'] = MYSQL_USER
app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD

if __name__ == '__main__':
    app.run(debug=True)
