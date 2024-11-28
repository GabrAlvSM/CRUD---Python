import sys
sys.path.append('/home/user/Documents/PYOO')

# from DB.Database import Database
from Entity.Cliente import Cliente

cli1 = Cliente()

clientes = cli1.selecionar()
for cliente in clientes:
    print(cliente)

print("Atualizar dados do cliente: ")
id_selecao = int(input("Digite o ID: "))

cliente_selecionado = list(cli1.selecionar_por_id(id_selecao))



print(cliente_selecionado)

# print("Atualizar cliente")
# id_selecao = int(input("Digite o ID: "))

# cli1.nome = input("Digite seu nome: ")
# cli1.cpf = input("Digite seu CPF:")
# cli1.login = input("Digite seu login: ")
# cli1.senha = input("Digite sua senha: ")
# cli1.telefone = input("Digite seu telefone: ")
# cli1.cidade = input("Digite sua cidade: ")
# cli1.estado = input("Digite seu estado: ")



# DELETAR

# print("\nDeseja deletar algum usuário? ")
# id_deletar = int(input("Informe o ID do cliente: "))
# cliente_deletado = cli1.delete(id_deletar)

# if cliente_deletado == True:
#     print("Cliente deletado com sucesso! ")
#     clientes = cli1.selecionar()
#     for cliente in clientes:
#         print(cliente)

# cadastro = cli1.cadastrar()
# if cadastro == True:
#     print("Front: Cliente cadastrado com sucesso!")



# CADASTRAR

# print("Cadastrar novo cliente: ")
# cli1.nome = input("Digite seu nome: ")
# cli1.cpf = input("Digite seu CPF:")
# cli1.login = input("Digite seu login: ")
# cli1.senha = input("Digite sua senha: ")
# cli1.telefone = input("Digite seu telefone: ")
# cli1.cidade = input("Digite sua cidade: ")
# cli1.estado = input("Digite seu estado: ")


# banco = Database()

# dados = banco.select_cliente()

# print("Clientes Cadastrados: ")
# for item in dados:
#     print(item)
