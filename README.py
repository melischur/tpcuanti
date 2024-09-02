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
    # Convertir la columna 'FECHA' a formato datetime
    datos['FECHA'] = pd.to_datetime(datos['FECHA'], format='%d%b%Y:%H:%M:%S', errors='coerce')

    # Crear una nueva columna para el mes y año
    datos['MES'] = datos['FECHA'].dt.month

    # Asegúrate de seleccionar solo las columnas numéricas para la suma
    columnas_numericas = datos.select_dtypes(include=['number']).columns

    # Agrupar los datos por mes y sumar los valores de cada tipo de llamado
    llamados_por_mes = datos.groupby('MES')[columnas_numericas].sum()

    # Crear la gráfica
    llamados_por_mes.plot(kind='bar', figsize=(10, 6))

    # Reemplazar los números de los meses por los nombres de los meses
    nombres_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
                     'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    plt.xticks(ticks=range(1, 13), labels=nombres_meses, rotation=45)

    # Configurar la gráfica
    plt.title('Total de Llamados por Tipo y Mes')
    plt.xlabel('Mes')
    plt.ylabel('Número de Llamados')
    plt.legend(title='Tipo de Llamado')
    plt.tight_layout()

    # Mostrar la gráfica
    plt.show()

# Ejemplo de uso
archivo = 'ruta_al_archivo.csv'  # Reemplaza con la ruta correcta
datos = leer_datos(archivo)
procesar_datos(datos)

