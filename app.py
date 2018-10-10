from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Category import CategoryResource
from resources.Comment import CommentResource
from resources.Translation import TranslationResource
from resources.Language import LanguageResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes

api.add_resource(Hello, '/Hello')
api.add_resource(CategoryResource, '/Category')
api.add_resource(CommentResource, '/Comment')
api.add_resource(TranslationResource, '/Translation')
api.add_resource(LanguageResource, '/Language')
