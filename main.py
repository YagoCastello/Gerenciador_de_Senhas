import sqlite3

Master_Password = '123456'

senha = input('Insira sua senha master: ')
if senha != Master_Password:
    print('Senha inválida! Encerrando ...')
    exit()