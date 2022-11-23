import pyodbc

# CONECTANDO O SQL COM O PYTHON
server = 'server'
database = 'database'
username = 'username@blueshift.com'
driver = '{ODBC Driver for SQL Server}'
Authentication = 'ActiveDirectoryInteractive'
conexao = pyodbc.connect(
'DRIVER=' + driver + ';SERVER=' + server + ';AUTHENTICATION=' + Authentication + ';DATABASE=' + database + ';UID=' + username)
cursor = conexao.cursor()
print('conexao bem sucedida')
