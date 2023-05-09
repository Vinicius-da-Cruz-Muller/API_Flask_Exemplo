# API é um "lugar" para disponibilizar recursos e/ou disponibilidades
#Objetivo: criar uma api que disponibliza a consulta, criação, edição e exclusão de livros
#URL Base - localhost - domínio utilizado, etc.
#Endpoints
    # - localhost/livros (GET)
    # - loclahost/livros (POST)
    # - localhost/livros/id (GET)
    # - localhost/livros/id (PUT)
    # - localhost/livros/id (DELETE)
#Quais recursos - livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Aneis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Percy Jackson e o Ladrão de Raios',
        'autor': 'Rick Riordan'
    },
    {
        'id': 3,
        'titulo': 'O Jogo dos Tronos',
        'autor': 'George R.R. Martin'
    },
]
#Consultar todos
@app.route('/livros', methods=['GET']) #@app.route('/livros') funciona, mas é preciso especificar que só poderemos usar esse método - só ele será aceito
def obter_livros():
    return jsonify(livros)
 #http://localhost:5000\livros para ver os livros no navegador
#Consultar por id
@app.route('/livros/<int:id>', methods=['GET']) #http://localhost:5000\livros\1 por exemplo
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
#Editar
@app.route('/livros/<int:id>', methods=['PUT']) #No postman - PUT, Body, raw, text para json, cola alteração, especifica id no endereço localhost
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
#Criar
@app.route('/livros', methods=['POST']) #POST, Body, raw, text para json, inclui alteração, endereço localhost (sem id, o id é incluso na alteração. não repetir ids)
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)
#Excluir
@app.route('/livros<int:id>', methods=['DELETE'])# altera para delete e passa o id
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)
app.run(port=5000, host='localhost', debug=True)