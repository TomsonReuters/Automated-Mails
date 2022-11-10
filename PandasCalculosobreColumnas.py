import openpyxl
import pandas as pd

#Cambiar esta linea segun sea apropiado
Excelworkbook = openpyxl.load_workbook('c:/misexcel/miarchivoexcel.xlsx')
Excelsheet=Excelworkbook.active

#obtener los titulos
titulos = next(Excelsheet.values)[0:]

#Convertir a Dataframe
dataframe_clientesbanco=pd.DataFrame(Excelsheet.values,columns=titulos)

#Quiero un sub dataset, solo con las columnas que me interesan
#Como tengo los titulos , ya puedo llamarlas por su nombre
mi_lista_columnas=['GASTRONOMIA','INGRESOS','PROVINCIA','Sexo','EDAD','Estado Civil']

lista_categorias=['SUPERMERCADO','GASTRONOMIA','ART_HOGAR','EST_SERVICIO','INDUMENTARIA', \
                  'TRANSPORTE','TURISMO','AUTOMOVIL','HOTELES','SERVICIOS','GEST_COMP_INTERNET',\
                      'CONSTRUCCION','DEPORTES','CINE_TEATR_ESP','EDUCACION','MASCOTAS','SALUD']

#filtrar dataframes por lista de columnas    
dataframe_clientes_subset=dataframe_clientesbanco[mi_lista_columnas]
dataframe_categorias=dataframe_clientesbanco[lista_categorias]

#Y ya puedo borrar la primera fila, ya tengo los titulos
dataframe_clientes_subset=dataframe_clientes_subset.drop(dataframe_clientes_subset.index[0])
dataframe_categorias=dataframe_categorias.drop(dataframe_categorias.index[0])


#Uso de funciones estadisticas basicas contra columnas de datasets
print("Gasto max en Servicios: ",dataframe_categorias['SERVICIOS'].max())
print("Edad promedio clientes: ",dataframe_clientes_subset['EDAD'].mean())


#Dos maneras de aplicar funciones estadisticas a filtros por colunas
#La primera de abajo es la manera "larga"
#La otra usa el encadenamiento de funciones (cada funcion devuelve un dataframe)

# sexo_df=dataframe_clientesbanco['Sexo']
# sexo_df=sexo_df[sexo_df=="Femenino"]
# mujeres=sexo_df.count()
# print("Cantidad mujeres: ",mujeres)

sexo_df=dataframe_clientesbanco['Sexo']
mujeres=sexo_df[sexo_df=="Femenino"].count()
print("Cantidad mujeres: ",mujeres)

#crear nueva columna Exchange Rate USDARS
ars_exchangerate=160
dataframe_clientes_subset["INGRESOS_USD"]=dataframe_clientes_subset["INGRESOS"]/ars_exchangerate
print(dataframe_clientes_subset)

#llenar columna Gastronomia con su promedio
promedio_gastronomia=dataframe_clientes_subset["GASTRONOMIA"].mean()

dataframe_clientes_subset["GASTRONOMIA"]=promedio_gastronomia

print(dataframe_clientes_subset["GASTRONOMIA"])
