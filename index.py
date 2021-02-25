from app import create_app, db
from app.models import user
from flask_migrate import Migrate

app = create_app('development')
# app = create_app('testing')  # 切換成測試環境。

# 遷移腳本
migrate = Migrate(app, db)
