import sqlite3
import pandas as pd

con = sqlite3.connect('StockTest.db')
wb = pd.read_excel('/Users/tom/Desktop/StockDB.xlsx',sheet_name = None)

for sheet in wb:
    wb[sheet].to_sql(sheet,con,index=False)
con.commit()
con.close()

