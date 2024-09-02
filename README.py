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

# Cargar los datos usando la función leer_datos
datos = leer_datos('ruta_al_archivo/archivo.csv')  # Reemplaza con la ruta correcta

# Verificar si la columna 'FECHA' existe
if 'FECHA' in datos.columns:
    # Convertir la columna 'FECHA' a formato datetime
    try:
        datos['FECHA'] = pd.to_datetime(datos['FECHA'], format='%d%b%Y:%H:%M:%S', errors='coerce')
    except Exception as e:
        st.error(f"Error al convertir la columna 'FECHA' a datetime: {e}")
else:
    st.error("La columna 'FECHA' no se encuentra en los datos.")

# Crear una nueva columna para el mes
if 'FECHA' in datos.columns and not datos['FECHA'].isnull().all():
    datos['MES'] = datos['FECHA'].dt.month
else:
    st.error("No se pudo crear la columna 'MES' debido a un problema con la conversión de 'FECHA'.")

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

# Mostrar la gráfica en Streamlit
st.pyplot(plt)

