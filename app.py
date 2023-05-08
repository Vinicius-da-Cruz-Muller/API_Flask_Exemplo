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
#Consultar por id
#Editar
#Excluir