
from tabulate import tabulate
from datetime import datetime
from conexao_bd import integracao


class Cartao:
    def __init__(self, id_proprietario=None, credito_disponivel=None, tipo=None, data_emissao=None):
        self.__id_proprietario = id_proprietario
        self.__credito_disponivel = credito_disponivel
        self.__tipo = tipo
        self.__data_emissao = data_emissao

    #GETTER E SETTER DO ID DO PROPRIETÁRIO
    @property
    def id_proprietario(self):
        return self.__id_proprietario

    @id_proprietario.setter
    def id_proprietario(self, id_proprietario):
        self.__id_proprietario = id_proprietario

    # GETTER E SETTER DO CREDITOS DISPONIVEL
    @property
    def credito_disponivel(self):
        return self.__credito_disponivel

    @credito_disponivel.setter
    def credito_disponivel(self, credito_disponivel):
        self.__credito_disponivel = credito_disponivel

    # GETTER E SETTER DO TIPO DO CARTÃO
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    # GETTER E SETTER DA DATA DE EMISSÃO
    @property
    def data_emissao(self):
        return self.__data_emissao

    @data_emissao.setter
    def data_emissao(self, data_emissao):
        self.__data_emissao = data_emissao


    def exibe_cartoes(self):
        query = "SELECT * FROM [GRP-10/22].Jean_Amorim_cartao"
        response = integracao.cursor.execute(query)
        result = response.fetchall()
        if result:
            print('================================== Cartoes================================')
            print()
            print(tabulate(result,headers=['id_proprietario', 'Creditos', 'Tipo', 'Data_Emissao']))
        else:
            print('Cartao não encontrado.')

    def cadastrar_cartao(self):
        self.__id_proprietario = input("Insira o id de usuario: ").strip()
        self.__credito_disponivel = input("Insira a quantidade de creditos: ").strip()
        self.__tipo = input("Insira o tipo do cartao, EX: ['comun', 'estudante', 'idoso', ou 'vale-transporte'] ").strip().lower()
        self.__data_emissao = input("Insira a data de emissão do cartão EX:(2015-02-21): ").strip()

        query = f"""INSERT INTO [GRP-10/22].Jean_Amorim_cartao (
                 id_proprietario, creditos, tipo, data_emissao)
            VALUES(?,?,?,?)
            """
        def cartao_verificados():
            '''tratamentos de erros'''
            try:
                int(self.__id_proprietario)
            except:
                print(f"id_proprietario '{self.__id_proprietario}' é invalido, por favor digite um numero inteiro")
                return False

            try:
                float(self.__credito_disponivel)
            except:
                print(f"Creditos '{self.__credito_disponivel}' é inválido, por favor digite um numero inteiro.")
                return False

            try:
                datetime.strptime(self.__data_emissao, "%Y-%m-%d")
            except:
                print(f"data_emissao '{self.__data_emissao}' é invalida, por favor digite um data valida")
                return False


            tipos = ['comun', 'estudante', 'idoso', 'vale-transporte']
            if self.__tipo not in tipos:
                print('Opção invalida, insira um tipo de cartão válido.')
                return False

            return True

        if cartao_verificados():
            cartao = Cartao()
            cartao.id_proprietario = self.__id_proprietario
            cartao.tipo = self.__tipo
            cartao.data_emissao = self.__data_emissao
            cartao.credito_disponivel = self.__credito_disponivel

            integracao.cursor.execute(query, [cartao.id_proprietario, cartao.credito_disponivel, cartao.tipo, cartao.data_emissao])
            integracao.cursor.commit()
            print("Cartao registrado com sucesso.")
        
