from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configs.config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # 取得組態物件
    app.debug = config[config_name].DEBUG  # debug mode
    db.init_app(app)

    # view
    from app.views.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    from app.views.frontend import frontend as frontend_blueprint
    app.register_blueprint(frontend_blueprint)

    return app
