import csv 
import json
import os

def cargar_dataset(ruta_documento):
    """
    Carga el dataset de un archivo CSV y lo devuelve como una lista de diccionarios.
    """
    columnas = []
    filas = []
    try:
        with open(ruta_documento, mode='r', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            columnas = lector.fieldnames if lector.fieldnames else []
            for fila in lector:
                filas.append(dict(fila))
        print(f"Dataset {ruta_documento} cargado correctamente.")
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_documento} no se encontró.")
    return columnas, filas

def guardar_resultado_csv(ruta_archivo, datos):
    """
    Funcionalidad Obligatoria 1: Implementar la función de exportación 
    y guardado de resultados en un archivo .csv.
    """
    if not datos:
        print("No hay datos para guardar.")
        return False

    try:
        if isinstance(datos[0], dict):
            campos = datos[0].keys()
            with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as f:
                escritor = csv.DictWriter(f, fieldnames=campos)
                escritor.writeheader()
                escritor.writerows(datos)
        else:
            with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as f:
                escritor = csv.writer(f)
                escritor.writerows(datos)
            print(f"Resultados guardados correctamente en {ruta_archivo}.")
            return True
    except Exception as e:
        print(f"Error al guardar el archivo {ruta_archivo}: {e}")
        return False

def guardar_resultado_json(ruta_archivo, datos):
    """
    Importar la función de exportación y guardado de resultados en un archivo .json.
    """

    try:
        with open(ruta_archivo, mode='w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
        print(f"Resultados guardados correctamente en {ruta_archivo}.")
        return True
    except Exception as e:
        print(f"Error al guardar el archivo {ruta_archivo}: {e}")
        return False
    
def cargar_resultado_anterior(ruta_archivo):
    """
    Función para abrir y leer los archivos guardados previamente.
    """
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo {ruta_archivo} no existe.")
        return None

    if ruta_archivo.endswith('.csv'):
        try:
            columnas, filas = cargar_dataset(ruta_archivo)
            print(f"Archivo CSV {ruta_archivo} cargado correctamente.")
            return {"columnas": columnas, "filas": filas}
        except Exception as e:
            print(f"Error al leer el archivo CSV {ruta_archivo}: {e}")
            return None 
    elif ruta_archivo.endswith('.json'):
        try:
            with open(ruta_archivo, mode='r', encoding='utf-8') as f:
                datos = json.load(f)
            print(f"Archivo JSON {ruta_archivo} cargado correctamente.")
            return datos
        except Exception as e:
            print(f"Error al leer el archivo JSON {ruta_archivo}: {e}")
            return None
    else:
        print(f"Error: El archivo {ruta_archivo} no tiene una extensión válida (.csv o .json).")
        return None