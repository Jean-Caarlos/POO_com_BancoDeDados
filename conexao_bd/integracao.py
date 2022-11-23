import pyodbc

# CONECTANDO O SQL COM O PYTHON
server = 'svr-estudos-v2.database.windows.net'
database = 'adb-estudos-v2'
username = 'jean.amorim@blueshift.com.br'
driver = '{ODBC Driver 18 for SQL Server}'
Authentication = 'ActiveDirectoryInteractive'
conexao = pyodbc.connect(
'DRIVER=' + driver + ';SERVER=' + server + ';AUTHENTICATION=' + Authentication + ';DATABASE=' + database + ';UID=' + username)
cursor = conexao.cursor()
print('conexao bem sucedida')
