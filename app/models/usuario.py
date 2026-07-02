from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash

class Usuario(db.Model):
    __tablename__='usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    password= db.Column(db.String(256),nullable=False)
    rol = db.Column(db.Enum('cliente','admin'),default='cliente')
    activo = db.Column(db.Boolean, default=True)
    creado_en = db.Column(db.DateTime, default=datetime.now())

    #relacion: un usuario tiene muchos pedidos
    pedidos = db.relationship('Pedido', backref='usuario', lazy=True)

    #--METODOS DE CONTRASENA--

    def set_password(self, password_plano):
        """Hash a la contraseña en texto plano"""
        self.password = generate_password_hash(password_plano)

    def __repr__(self):
        return f'<Usuario: {self.email} | {self.rol}>'