"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin
from flask_babelex import Babel


db = SQLAlchemy()
babel = Babel()



def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    app.config.from_object('config.Config')

    # Initialize Flask-BabelEx
    babel = Babel(app)

    # Initialize Flask-SQLAlchemy
    db = SQLAlchemy(app)

    with app.app_context():
        from . import routes
        from . import video
        from . import hardware
        from . import auth
        from .models import User

        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(video.video_bp)
        app.register_blueprint(hardware.hardware_bp)
        app.register_blueprint(auth.auth_bp)

        # Create Database Models
        db.create_all()

        # Setup Flask-User and specify the User data-model
        user_manager = UserManager(app, db, User)

        return app