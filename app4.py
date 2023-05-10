from flask import Flask, request, jsonify

app4 = Flask(__name__)


materiais = []
quantidades = []

@app4.route('/materiais', methods=['GET'])#Busca Geral de materiais
def get_materiais():
    dados_materiais = []
    for i, material in enumerate(materiais):
        info_material = {
            'id': i,
            'name': material,
            'qtd': quantidades[i]
        }
        dados_materiais.append(info_material)
    response = jsonify({'materiais': dados_materiais}), 200
    return response



@app4.route('/quantidades', methods=['GET']) #Busca Geral de quantidades
def get_quantidades():
    response = jsonify({'quantidades': quantidades}), 200

    return response



@app4.route('/materiais', methods=['POST'])
def criar_novo_material():
    data = request.json
    material = data['material']
    nome = material['nome']
    qtd = material['qtd']
    materiais.append(nome)
    quantidades.append(qtd)
    response = jsonify({'Testando...': f'{nome} criado com sucesso!'}), 201
    return response



@app4.route('/materiais/<int:id>', methods=['GET'])#Procura material por ID
def buscar_material_por_id(id):
    if id < len(materiais):
        nome = materiais[id]
        qtd = quantidades[id]
        material = {
            'id': id,
            'nome': nome,
            'qtd': qtd
        }
        response = jsonify({'material': material}), 200
        return response
    else:
        response = jsonify({'Testando...': f'Material com ID {id} não encontrado.'}), 404
        return response
    

    
@app4.route('/materiais/<int:id>', methods=['PUT'])#Altera material
def atualizar_material(id):
    if id < len(materiais):
        material = request.json['material']
        materiais[id] = material['nome']
        quantidades[id] = material['qtd']
        response = jsonify({'Testando...': f'{material["nome"]} atualizado com sucesso!'}), 200
        return response
    else:
        response = jsonify({'Testando...': f'Material com ID {id} não encontrado.'}), 404
        return response
    

    
@app4.route('/materiais/<int:id>', methods=['DELETE'])#Deleta material
def remover_material(id):
    if id < len(materiais):
        del materiais[id]
        del quantidades[id]
        response = jsonify({'materiais': materiais}), 200
        return response
    else:
        response = jsonify({'Testando...': f'Material não encontrado.'}), 404
        return response


if __name__ == '__main__':

    app4.run(host="localhost", port="5000", debug=True)