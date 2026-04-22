from app.models.font import Font
from app.extensions import db
from app.services.file_service import FileService

class FontService:
    @staticmethod
    def get_all_fonts():
        return Font.query.all()

    @staticmethod
    def get_font_by_id(font_id):
        return Font.query.get(font_id)

    @staticmethod
    def upload_font(file, name, family, style):
        filename, size, mimetype = FileService.save_font(file)
        
        font = Font(
            name=name,
            family=family,
            style=style,
            filename=filename,
            file_size=size,
            mimetype=mimetype
        )
        
        db.session.add(font)
        db.session.commit()
        
        return font

    @staticmethod
    def update_font(font_id, data):
        font = Font.query.get(font_id)
        if not font:
            return None
            
        font.name = data.get('name', font.name)
        font.family = data.get('family', font.family)
        font.style = data.get('style', font.style)
        
        db.session.commit()
        return font

    @staticmethod
    def delete_font(font_id):
        font = Font.query.get(font_id)
        if not font:
            return False
            
        # Delete physical file
        FileService.delete_font_file(font.filename)
        
        # Delete DB record
        db.session.delete(font)
        db.session.commit()
        return True
