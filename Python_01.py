# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 12:48:00 2022

@author: Iuri
"""



import mysql.connector
import pandas as pd


usuario = 'teste'
senha = 'teste'

con = mysql.connector.connect(host='localhost', database='usersdb',user='root',password='senha')

if con.is_connected():
    db_info = con.get_server_info()
    
    checkusername = con.cursor()
    checkusername.execute("SELECT * FROM users")
    resultusername = checkusername.fetchall()

        
    for record in resultusername:        
        if usuario == record[1]:
            print('Login Correto')
            if senha == record[2]:
                print('Senha Correta')
        
                    
df = pd.DataFrame(resultusername, columns=['id', 'usuario', 'senha'])                    