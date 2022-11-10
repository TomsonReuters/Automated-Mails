
import pandas as pd

#DUPLICADOS EN DATASETS

#Creando un dataframe sin importar dataset
#La clave o categoria, representa la columna
# y dentro de cada una hay una lista de valores que van en esa columna
alumnos_df = pd.DataFrame({

    'nombre': ['Santino', 'Santino', 'Clara', 'Clara', 'Florencia'],

    'barrio': ['Palermo', 'Palermo', 'Belgrano', 'Belgrano', 'Flores'],

    'promedio': [7, 7, 5, 5, 10]

})

##eliminar duplicados
alumnos_df=alumnos_df.drop_duplicates()

#Ejemplo 2
alumnos_df = pd.DataFrame({

    'nombre': ['Santino', 'Santino', 'Santino', 'Clara', 'Florencia'],

    'barrio': ['Palermo', 'Palermo', 'Belgrano', 'Belgrano', 'Flores'],

    'promedio': [7, 7, 7, 5, 10]

})
#print (alumnos_df)

##Eliminar duplicados
alumnos_df=alumnos_df.drop_duplicates()

#Ejemplo 3 sin repetir barrios
alumnos_df = pd.DataFrame({

    'nombre': ['Santino', 'Santino', 'Santino', 'Clara', 'Florencia'],

    'barrio': ['Palermo', 'Palermo', 'Belgrano', 'Belgrano', 'Flores'],

    'promedio': [7, 7, 7, 5, 10]

})

##Eliminar duplicados
alumnos_df=alumnos_df.drop_duplicates(subset=['barrio'])

print (alumnos_df)

