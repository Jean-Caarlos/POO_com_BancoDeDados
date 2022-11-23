from tabulate import tabulate
from datetime import datetime
from conexao_bd import integracao


class Motorista:
    def __init__(self, nome=None, sobrenome=None, cnh=None, data_nascimento=None):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cnh = cnh
        self.__data_nascimento = data_nascimento

    # GETTER E SETTER DO NUMERO DA CNH
    @property
    def cnh(self):
        return self.__cnh

    @cnh.setter
    def cnh(self, cnh):
        self.__cnh = cnh

    # GETTER E SETTER DO NOME
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome= nome

    # GETTER E SETTER DO SOBRENOME
    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    # GETTER E SETTER DA DATA DE NASCIMENTO
    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento


    def exibe_motorista(self):
        query = "SELECT * FROM [GRP-10/22].Jean_Amorim_motorista"
        response = integracao.cursor.execute(query)
        result = response.fetchall()
        if result:
            print('================================== Motorista ================================')
            print()
            print(tabulate(result,headers=['CNH', 'Nome', 'Sobrenome', 'Data_Nascimento']))
        else:
            print('Motorista não encontrado.')

    def cadastrar_motorista(self):
        self.__nome = input("Insira o nome do motorista: ").strip()
        self.__sobrenome = input("Insira o sobrenome do motorista: ").strip()
        self.__cnh = input("Insira o numero da CNH: ").strip()
        self.__data_nascimento = input("Insira a data de nascimento do motorista EX:(2015-02-21): ").strip()


        '''tratamentos de erros'''
        try:
            int(self.__cnh)
        except:
            print(f"CNH '{self.__cnh}' é invalido, por favor digite um numero valido")
            return False

        try:
            datetime.strptime(self.__data_nascimento, "%Y-%m-%d")
        except:
            print(f"Data_Nascimento '{self.__data_nascimento}' é inválido, por favor digite uma data valida.")
            return False

        while True:
            if self.__nome == '' or self.__nome.isnumeric() == True:
                print(f"nome '{self.__nome}' é invalido, por favor digite um nome valido")
                self.__nome = input("Insira o Nome: ").strip().lower()

            elif self.__sobrenome == '' or self.__sobrenome == self.__nome or self.__sobrenome.isnumeric() == True:
                print(f"sobrenome '{self.__sobrenome}' é invalido, por favor digite um sobrenome valido")
                self.__sobrenome = input("Insira o Sobrenome: ").strip().lower()

            else:
                break

        motorista = Motorista(self.__nome, self.__sobrenome, self.__cnh, self.__data_nascimento)
        query = f"""
                    INSERT INTO [GRP-10/22].Jean_Amorim_motorista (
                         nome, sobrenome, cnh, data_nascimento)
                    VALUES(?,?,?,?)
                    """

        integracao.cursor.execute(query, [motorista.nome, motorista.sobrenome, motorista.cnh, motorista.data_nascimento])
        integracao.cursor.commit()
        print("Motorista registrado com sucesso.")