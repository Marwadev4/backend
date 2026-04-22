import os
import magic
from werkzeug.utils import secure_filename
from flask import current_app

class FileService:
    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

    @staticmethod
    def validate_magic_bytes(file_stream):
        # Read the first 2048 bytes to detect the file type
        file_header = file_stream.read(2048)
        file_stream.seek(0)  # Reset stream position
        
        mime = magic.from_buffer(file_header, mime=True)
        # Font mime types can vary, commonly application/x-font-ttf, font/ttf, etc.
        valid_mime_prefixes = ['font/', 'application/x-font-', 'application/font-']
        
        return any(mime.startswith(prefix) for prefix in valid_mime_prefixes) or \
               mime in ['application/octet-stream', 'application/vnd.ms-fontobject']

    @staticmethod
    def save_font(file):
        if not file or not FileService.allowed_file(file.filename):
            raise ValueError("Invalid file extension")

        if not FileService.validate_magic_bytes(file.stream):
            raise ValueError("Invalid font file content (magic byte validation failed)")

        filename = secure_filename(file.filename)
        # Handle duplicates by adding a timestamp or UUID if needed, but for now simple secure_filename
        
        upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        
        # Ensure directory exists
        os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
        
        file.save(upload_path)
        
        return filename, os.path.getsize(upload_path), file.mimetype

    @staticmethod
    def delete_font_file(filename):
        path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(path):
            os.remove(path)
