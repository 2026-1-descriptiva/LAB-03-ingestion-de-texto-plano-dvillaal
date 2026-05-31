"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

from pprint import pprint
import pandas as pd
import re

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    with open("./files/input/clusters_report.txt") as file:
        file = open("files/input/clusters_report.txt", mode="r")
        
        titulo1 = file.readline()
        titulo1 = re.sub(r"\s{2,}", "-", titulo1).strip().split('-')

        titulo2 = file.readline()
        titulo2 = re.sub(r"\s{2,}", "-", titulo2).strip().split('-')

        columnas = [titulo1[0], titulo1[1]+ " "+titulo2[1], titulo1[2]+" "+titulo2[2], titulo1[3]]
        columnas = list(map(lambda x: x.lower().replace(" ", "_"), columnas))

        texto = file.readlines()

        texto_nuevo = "".join(texto[2:])

        filas = re.split(r"\n\s*\n", texto_nuevo.strip())
        
        filas = list(map(lambda x: re.sub(r"\s{3,}", "#", x).strip().split("#"), filas))
        
        filas_df = []
        for fila in filas:
            if len(fila) < 2:
                filas.remove(fila)
                continue
            if fila[0] == '': fila.pop(0)

            filas_df.append([fila[0].strip(), fila[1].strip(), fila[2].rstrip(" %").replace(",", "."), re.sub(r"\s{2,}", " ", ' '.join(fila[3:])).replace(".", "")])

        df = pd.DataFrame(filas_df, columns=columnas)
        df['cluster'] = df['cluster'].astype(int)
        

        df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].astype(int)
        df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].astype(float)

    return df

pregunta_01()
