import sys
sys.path.append('/home/user/Documents/PYOO')
from DB.Database import Database

class Cliente:

    def __init__(self):
        self.nome = None
        self.cpf = None
        self.login = None
        self.senha = None
        self.telefone = None
        self.cidade = None
        self.estado = None
        self.banco = Database()

    def getNome(self):
        return self.nome
    
    def cadastrar(self):
        dados_cliente = (self.nome, self.cpf, self.login, self.senha, self.telefone, self.cidade, self.estado)
        # envia os dados da tupla para a funcao de inserir clientes
        self.banco.insert_cliente(dados_cliente)
        cadastro = self.banco.insert_cliente(dados_cliente)
        return cadastro

    def selecionar(self):
        # chama a funcao de listar clientes
        clientes = self.banco.select_cliente()
        return clientes
    
    def selecionar_por_id(self, id):
        # chama a funcao de listar clientes
        clientes = self.banco.select_cliente_by_id(id)
        return clientes
    
    def atualizar(self, lista):
        atualizado = self.banco.update_cliente_by_id(lista[0])
        return atualizado

    def delete(self, id):
        # chama a funcao de deletar cliente por id
        excluir = self.banco.delete_client_by_id(id)
        return excluir       