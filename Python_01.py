# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 20:35:29 2022

@author: Iuri
"""

import mysql.connector
from mysql.connector import errorcode
import pandas as pd

try:
  cnx = mysql.connector.connect(user='root',password='',
                                database='baseteste')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  
  cursor = cnx.cursor()    
      
  add_user = ("INSERT INTO users "
                  "(username, password) "
                  "VALUES ('iuri', 'teste')")
  cursor.execute(add_user)
  cnx.commit()
       
  cursor.execute("SELECT * FROM users")
  resultusername = cursor.fetchall()
  df = pd.DataFrame(resultusername, columns=['id', 'username', 'password'])

 

 
  
  cnx.close()
