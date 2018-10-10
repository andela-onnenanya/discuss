from flask import request
from flask_restful import Resource
from Model import db, Language, LanguageSchema
import simplejson as json
from sqlalchemy import or_

languages_schema = LanguageSchema(many=True)
language_schema = LanguageSchema()

class LanguageResource(Resource):
    def get(self):
        languages = Language.query.all()
        languages = languages_schema.dump(languages).data
        return {'status': 'success', 'data': languages}, 200
    
    def post(self):
        json_data = json.loads(request.data)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = language_schema.load(json_data)
        if errors:
            return errors, 422
        language = Language.query.filter(or_(Language.code==data['code'], Language.name==data['name'])).first()
        if language :
            return {'message': 'Language already exists'}, 400
        language = Language(
            name=json_data['name'],
            code=json_data['code']
            )

        db.session.add(language)
        db.session.commit()

        result = language_schema.dump(language).data

        return { "status": 'success', 'data': result }, 201
    
    def put(self):
        json_data = json.loads(request.data)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = language_schema.load(json_data)
        if errors:
            return errors, 422
        language = Language.query.filter_by(id=request.args.get('id')).first()
        if not language:
            return {'message': 'Language does not exist'}, 400
        for key, value in data.items():
            if language[key] and language[key] != 'id':
              setattr(language, key, value)
        # language.name = data['name']
        db.session.commit()

        result = language_schema.dump(language).data

        return { "status": 'success', 'data': result }, 200
    
    def delete(self):
        json_data = json.loads(request.data)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = language_schema.load(json_data)
        if errors:
            return errors, 422
        language = Language.query.filter_by(id=request.args.get('id')).delete()
        db.session.commit()

        result = language_schema.dump(language).data

        return { "status": 'success', 'data': result}, 200

