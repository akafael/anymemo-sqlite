#/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

#Tratamento de exceção explícito
try:
    #Conexão do Database
    con = lite.connect('test.db')
    #Objeto retornado pelo database
    cur = con.cursor()
    #Função para selecionar versão do SQLite
    cur.execute('SELECT SQLITE_VERSION()')
    #Fetch data
    data = cur.fetchone()
    #Mostra na tela
    print "SQLite version: %s" % data
#Caso encontre algum erro, tem isso:
except lite.Error, e:
    #Mensagem de erro e sai
    print "Error %s:" %e.args[0]
    sys.exit(1)
#Fechar arquivo
finally:
    if con:
        con.close()
