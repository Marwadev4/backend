from app.extensions import db
from datetime import datetime

class Font(db.Model):
    __tablename__ = 'fonts'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    family = db.Column(db.String(100), nullable=False)
    style = db.Column(db.String(50), nullable=False)
    filename = db.Column(db.String(255), nullable=False, unique=True)
    mimetype = db.Column(db.String(100))
    file_size = db.Column(db.Integer)  # in bytes
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'family': self.family,
            'style': self.style,
            'filename': self.filename,
            'mimetype': self.mimetype,
            'file_size': self.file_size,
            'created_at': self.created_at.isoformat()
        }
