import json
from flask import jsonify, request, Blueprint, send_file
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
        file = File(owner=user.id)
        if form.get('public').lower() == 'true':
          file.public = True
        file.fs.put(request.files["files"])
        file.save()
        return jsonify({'msg': 'File successfully created'}), 201
    except ValidationError as error:
        return jsonify(error.to_dict()), 403

@file_upload.route('/my', methods=['GET'])
@jwt_required()
@token_valid
def my_uploads(user):
    files = File.objects(owner=user.id)
    return jsonify(json.loads(files.to_json())), 200

@file_upload.route('/<file_id>', methods=['GET'])
@jwt_required()
@token_valid
def download(user, file_id):
    file = File.objects(id=file_id).first()
    print(file.owner.id)
    print(user.id)
    if not file.public and (file.owner.id != user.id):
        return jsonify({'msg': 'Not your private file'}), 403
    return file.fs.read()
