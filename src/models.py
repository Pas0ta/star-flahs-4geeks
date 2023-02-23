from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    nombre = db.Column(db.String(250), unique=False, nullable=False)
    apellido = db.Column(db.String(250), unique=False, nullable=False)
    nombre_usuario = db.Column(db.String(250), unique=False, nullable=False)
    fecha_registro = db.Column(db.String(250), unique=False, nullable=False)
    favusuario = db.relationship('Favoritos', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "nombre_usuario": self.nombre_usuario,
            "fecha_registro": self.fecha_registro,
            # do not serialize the password, its a security breach
        }

class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    cumpleaños = db.Column(db.String(250), nullable=False)
    altura = db.Column(db.String(250), nullable=False)
    peso = db.Column(db.String(250), nullable=False)
    genero = db.Column(db.String(250), nullable=False)
    color_pelo = db.Column(db.String(250), nullable=False)
    color_piel =db.Column(db.String(250), nullable=False)
    favpersonajes = db.relationship('Favoritos', backref='personajes', lazy=True)

    def __repr__(self):
        return '<Personajes %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "cumpleaños": self.cumpleaños,
            "nombre": self.nombre,
            "altura": self.altura,
            "peso": self.peso,
            "genero": self.genero,
            "color_pelo": self.color_pelo,
            "color_piel": self.color_piel,
        }

class Planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    color = db.Column(db.String(250), nullable=True)
    tamaño = db.Column(db.String(250), nullable=True)
    posicion = db.Column(db.String(250), nullable=True)
    clima = db.Column(db.String(250), nullable=True)
    gravedad = db.Column(db.String(250), nullable=True)
    rotacion = db.Column(db.String(250), nullable=True)
    orbita = db.Column(db.String(250), nullable=True)
    terreno = db.Column(db.String(250), nullable=True)
    poblacion = db.Column(db.String(250), nullable=True)
    favplanetas = db.relationship('Favoritos', backref='planetas', lazy=True)

    def __repr__(self):
        return '<Planetas %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "color": self.color,
            "nombre": self.nombre,
            "tamaño": self.tamaño,
            "posicion": self.posicion,
            "clima": self.clima,
            "gravedad": self.gravedad,
            "rotacion": self.rotacion,
            "orbita": self.orbita,
            "terreno": self.terreno,
            "pobalcion": self.poblacion,
            }

class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    id_planetas = db.Column(db.Integer, db.ForeignKey('planetas.id'),
        nullable=True)
    id_personajes = db.Column(db.Integer, db.ForeignKey('personajes.id'),
        nullable=True)

    def __repr__(self):
        return '<Favoritos %r>' % self.id

def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "id_planetas": self.id_planetas,
            "id_personajes": self.id_personajes,
        }