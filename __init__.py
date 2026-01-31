
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import ProductionConfig

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)
    db.init_app(app)

    from .auth.routes import auth_bp
    from .doctor.routes import doctor_bp
    from .patient.routes import patient_bp
    from .api.fhir import api_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(doctor_bp)
    app.register_blueprint(patient_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    with app.app_context():
        db.create_all()

    return app
