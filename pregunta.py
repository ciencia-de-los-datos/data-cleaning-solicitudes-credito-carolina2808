"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():
    # Lee el archivo CSV
    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    # Elimina filas duplicadas, si las hay
    df.drop_duplicates(inplace=True)

    # Manejo de datos faltantes (NaN)
    
    df.dropna(inplace=True)
    
    # df.fillna(0, inplace=True)

    
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], format='%d/%m/%Y', errors='coerce')

    
    df['monto_del_credito'] = pd.to_numeric(df['monto_del_credito'], errors='coerce')
    df['estrato'] = pd.to_numeric(df['estrato'], errors='coerce')

    

    return df
