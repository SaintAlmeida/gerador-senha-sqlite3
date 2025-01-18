import sqlite3 as sq

senha_root = 'ALmeida@2022'

conn = sq.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS users (
               service TEXT NOT NULL,
               username TEXT NOT NULL,
               password TEXT NOT NULL
               

               );
               ''')



def menu():
    print('****************************')
    print('* i : Inserir Nova Senha *')
    print('* l : Listar Serviços Salvos *')
    print('* r : Recuperar uma senha *')
    print('* s : sair *')
    print('****************************')

    while True: 
        menu()
        op = input('O que deseja fazer?: ')
        if op not in ['i','l','r','s']:
            print('Opção Inválida')
            continue

        if op == 's':
          break

conn.close()