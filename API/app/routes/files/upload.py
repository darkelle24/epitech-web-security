from flask import jsonify, request, Blueprint
from mongoengine.errors import ValidationError
from flask_jwt_extended import jwt_required
from app.middleware.token_valid import token_valid
from app.errors import *
from app.middleware.token_valid import token_valid
from app.middleware.request_form import request_form
from app.models.File import File

file_upload = Blueprint('file_upload', __name__)

@file_upload.route('/upload', methods=['POST'])
@jwt_required()
@token_valid
@request_form
def upload(form, user):
    try:
        if not request.files.getlist("files"):
            return jsonify({'msg': 'File required'}), 404
        for x in request.files.getlist("files"):
            upload = File(public=form.get('public'), owner=user.id)
            upload.filename = upload.id
            upload.fs.put(x, content_type=x.content_type)
            upload.save()
        return jsonify({'msg': 'File successfully created'}), 201
    except ValidationError as error:
        return jsonify(error.to_dict()), 403
