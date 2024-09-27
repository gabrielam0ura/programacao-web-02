from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Formulario(db.Model):
    __tablename__ = 'formulario'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text, nullable=False)

    perguntas = db.relationship('Pergunta', backref='formulario', cascade='all, delete-orphan')

class Pergunta(db.Model):
    __tablename__ = 'pergunta'
    
    id = db.Column(db.Integer, primary_key=True)
    id_formulario = db.Column(db.Integer, db.ForeignKey('formulario.id'), nullable=False)
    tipo_pergunta = db.Column(db.Enum('curta', 'longa', 'alternativas', 'multipla_escolha', name='tipo_pergunta'), nullable=False)
    texto = db.Column(db.Text, nullable=False)

    alternativas = db.relationship('Alternativa', backref='pergunta', cascade='all, delete-orphan')

class Alternativa(db.Model):
    __tablename__ = 'alternativa'
    
    id = db.Column(db.Integer, primary_key=True)
    id_pergunta = db.Column(db.Integer, db.ForeignKey('pergunta.id'), nullable=False)
    texto = db.Column(db.Text, nullable=False)
