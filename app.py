from flask import Flask
from models.models import db
from routes.routes import bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registros.db'

# Inicializar banco e rotas
db.init_app(app)
app.register_blueprint(bp)

# Criar banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
