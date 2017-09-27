from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/yummy_recipe_api_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 

db = SQLAlchemy(app)

migrate = Migrate(app, db)
# from yummy_recipe.models import *


@app.route('/user', methods=['POST'])
# @token_required current_user
def register_user():

    return ''


@app.route('/login', methods=['POST'])
def login():

    return ''


@app.route('/category', methods=['GET'])
# @token_required current_user
def get_all_categories():

    return ''


@app.route('/recipe', methods=['GET'])
# @token_required current_user
def get_one_recipe():

    return ''


if __name__ == '__main__':
    app.run(debug=True)