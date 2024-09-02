# tpcuanti
# Pseudocódigo:
# 1. Leer el archivo CSV y extraer los datos.
# 2. Procesar los datos para obtener el número de llamados por mes.
# 3. Calcular el porcentaje de llamados por mes.
# 4. Generar un gráfico de barras con los datos procesados.

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Título principal de la aplicación
st.title("Análisis de casos Covid")

# Descripción de la aplicación
st.markdown("""
Esta aplicación permite cargar y analizar datos relacionados con los casos de COVID-19.
Puedes cargar tu propio archivo CSV y visualizar la distribución de casos por mes.
""")

def leer_datos(archivo):
    # Leer el archivo CSV
    datos = pd.read_csv(archivo)
    return datos

def procesar_datos(datos):
    # Convertir la columna 'FECHA' a formato datetime
    datos['FECHA'] = pd.to_datetime(datos['FECHA'], format='%d%b%Y:%H:%M:%S', errors='coerce')

    # Crear una nueva columna para el mes y año
    datos['MES'] = datos['FECHA'].dt.month

    # Asegúrate de seleccionar solo las columnas numéricas para la suma
    columnas_numericas = datos.select_dtypes(include=['number']).columns

    # Agrupar los datos por mes y sumar los valores de cada tipo de llamado
    llamados_por_mes = datos.groupby('MES')[columnas_numericas].sum()

    return llamados_por_mes

# Cargar archivo usando un botón en Streamlit
archivo_subido = st.file_uploader("Carga un archivo CSV", type=["csv"])

# Si el archivo es cargado, leer y procesar los datos
if archivo_subido is not None:
    datos = leer_datos(archivo_subido)
    st.write("Datos cargados correctamente. Procesando...")

    # Procesar los datos
    resultados = procesar_datos(datos)

    # Mostrar los resultados
    st.write(resultados)

    # Crear la gráfica
    st.write("Generando gráfica...")
    fig, ax = plt.subplots(figsize=(10, 6))
    resultados.plot(kind='bar', ax=ax)

    # Reemplazar los números de los meses por los nombres de los meses
    nombres_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
                     'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    ax.set_xticks(range(12))
    ax.set_xticklabels(nombres_meses, rotation=45)

    # Configurar la gráfica
    ax.set_title('Total de Llamados por Tipo y Mes')
    ax.set_xlabel('Mes')
    ax.set_ylabel('Número de Llamados')
    ax.legend(title='Tipo de Llamado')

    # Mostrar la gráfica en Streamlit
    st.pyplot(fig)
else:
    st.write("Por favor, carga un archivo CSV para continuar.")
