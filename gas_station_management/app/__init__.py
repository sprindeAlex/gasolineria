# File: /gas_station_management/gas_station_management/app/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Register blueprints or routes here
    from .routes.products_routes import products_bp
    from .routes.users_routes import users_bp
    from .routes.tickets_routes import tickets_bp

    app.register_blueprint(products_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(tickets_bp)

    return app