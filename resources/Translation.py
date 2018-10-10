from flask import jsonify, request
from flask_restful import Resource
from Model import db, Comment, Translation, TranslationSchema

translations_schema = TranslationSchema(many=True)
translation_schema = TranslationSchema()

class TranslationResource(Resource):
    def get(self):
        translations = Translation.query.all()
        translations = translations_schema.dump(translations).data
        return {"status":"success", "data":translations}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = translation_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        comment_id = Comment.query.filter_by(id=data['comment_id']).first()
        language_id = Comment.query.filter_by(id=data['language_id']).first()
        if not comment_id:
            return {'status': 'error', 'message': 'comment not found'}, 400
        if not language_id:
            return {'status': 'error', 'message': 'language not found'}, 400
        translation = Translation(
            comment_id=data['comment_id'],
            language_id = data['language_id'],
            translation=data['translation']
            )
        db.session.add(translation)
        db.session.commit()

        result = translation_schema.dump(translation).data

        return {'status': "success", 'data': result}, 201
    