from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")  # Configuração para banco de dados
app.config["SECRET_KEY"] = "5299b6dc3e8f9af13324341b873c4880"  # Configuração para senha de login
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"   # Faz o upload das fotos que o usuário enviar.

database = SQLAlchemy(app)  # Banco de dados
bcrypt = Bcrypt(app)   # Gerador de senhas criptografadas
login_manager = LoginManager(app)  # Gerencia o login
login_manager.login_view = "homepage"  # Página que vai rodar o login


from fakepinterest import routes