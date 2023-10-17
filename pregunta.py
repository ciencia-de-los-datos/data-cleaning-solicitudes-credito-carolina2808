"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime

def clean_data():

    def normalizar_fecha(fecha):
        try:
            # Intenta analizar la fecha en diferentes formatos
            formatos = ['%Y/%m/%d', '%d/%m/%Y', '%y/%m/%d', '%d/%m/%y']
            for formato in formatos:
                try:
                    fecha_obj = datetime.strptime(fecha, formato)
                    return fecha_obj.strftime('%d/%m/%Y')
                except ValueError:
                    pass  # Formato no coincide
            raise ValueError('Formato de fecha no reconocido')
        except ValueError as e:
            print(f"Error: {e}")
            return None

    # Lectura de la base de datos
    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)
    df.reset_index(inplace=True,drop=True)
    
    # Checkeo de la fecha
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(normalizar_fecha)
    
    # Botando los duplicados y los faltantes
    df.dropna(axis='index',inplace=True)
    df.drop_duplicates(inplace=True)

    # Checkeo de minusculas
    df['sexo'] = df['sexo'].str.lower().astype(str).str.strip()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower().astype(str)
    df['idea_negocio'] = df['idea_negocio'].str.lower().astype(str)
    df['barrio'] = df['barrio'].str.lower().astype(str)
    df['línea_credito'] = df['línea_credito'].str.lower().astype(str)
     
    # Checkeo de espacios en blanco y guiones
    df['idea_negocio'] = df['idea_negocio'].str.replace('_',' ').str.replace('-',' ').str.strip()
    df['barrio'] = df['barrio'].str.replace('_','-').str.replace('-',' ')
    df['línea_credito'] = df['línea_credito'].str.replace('_',' ').str.replace('-',' ').str.strip()

    # Limpieza de caracteres en la variable monetaria
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',','').str.replace('$','',regex=False).str.replace(' ','').str.strip().astype(float)   

    # Depuramos duplicados y faltantes resultantes tras la limpieza
    df.drop_duplicates(inplace=True)
    df.dropna(axis='index',inplace=True)
    return df


