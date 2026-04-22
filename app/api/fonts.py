import os
from flask import Blueprint, request, jsonify, send_from_directory, current_app
from app.services.font_service import FontService

fonts_bp = Blueprint('fonts', __name__, url_prefix='/api/fonts')

@fonts_bp.route('', methods=['GET'])
def list_fonts():
    fonts = FontService.get_all_fonts()
    return jsonify([f.to_dict() for f in fonts])

@fonts_bp.route('/<int:font_id>', methods=['GET'])
def get_font(font_id):
    font = FontService.get_font_by_id(font_id)
    if not font:
        return jsonify({'error': 'Font not found'}), 404
    return jsonify(font.to_dict())

@fonts_bp.route('/upload', methods=['POST'])
def upload_font():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    name = request.form.get('name')
    family = request.form.get('family')
    style = request.form.get('style')

    if not all([name, family, style]):
        return jsonify({'error': 'Missing metadata (name, family, style)'}), 400

    try:
        font = FontService.upload_font(file, name, family, style)
        return jsonify(font.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

@fonts_bp.route('/<int:font_id>', methods=['PUT'])
def update_font(font_id):
    data = request.get_json()
    font = FontService.update_font(font_id, data)
    if not font:
        return jsonify({'error': 'Font not found'}), 404
    return jsonify(font.to_dict())

@fonts_bp.route('/<int:font_id>', methods=['DELETE'])
def delete_font(font_id):
    success = FontService.delete_font(font_id)
    if not success:
        return jsonify({'error': 'Font not found'}), 404
    return jsonify({'message': 'Font deleted successfully'})

@fonts_bp.route('/<int:font_id>/download', methods=['GET'])
def download_font(font_id):
    font = FontService.get_font_by_id(font_id)
    if not font:
        return jsonify({'error': 'Font not found'}), 404
    
    return send_from_directory(
        current_app.config['UPLOAD_FOLDER'],
        font.filename,
        as_attachment=True
    )
