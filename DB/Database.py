# INSTALAR MYSQL CONNECTOR: 
# 
# sudp apt pip install
# sudo pip install mysql-connector-python

import mysql.connector

class Database():
    # DECLARAR O NOME DO BANCO
    def __init__(self, banco="sysphyton"): 
        self.banco = banco

    # INFORMA AS INFOMACOES NECESSARIAS PARA CONECTAR COM O BANCO
    def connect(self):
        self.conn = mysql.connector.connect(host='10.28.0.235', database=self.banco,user='devweb', password='suporte@22')

        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado com sucesso!", "server: "+db_info)
        else:
            print("Erro de conexão")

    # CRUD

    # CREATE - INSERT
    def insert_cliente(self, dados_cliente):
        self.connect()
        try:
            # INSERE OS DADOS NO BANCO
            self.cursor.execute('INSERT INTO cliente(nome,cpf,login,senha,telefone,cidade,estado) VALUES (%s,%s,%s,%s,%s,%s,%s);', dados_cliente)
            # COMITA PARA O BANCO DE DADOS --- EXTREMAMENTE IMPORTANTE
            self.conn.commit()
            print("Cliente cadastrado com sucesso!")

        # RETORNA O ERRO
        except Exception as err:
            print(err)

    #READ - SELECT
    def select_cliente(self):
        self.connect()
        try:
            self.cursor.execute('SELECT * FROM cliente')
            clientes = self.cursor.fetchall()
            return clientes

        # RETORNA O ERRO
        except Exception as err:
            print(err)

    #READ - SELECT BY ID
    def select_cliente_by_id(self, id):
        self.connect()
        try:
            self.cursor.execute(f'SELECT * FROM cliente WHERE id = {id}')
            cliente = self.cursor.fetchone()
            return cliente

        # RETORNA O ERRO
        except Exception as err:
            print(err)

        # ENCERRA CONEXAO COM O BANCO
        finally:
            self.close_connection()


    #UPDATE - UPDATE
    def update_cliente_by_id(self, id):
        self.connect()
        try:
            cliente = list(self.select_cliente_by_id(id))

            cliente[1] = input("Digite o novo nome: ")
            cliente[2] = input("Digite o novo cpf: ")
            cliente[3] = input("Digite o novo login: ")
            cliente[4] = input("Digite o novo senha: ")
            cliente[5] = input("Digite o novo telefone: ")
            cliente[6] = input("Digite o novo cidade: ")
            cliente[7] = input("Digite o novo estado: ")

            self.cursor.execute(f"""
                                    UPDATE cliente SET nome = '{cliente[1]}', 
                                                        cpf = '{cliente[2]}', 
                                                        login = '{cliente[3]}', 
                                                        senha = '{cliente[4]}', 
                                                        telefone = '{cliente[5]}', 
                                                        cidade = '{cliente[6]}', 
                                                        estado = '{cliente[7]}' 
                                                        WHERE id = {cliente[0]}
                                                    """)

            self.conn.commit()
            print("Cliente atualizado com sucesso!")
        
        # RETORNA O ERRO
        except Exception as err:
            print(err)
        
        # ENCERRA CONEXAO COM O BANCO
        finally:
            self.close_connection()

    #DELETE - DELETE
    def delete_client_by_id(self, id):
        self.connect()
        try:
            self.cursor.execute(f'DELETE FROM cliente WHERE id = {id}')
            self.conn.commit()
            return True

        # RETORNA O ERRO
        except Exception as err:
            print(err)

        # ENCERRA CONEXAO COM O BANCO
        finally:
            self.close_connection()

    # DESCONECTA DO BANCO
    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão encerrada com sucesso!")


if __name__ == '__main__':
    db = Database()
    # db.connect()
    # db.insert_cliente()
    # db.select_cliente()
    # db.select_cliente_by_id(2)
    # db.update_cliente_by_id(7)
    # db.delete_client_by_id(2)
    # db.close_connection()