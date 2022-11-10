import sqlite3
import pandas as pd

#Crear la DB

con = sqlite3.connect('StockTest.db')

#Leer archivo con ruta especifica
wb = pd.read_excel('/Users/tom/Desktop/StockDB.xlsx',sheet_name = None)

#Añadirla a SQL
for sheet in wb:
    wb[sheet].to_sql(sheet,con,index=False)
con.commit()
con.close()

