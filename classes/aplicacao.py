from usuario import Usuario
from onibus import Onibus
from motorista import Motorista
from cartao import Cartao

usuario = Usuario()
onibus = Onibus()
cartao = Cartao()
motorista = Motorista()


print(' ====================================================================================')
print(' =================================== Bem-Vindo a CadUni =============================')
print(' ====================================================================================')

while True:
    resp = input('''
    Escolha a opção desejada!
    1 - Registrar Usuario
    2 - Visualizar Usuario
    3 - Registrar cartoes
    4 - Visualizar cartoes
    5 - Registrar motorista
    6 - Visualizar motorista
    7 - Registrar Onibus 
    8 - Visualizar Onibus
    9 - Fechar o programa
    > ''')

    if resp == '1':
        usuario.cadastrar_usuario()

    elif resp == '2':
        usuario.exibe_usuario()

    elif resp == '3':
        cartao.cadastrar_cartao()

    elif resp == '4':
        cartao.exibe_cartoes()

    elif resp == '5':
        motorista.cadastrar_motorista()

    elif resp =='6':
        motorista.exibe_motorista()
        
    elif resp == '7':
        onibus.cadastrar_onibus()

    elif resp == '8':
        onibus.exibe_onibus()

    elif resp == '9':
        print('Programa finalizado')
        break

    else:
        print('Erro! Insira uma opção válida.')



