from tabulate import tabulate
from datetime import datetime
from conexao_bd import integracao


class Onibus:
    def __init__(self, id_motorista=None, placa=None, numero_linha=None, modelo=None, ano_fabricacao=None):
        self.__id_motorista = id_motorista
        self.__placa = placa
        self.__numero_linha = numero_linha
        self.__modelo = modelo
        self.__ano_fabricacao = ano_fabricacao

    # GETTER E SETTER DA PLACA DO ONIBUS
    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    # GETTER E SETTER DO ID DO NUMERO DA LINHA
    @property
    def numero_linha(self):
        return self.__numero_linha

    @numero_linha.setter
    def numero_linha(self, numero_linha):
        self.__numero_linha = numero_linha

    # GETTER E SETTER DO MODELO DO ONIBUS
    @property
    def modelo_onibus(self):
        return self.__modelo

    @modelo_onibus.setter
    def modelo_onibus(self, modelo):
        self.__modelo = modelo

    # GETTER E SETTER DO ANO DE FABRICAÇÃO
    @property
    def ano_fabricacao(self):
        return self.__ano_fabricacao

    @ano_fabricacao.setter
    def ano_fabricacao(self, ano_fabricacao):
        self.__ano_fabricacao = ano_fabricacao

    # GETTER E SETTER DO ID DO MOTORISTA
    @property
    def id_motorista(self):
        return self.__id_motorista

    @id_motorista.setter
    def id_motorista(self, id_motorista):
        self.__id_motorista = id_motorista

    def exibe_onibus(self):
        query = "SELECT * FROM [GRP-10/22].Jean_Amorim_onibus"
        response = integracao.cursor.execute(query)
        result = response.fetchall()
        if result:
            print('================================== Onibus ================================')
            print()
            print(tabulate(result, headers=['Id_Motorista', 'Placa', 'Numero_Linha', 'Modelo', 'Ano_fabricacao']))
        else:
            print('Onibus não encontrado.')

    def cadastrar_onibus(self):
        self.__id_motorista = input("Insira o id do motorista: ").strip()
        self.__placa = input("Insira o numero da placa do onibus: ").strip()
        self.__numero_linha = input("Insira o numero da linha: ").strip()
        self.__modelo = input("Insira o modelo do onibus: ").strip().lower()
        self.__ano_fabricacao = input("Insira o ano de fabricação do onibus EX:(2015-02-21): ").strip()


        '''tratamentos de erros'''
        try:
            int(self.__id_motorista)
        except:
            print(f"Id_Motorista '{self.__id_motorista}' é invalido, por favor digite um numero inteiro")
            return False

        try:
            int(self.__placa)
        except:
            print(f"PLACA '{self.__placa}' é invalido, por favor digite um numero valido")
            return False

        try:
            int(self.__numero_linha)
        except:
            print(f"Numero_linha '{self.__numero_linha}' é invalido, por favor digite um numero inteiro")
            return False

        while True:
            if self.__modelo == '' or self.__modelo.isnumeric() == True:
                print(f"Modelo '{self.__modelo}' é invalido, por favor digite um nome valido")
                self.__modelo = input("Insira o Modelo: ").strip().lower()
            else:
                break

        try:
            datetime.strptime(self.__ano_fabricacao, "%Y-%m-%d")
        except:
            print(f"Ano_fabricação '{self.__ano_fabricacao}' é inválido, por favor digite uma data valida.")
            return False


        onibus = Onibus(self.__id_motorista, self.__placa, self.__numero_linha, self.__modelo, self.__ano_fabricacao)
        query = f"""
                INSERT INTO [GRP-10/22].Jean_Amorim_onibus (
                    id_motorista, placa, numero_linha, modelo, ano_fabricacao)
                VALUES(?,?,?,?,?)
                """
        integracao.cursor.execute(query, [onibus.id_motorista, onibus.placa, onibus.numero_linha, onibus.modelo_onibus, onibus.ano_fabricacao])
        integracao.cursor.commit()
        print("Onibus registrado com sucesso.")
