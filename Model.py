from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from sqlalchemy import UniqueConstraint
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(250), nullable=False)
    score = db.Column(db.Integer, server_default='0', nullable=True)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    category = db.relationship('Category', backref=db.backref('comments', lazy='dynamic' ))

    def __init__(self, comment, category_id, score):
        self.comment = comment
        self.category_id = category_id
        self.score = score


class Translation(db.Model):
    __tablename__ = 'translations'
    id = db.Column(db.Integer, primary_key=True)
    translation = db.Column(db.String(250), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id', ondelete='CASCADE'), nullable=False)
    comment = db.relationship('Comment', backref=db.backref('translations', lazy='dynamic' ))
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id', ondelete='CASCADE'), nullable=False)
    comment = db.relationship('Language', backref=db.backref('translations', lazy='dynamic' ))
    __table_args__ = (UniqueConstraint('language_id', 'comment_id', name='_comment_language_uc'),)

    def __init__(self, translation, comment_id, language_id):
        self.translation = translation
        self.comment_id = comment_id
        self.language_id = language_id

class Language(db.Model):
    __tablename__ = 'languages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    code = db.Column(db.String(2), nullable=False, unique=True)

    def __init__(self, name, code):
        self.name = name
        self.code = code

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name


class CategorySchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)

class LanguageSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    code = fields.String(required=True)


class TranslationSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    comment_id = fields.Integer(required=True)
    translation = fields.String(required=True, validate=validate.Length(1))
    language_id = fields.Integer(required=True)

class CommentSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    category_id = fields.Integer(required=True)
    comment = fields.String(required=True, validate=validate.Length(1))
    creation_date = fields.DateTime()
    score = fields.Integer(required=False)
    