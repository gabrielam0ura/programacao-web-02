from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from models import db, Formulario, Pergunta, Alternativa
from resources import resources_bp, criar_formulario, excluir_formulario

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:011711@localhost:5432/fields'

db.init_app(app)

app.register_blueprint(resources_bp)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/criar')
def criar():
    return render_template('criar.html')

@app.route('/api/formulario', methods=['POST'])
def criar_formulario_rota():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Nenhum dado JSON recebido"}), 400
    criar_formulario(data)
    return redirect(url_for('meusForms'))

@app.route('/meus')
def meusForms():
    formularios = Formulario.query.all()
    return render_template('meus.html', formularios=formularios)

@app.route('/formulario/<int:id>')
def detalhes_form(id):
    formulario = Formulario.query.get_or_404(id)
    perguntas = Pergunta.query.filter_by(id_formulario=formulario.id)
    return render_template('detalhes_form.html', formulario=formulario, perguntas=perguntas)

# @app.route('/formulario/<int:id>/editar', methods=['GET'])
# def editar_form(id):
#     formulario = Formulario.query.get_or_404(id)
#     return render_template('editar_form.html', formulario=formulario)

# @app.route('/api/formulario/<int:id>/editar', methods=['POST'])
# def editar_formulario_rota(id):
#     data = request.get_json()
#     if data is None:
#         return jsonify({"error": "Nenhum dado JSON recebido"}), 400
#     editar_formulario(id, data)
#     return redirect(url_for('detalhes_form', id=id))

@app.route('/api/formulario/<int:id>/excluir', methods=['POST'])
def excluir_formulario_rota(id):
    excluir_formulario(id)
    return redirect(url_for('meusForms'))

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == '__main__':
    app.run(debug=True)