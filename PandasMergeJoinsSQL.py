
#Netflix Dataset https://www.kaggle.com/shivamb/netflix-shows
#append, merge (joins en SQL)

import pandas as pd

#Ruta hacia el archivo

netflix=pd.read_csv("C:/misexcel/datasets/netflix.csv")
netflix_df=pd.DataFrame(netflix)

imdb=pd.read_csv("C:/misexcel/datasets/IMDB/IMDb movies.csv")
imdb_df=pd.DataFrame(imdb)

#####COPIAR DATAFRAME Y PEGARLO EN OTRO LADO
#copia 2 
#netflix2=netflix_df

#altero el original
#netflix_df=netflix_df['title']

#la copia no cambio
#print(netflix2)
#print(netflix_df)


#### Combinando dataframes con append()#####
#Cortamos el dataset en 2 para luego mostrar como unirlos
#primeras 10 filas
netflix_df_head10=netflix_df[["title","listed_in"]].head(10)

#ultimas 10 filas
netflix_df_tail10=netflix_df[["title","listed_in"]].tail(10)

#append me permite "pegar" uno o mas dataframes
#abajo del otro 
netflix_combinado=netflix_df_head10.append(netflix_df_tail10)

netflix_combinado2=netflix_df_head10.append(    \
    [netflix_df_tail10,netflix_df_head10]     \
    )

##pegando columnas (o "series" en lenguaje Pandas)
# #solo una columna  especifica,por nombre
mi_columna=netflix_df['title']

netflix_combinado2=netflix_combinado2.append(mi_columna)

print(netflix_combinado2)

# #solo una columna  especifica,por coordenadas de celdas
# netflix_titles=netflix_df_short.iloc[0:,1]

# #combinandos un rango en la fila,
# # y un indice negativo (inverso) en la columna
# netflix_titles=netflix_df_short.iloc[0:3,-1]

# #indices por nombre de columna con la funcion loc()
# netflix_titles=netflix_df.loc[[0,1,2],"title":"director"]


# #titulos en las filas tambien
# titulo_filas=["fila1","fila2","fila3"]

# #creo un dataset de 3 filas
# netflix_df_3filas=netflix_df_short=netflix_df[["title","listed_in"]].head(3)

# #En Pandas las filas son el index , y las columnas columns...
# netflix_df_3filas.index=titulo_filas

# #usando la funcion loc() para acceder a celdas 
# #por nombre de fila y columna
# netflix_df_3filas=netflix_df_3filas.loc["fila1","title"]

# #Usando el simbolo :  para indicar TODAS las filas o columnas
# netflix_titles=netflix_df.loc[:,"title":"director"]

# #Todo el dataframe
# netflix_titles=netflix_df.loc[:,:]

# #print(netflix_titles)

# #Usando el identificador unico de Netflix como titulo de fila
# netflix_df.set_index("show_id",inplace=True)

# # Traer todo el catalogo de Netflix desde el id 70234439 
# #hasta el final, pero solo con la columna title
# #luego solo guardar los primeros 5 resultados 
# netflix_df=netflix_df.loc["70234439":,"title"].head(5)
# print(netflix_df)


