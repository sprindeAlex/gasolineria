from flask import Flask
from config.database import init_db
from app.routes.products_routes import products_bp
from app.routes.users_routes import users_bp
from app.routes.tickets_routes import tickets_bp

def create_app():
    app = Flask(__name__)
    
    # Initialize the database
    init_db(app)

    # Register blueprints
    app.register_blueprint(products_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(tickets_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)