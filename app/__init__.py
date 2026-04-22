import os
from flask import Flask
from app.config import config
from app.extensions import db, ma, cors

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)

    # Register blueprints
    from app.api.fonts import fonts_bp
    app.register_blueprint(fonts_bp)

    # Create tables
    with app.app_context():
        db.create_all()

    @app.route('/health')
    def health_check():
        return {'status': 'healthy'}

    return app
