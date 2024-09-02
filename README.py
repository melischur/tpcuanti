# tpcuanti
# Pseudocódigo:
# 1. Leer el archivo CSV y extraer los datos.
# 2. Procesar los datos para obtener el número de llamados por mes.
# 3. Calcular el porcentaje de llamados por mes.
# 4. Generar un gráfico de barras con los datos procesados.

import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Button, filedialog

# Título de la aplicación
st.title('Análisis y Visualización de Datos')

# Cargar y mostrar archivo CSV
uploaded_file_csv = st.file_uploader("Elige un archivo CSV", type="csv", key="csv")

def leer_datos(archivo):
    # Leer el archivo CSV
    datos = pd.read_csv(archivo)
    return datos

def procesar_datos(datos):
    # Convertir la columna de fecha a datetime
    datos['fecha'] = pd.to_datetime(datos['fecha'])
    # Agrupar por mes y contar los llamados
    llamados_por_mes = datos.groupby(datos['fecha'].dt.to_period('M')).size()
    # Calcular el porcentaje de llamados por mes
    total_llamados = llamados_por_mes.sum()
    porcentaje_llamados = (llamados_por_mes / total_llamados) * 100
    return porcentaje_llamados

def generar_grafico(porcentaje_llamados):
    # Generar el gráfico de barras
    porcentaje_llamados.plot(kind='bar')
    plt.xlabel('Mes')
    plt.ylabel('Porcentaje de Llamados')
    plt.title('Porcentaje de Llamados por Casos COVID por Mes')
    plt.show()

def cargar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if archivo:
        datos = leer_datos(archivo)
        porcentaje_llamados = procesar_datos(datos)
        generar_grafico(porcentaje_llamados)

def main():
    root = Tk()
    root.title("Cargar Archivo CSV")
    boton_cargar = Button(root, text="Cargar Archivo CSV", command=cargar_archivo)
    boton_cargar.pack(pady=20)
    root.mainloop()

if __name__ == '__main__':
    main()
