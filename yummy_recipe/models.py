from sqlalchemy import ForeignKey
from app import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return '<name {}>'.format(self.name)


class Recipe(db.Model):

    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50))
    category_id = db.Column(db.Integer, ForeignKey('categories.id'))
    user_id = db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, recipe_name):
        self.recipe_name = recipe_name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Recipe.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<recipe_name {}>'.format(self.recipe_name)


class Category(db.Model):

    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50))
    user_id = db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, category_name):
        self.category_name = category_name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Category.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()    

    def __repr__(self):
        return '<category_name {}>'.format(self.category_name)
