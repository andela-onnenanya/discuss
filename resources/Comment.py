from flask import jsonify, request
from flask_restful import Resource
from Model import db, Comment, Category, CommentSchema, Translation, TranslationSchema, Language, LanguageSchema
import simplejson as json
from sqlalchemy import or_
from sqlalchemy import and_

comments_schema = CommentSchema(many=True)
comment_schema = CommentSchema()
translation_schema = TranslationSchema()
translations_schema = TranslationSchema(many=True)
langeuage_schema = LanguageSchema()

class CommentResource(Resource):
    def get(self):
        if request.args.get('id'):
            comment_id = request.args.get('id')
            comment = Comment.query.filter_by(id=request.args.get('id')).first()
            if request.args.get('language_id'):
                language_id = request.args.get('language_id')
                translation = Translation.query.filter(and_(Translation.language_id==language_id, 
                    Translation.comment_id==comment_id)).first()
                if not translation:
                    return {'message': 'Translation not found'}, 400
                language = Language.query.filter_by(id=request.args.get('id')).first()
                language = langeuage_schema.dump(language).data['name']
                translation = translation_schema.dump(translation).data['translation']
                result = comment_schema.dump(comment).data
                result['translation']=translation
                result['translation_lang'] = language
                # setattr(result, 'translation', translation)
                return {"status":"success", "data":result}, 200
            if request.args.get('translations'):
                translations = Translation.query.filter(Translation.comment_id==comment_id).all()
                translations = translations_schema.dump(translations).data
                result = comment_schema.dump(comment).data
                result['translations']=translations
                # setattr(result, 'translation', translation)
                return {"status":"success", "data":result}, 200


        comments = Comment.query.all()
        comments = comments_schema.dump(comments).data
        return {"status":"success", "data":comments}, 200

    def post(self):
        json_data = json.loads(request.data)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = comment_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        category_id = Category.query.filter_by(id=data['category_id']).first()
        if not category_id:
            return {'status': 'error', 'message': 'comment category not found'}, 400
        if 'score' in json_data:
            return {'status': 'error', 'message': 'Score can not be added when commenting'}, 422
        comment = Comment(
            category_id=data['category_id'], 
            comment=data['comment'],
            score=0
            )
        db.session.add(comment)
        db.session.commit()

        result = comment_schema.dump(comment).data

        return {'status': "success", 'data': result}, 201
    
    def put(self):
        json_data = json.loads(request.data)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = comment_schema.load(json_data)
        if errors:
            return errors, 422
        comment = Comment.query.filter_by(id=request.args.get('id')).first()
        if not comment:
            return {'message': 'Comment does not exist'}, 400
        if 'score' in json_data:
            return {'status': 'error', 'message': 'Score can not be edited directly'}, 422
        for key, value in data.items():
            if data[key] and data[key] != 'id':
                setattr(comment, key, value)
        
        if request.args.get('vote') == 'up':
            setattr(comment, 'score', comment_schema.dump(comment).data['score'] + 1)
        if request.args.get('vote') == 'down':
            setattr(comment, 'score', comment_schema.dump(comment).data['score'] - 1)
        # language.name = data['name']
        db.session.commit()

        result = comment_schema.dump(comment).data
        return { "status": 'success', 'data': result }, 200
    