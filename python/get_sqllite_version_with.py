#/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

#Conexão do Database
con = lite.connect('test.db')

with con:
    #Objeto retornado pela conexão com database
    cur = con.cursor()
    #Executa função para obter Versão do SQLite
    cur.execute('SELECT SQLITE_VERSION()')
    #Obtém dados
    data = cur.fetchone()
    print "SQLite version: %s" % data

#Usando "with", já é tratado exceções, erros e o fechamento do arquivo
