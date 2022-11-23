from tabulate import tabulate
from datetime import datetime
from conexao_bd import integracao


class Usuario:
    def __init__(self, nome=None, sobrenome=None, email=None, bairro=None, data_nascimento=None):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__bairro = bairro
        self.__data_nascimento = data_nascimento


    #GETTER E SETTER DE NOME
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
         self.__nome = nome

    # GETTER E SETTER DE SOBRENOME
    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    # GETTER E SETTER DE EMAIL
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    # GETTER E SETTER DE BAIRRO
    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    # GETTER E SETTER DE DATA_NASCIMENTO
    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    
    def exibe_usuario(self):
        query = "SELECT * FROM [GRP-10/22].Jean_Amorim_usuario"
        response = integracao.cursor.execute(query)
        result = response.fetchall()
        if result:
            print('================================== Usuario ================================')
            print()
            print(tabulate(result,headers=['Nome', 'Sobrenome', 'Email', 'Bairro', 'Data_Nascimento']))
        else:
            print('Usuario não encontrado.')

    def cadastrar_usuario(self):
        self.__nome = str(input("Insira o Nome: ")).strip().lower()
        self.__sobrenome = str(input("Insira o Sobrenome: ")).strip().lower()
        self.__email = input("Insira o E-mail: ").strip().lower()
        self.__bairro = input("Insira o Bairro: ").strip()
        self.__data_nascimento = input("Insira a data de nascimento EX:(2015-02-21): ").strip()



        '''tratamentos de erros'''
        while True:
            if self.__nome == '' or self.__nome.isnumeric() == True:
                print(f"nome '{self.__nome}' é invalido, por favor digite um nome valido")
                self.__nome = input("Insira o Nome: ").strip().lower()

            elif self.__sobrenome == '' or self.__sobrenome == self.__nome or self.__sobrenome.isnumeric() == True:
                print(f"sobrenome '{self.__sobrenome}' é invalido, por favor digite um sobrenome valido")
                self.__sobrenome = input("Insira o Sobrenome: ").strip().lower()

            elif self.__bairro == '' or self.__bairro.isnumeric() == True:
                print(f"bairro '{self.__bairro}' é invalido, por favor digite um bairro valido")
                self.__bairro = input("Insira o Bairro: ").strip().lower()
            else:
                break

        while True:
            pos_a = self.__email.find('@')
            servidor = self.__email[pos_a:]
            if pos_a != -1 and '.' in servidor:
                break
            else:
                print('E-mail invalido!')
                self.__email = input("Insira o E-mail: ").strip().lower()

        try:
            datetime.strptime(self.__data_nascimento, "%Y-%m-%d")
        except:
            print(f"Data_Nascimento '{self.__data_nascimento}' é inválido, por favor digite uma data valida.")
            return False



        usuario = Usuario(self.__nome, self.__sobrenome, self.__email, self.__bairro, self.__data_nascimento)
        query = f"""
                INSERT INTO [GRP-10/22].Jean_Amorim_usuario (
                    nome, sobrenome, email, bairro, data_nascimento)
                VALUES(?,?,?,?,?)
                    """
        integracao.cursor.execute(query, [usuario.nome, usuario.sobrenome, usuario.email, usuario.bairro, usuario.data_nascimento])
        integracao.cursor.commit()
        print("Usuario registrado com sucesso.")