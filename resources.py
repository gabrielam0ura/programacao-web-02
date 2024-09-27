from flask import Blueprint, request, jsonify, redirect, url_for
from models import db, Formulario, Pergunta, Alternativa

resources_bp = Blueprint('resources', __name__)

@resources_bp.route('/api/formulario', methods=['POST'])
def criar_formulario():
    data = request.get_json()
    print(data)
    formulario = Formulario(titulo=data['titulo'], descricao=data['descricao'])
    db.session.add(formulario)
    db.session.flush()

    if 'perguntaCurta' in data and data['perguntaCurta']:
        pergunta_curta = Pergunta(texto=data['perguntaCurta'], tipo_pergunta='curta', id_formulario=formulario.id)
        db.session.add(pergunta_curta)

    if 'perguntaLonga' in data and data['perguntaLonga']:
        pergunta_longa = Pergunta(texto=data['perguntaLonga'], tipo_pergunta='longa', id_formulario=formulario.id)
        db.session.add(pergunta_longa)

    if 'perguntaAlternativas' in data and data['perguntaAlternativas']:
        pergunta_alternativas = Pergunta(texto=data['perguntaAlternativas'], tipo_pergunta='alternativas', id_formulario=formulario.id)
        db.session.add(pergunta_alternativas)
        db.session.flush()

        alternativas = []
        for i in range(len(data)):
            chave = f'textoOpcaoAlternativa[{i}]'
            if chave in data:
                alternativas.append(data[chave])
            else:
                break
        
        for alternativa in alternativas:
            opcao_alternativa = Alternativa(texto=alternativa, id_pergunta=pergunta_alternativas.id)
            db.session.add(opcao_alternativa)

    if 'perguntaMultipla' in data and data['perguntaMultipla']:
        pergunta_multipla = Pergunta(texto=data['perguntaMultipla'], tipo_pergunta='multipla_escolha', id_formulario=formulario.id)
        db.session.add(pergunta_multipla)
        db.session.flush()

        alternativas_multipla = []
        for i in range(len(data)):
            chave = f'textoOpcaoMultipla[{i}]'
            if chave in data:
                alternativas_multipla.append(data[chave])
            else:
                break
        
        for alternativa in alternativas_multipla:
            opcao_multipla = Alternativa(texto=alternativa, id_pergunta=pergunta_multipla.id)
            db.session.add(opcao_multipla)

    db.session.commit()
    return redirect(url_for('meusForms'))

@resources_bp.route('/api/formulario/<int:id>', methods=['GET'])
def detalhes_formulario(id):
    formulario = Formulario.query.get_or_404(id)
    return jsonify({'titulo': formulario.titulo, 'descricao': formulario.descricao}), 200

# @resources_bp.route('/api/formulario/<int:id>/editar', methods=['POST'])
# def editar_formulario(id):
#     formulario = Formulario.query.get_or_404(id)
#     data = request.get_json()
    
#     formulario.titulo = data.get('titulo', formulario.titulo)
#     formulario.descricao = data.get('descricao', formulario.descricao)

#     perguntas_existentes = Pergunta.query.filter_by(id_formulario=formulario.id).all()
#     for pergunta in perguntas_existentes:
#         db.session.delete(pergunta)

#     if 'perguntaCurta' in data and data['perguntaCurta']:
#         db.session.add(Pergunta(texto=data['perguntaCurta'], tipo_pergunta='curta', id_formulario=formulario.id))

#     if 'perguntaLonga' in data and data['perguntaLonga']:
#         db.session.add(Pergunta(texto=data['perguntaLonga'], tipo_pergunta='longa', id_formulario=formulario.id))

#     if 'perguntaAlternativas' in data and data['perguntaAlternativas']:
#         pergunta_alternativas = Pergunta(texto=data['perguntaAlternativas'], tipo_pergunta='alternativas', id_formulario=formulario.id)
#         db.session.add(pergunta_alternativas)

#         for i in range(len(data)):
#             chave = f'textoOpcaoAlternativa[{i}]'
#             if chave in data:
#                 db.session.add(Alternativa(texto=data[chave], id_pergunta=pergunta_alternativas.id))

#     if 'perguntaMultipla' in data and data['perguntaMultipla']:
#         pergunta_multipla = Pergunta(texto=data['perguntaMultipla'], tipo_pergunta='multipla_escolha', id_formulario=formulario.id)
#         db.session.add(pergunta_multipla)

#         for i in range(len(data)):
#             chave = f'textoOpcaoMultipla[{i}]'
#             if chave in data:
#                 db.session.add(Alternativa(texto=data[chave], id_pergunta=pergunta_multipla.id))

#     db.session.commit()
#     return redirect(url_for('detalhes_form', id=id))

@resources_bp.route('/api/formulario/<int:id>/excluir', methods=['POST'])
def excluir_formulario(id):
    formulario = Formulario.query.get_or_404(id)
    db.session.delete(formulario)
    db.session.commit()
    return redirect(url_for('meusForms'))
