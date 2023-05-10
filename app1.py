from flask import Flask, request, jsonify
#import json

app1 = Flask(__name__)

# Customers list
customers = []
#     {
#     "customer": { Método do professor Joe
#         "name" : "Fulano",
#         "email" : "Fulano@gmail.com"
#     }
# }
# {
#     "email": "Fulanoo@gmail.com", Meu método
#     "id": 1,
#     "name": "Fulano"
# }


@app1.route('/customers', methods=['GET']) #Busca Geral
def get_customers():
    response = jsonify({'customers': customers}), 200

    return response
#Método do professor abaixo. Ao criar um novo cliente, utilizava uma formatação json que impedia de alterar o cliente depois, apenas incluindo na sequencia.
# @app1.route('/customers', methods=['POST'])#Cria cliente
# def new_customer():
#     request_data = request.get_json()
#     customer_data = request_data['customer']

#     customers.append({'id': customer_data['id'],'name': customer_data['name'], 'email': customer_data['email']})

#     return 'OK', 201
@app1.route('/customers', methods=['POST']) #Método que cria um cliente sem apontar indice.
def incluir_novo_customer():
    novo_customer = request.get_json()
    customers.append(novo_customer)

    return jsonify(customers)

@app1.route('/customers/<int:id>', methods=['GET']) #Busca cliente
def obter_customer_id(id):
    for customer in customers:
        if customer.get('id') == id:
            return jsonify(customer)
        
@app1.route('/customers/<int:id>', methods=['PUT']) #Altera cliente
def editar_customer_por_id(id):
    customer_alterado = request.get_json()
    for indice, customer in enumerate(customers):
        if customer.get('id') == id:
            customers[indice].update(customer_alterado)
            return jsonify(customers[indice])

@app1.route('/customers/<int:id>', methods=['DELETE'])# 
def excluir_customer(id):
    for indice, customer in enumerate(customers):
        if customer.get('id') == id:
            del customers[indice]

    return jsonify(customers)
#busca, alteração e remoção de cliente por id.


if __name__ == '__main__':
    
    app1.run(host="localhost", port="5000", debug=True)