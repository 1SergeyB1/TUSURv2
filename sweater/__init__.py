from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)
# Секретный ключ приложения
app.config['SECRET_KEY'] = 'you-will-never-guess'
# Подключение к бд
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Data.db'
# hashes the password and then stores in the database
app.config['SECURITY_PASSWORD_SALT'] = "vG}KjS0Uh#gOyHY"
# allows new registrations to application
app.config['SECURITY_REGISTERABLE'] = True
# to send automatic registration email to user
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
# Максимальный размер файла, загружаемого на сервис(предположительно 10 МБ)
app.config['MAX_CONTENT_LENGHT'] = 10240 * 1024
# Папка для загрузки файлов
app.config['UPLOAD_FOLDER'] = 'uploads'
# Логин менеджер
manager = LoginManager(app)
# объект для хранения бд
db = SQLAlchemy(app)

import routes
import models
