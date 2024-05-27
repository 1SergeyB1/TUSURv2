from sweater import db, manager
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    # Название таблицы в бд
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # Имя
    first_name = db.Column(db.String())
    # Фамилия
    last_name = db.Column(db.String())
    # Отчество
    patronymic = db.Column(db.String())
    # почта
    email = db.Column(db.String(), unique=True)
    # роль
    role = db.Column(db.Boolean, default=False)
    # пароль
    password = db.Column(db.String())
    # photo
    photo = db.Column(db.String())
    # Имущество, закреплённое за пользователем
    property = db.relationship("Property")


class Building(db.Model):
    # Название таблицы в бд
    __tablename__ = 'buildings'
    id = db.Column(db.Integer, primary_key=True)
    # photo
    photo = db.Column(db.String())
    # Адресс
    address = db.Column(db.String())
    # помещения
    floor = db.relationship("Floor")


class Floor(db.Model):
    # Название таблицы в бд
    __tablename__ = 'floor'
    id = db.Column(db.Integer, primary_key=True)
    # photo
    number = db.Column(db.Integer)
    # корпус
    building = db.Column(db.Integer, db.ForeignKey(Building.id))
    # помещения
    rooms = db.relationship("Room")


class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    floor = db.Column(db.Integer(), db.ForeignKey(Floor.id))
    number = db.Column(db.Integer())
    photo = db.Column(db.String())
    property = db.relationship("Property")


class Category(db.Model):
    __tablename__ = 'categorys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    property = db.relationship('Property')


class Property(db.Model):
    __tablename__ = 'propertys'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    category = db.Column(db.Integer, db.ForeignKey(Category.id))
    photo = db.Column(db.String())
    is_works = db.Column(db.Boolean,default=True)
    location = db.Column(db.Integer, db.ForeignKey(Room.id))
    responsible_person = db.Column(db.Integer, db.ForeignKey(User.id))
    date_of_commissioning = db.Column(db.DateTime(timezone=True), server_default=func.now())
    qr_code = db.Column(db.String())
    history = db.relationship('History')


class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey(Property.id))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    room_id = db.Column(db.Integer, db.ForeignKey(Room.id))
    date_of = db.Column(db.DateTime(timezone=True), server_default=func.now())


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
