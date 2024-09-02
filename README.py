# tpcuanti
# Pseudocódigo:
# 1. Leer el archivo CSV y extraer los datos.
# 2. Procesar los datos para obtener el número de llamados por mes.
# 3. Calcular el porcentaje de llamados por mes.
# 4. Generar un gráfico de barras con los datos procesados.

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def leer_datos(archivo):
    # Leer el archivo CSV
    datos = pd.read_csv(archivo)
    return datos

def procesar_datos(datos):
    # Verificar si la columna 'fecha' existe en el DataFrame
    if 'fecha' in datos.columns:
        try:
            # Intentar convertir la columna 'fecha' a formato datetime
            datos['fecha'] = pd.to_datetime(datos['fecha'])
        except Exception as e:
            st.error(f"Error al convertir la columna 'fecha' a datetime: {e}")
    else:
        st.warning("La columna 'fecha' no se encuentra en los datos.")
        # Opcional: Manejar la ausencia de la columna 'fecha'
        # Por ejemplo, podrías crear una columna 'fecha' vacía o con valores predeterminados
        # datos['fecha'] = pd.NaT  # NaT significa "Not a Time" en pandas

    # Resto de la lógica de procesamiento
    return datos

def generar_grafico(porcentaje_llamados):
    # Generar el gráfico de barras
    fig, ax = plt.subplots()
    porcentaje_llamados.plot(kind='bar', ax=ax)
    ax.set_xlabel('Mes')
    ax.set_ylabel('Porcentaje de Llamados')
    ax.set_title('Porcentaje de Llamados por Casos COVID por Mes')
    st.pyplot(fig)

def main():
    st.title("Análisis de casos COVID 2021")
    archivo = st.file_uploader("Cargar Archivo CSV", type="csv")
    
    if archivo is not None:
        datos = leer_datos(archivo)
        porcentaje_llamados = procesar_datos(datos)
        generar_grafico(porcentaje_llamados)

if __name__ == '__main__':
    main()
