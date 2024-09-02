# tpcuanti
# Pseudocódigo:
# 1. Leer el archivo CSV y extraer los datos.
# 2. Procesar los datos para obtener el número de llamados por mes.
# 3. Calcular el porcentaje de llamados por mes.
# 4. Generar un gráfico de barras con los datos procesados.

import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Button, filedialog

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
            print(f"Error al convertir la columna 'fecha' a datetime: {e}")
    else:
        print("La columna 'fecha' no se encuentra en los datos.")
        # Opcional: Manejar la ausencia de la columna 'fecha'
        # Por ejemplo, podrías crear una columna 'fecha' vacía o con valores predeterminados
        # datos['fecha'] = pd.NaT  # NaT significa "Not a Time" en pandas

    # Resto de la lógica de procesamiento
    return datos

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
    root.title("Análisis de casos COVID 2021")
    boton_cargar = Button(root, text="Cargar Archivo CSV", command=cargar_archivo)
    boton_cargar.pack(pady=20)
    root.mainloop()

if __name__ == '__main__':
    main()
