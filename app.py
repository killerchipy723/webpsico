from flask import Flask
from db import db
from routes.main_routes import main_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clave_secreta_ines_camano_demo'
    
    # Configuración de base de datos (puedes ajustar URI según utilices SQLite/MySQL)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webpsico.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Registro de Blueprints
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)