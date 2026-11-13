"""
DATALAB - EXPLORADOR DE GOLES DEL MUNDIAL (Entrega 2: Analizador)

División de Trabajo:
Integrante 1: carga del dataset con csv y guardado/lectura de archivos (archivos.py).
Integrante 2: historial de consultas (archivos.py).
Integrante 3: análisis y estructuras de datos (analisis.py).
Integrante 4: funcionalidad opcional: resumen del dataset (analisis.py).
Integrante 5: menú principal, integración y control de flujo (main.py).
Integrante 6: README, video, diagrama de flujo de datos y contribuciones.

Este archivo SOLO maneja la conversación con el usuario (menú, preguntas y
mensajes). Todo el análisis está en analisis.py y toda la lectura/escritura
de archivos está en archivos.py.
"""
import json
import os

import archivos
import analisis

RUTA_DATASET = "goals_completo.csv"   # dataset completo (200+ registros)
RUTA_RESPALDO = "goals_pequeno.csv"   # se usa solo si no existe el completo
RUTA_RESUMEN = "resumen.json"         # se genera solo al iniciar el programa

# Archivos que el usuario NO puede sobrescribir al guardar un resultado
ARCHIVOS_PROTEGIDOS = (RUTA_DATASET.lower(), RUTA_RESPALDO.lower(),
                       RUTA_RESUMEN.lower(), "historial.csv")


# ---------------------------------------------------------------
# Menú y preguntas básicas
# ---------------------------------------------------------------
def cargar_menu():
    """Imprime el menú principal en consola."""
    print("\n" + "=" * 55)
    print("   DATALAB - EXPLORADOR DE GOLES DEL MUNDIAL   ")
    print("=" * 55)
    print("1. Buscar registros por texto (Texto)")
    print("2. Ver estadísticas básicas del minuto de los goles")
    print("3. Agrupar goles por Selección (Categoría)")
    print("4. Analizar criterios del 'Mejor Equipo de la Historia'")
    print("5. Ver resumen del dataset")
    print("6. Recuperar un resultado guardado")
    print("7. Ver historial de Consultas")
    print("8. Salir")
    print("=" * 55)
    return True  # retorna True tras desplegar el menú en consola


def pedir_si_no(pregunta):
    """Pregunta hasta recibir s/n. Retorna True si el usuario responde que sí."""
    while True:
        respuesta = input(f"{pregunta} (s/n): ").strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print(" Responde con s o n.")


# ---------------------------------------------------------------
# Carga del dataset y resumen inicial
# ---------------------------------------------------------------
def cargar_datos():
    """Carga el dataset completo (o el pequeño si no existe). Retorna (columnas, filas)."""
    columnas, filas = archivos.cargar_dataset(RUTA_DATASET)
    if not filas:
        print(f" Aviso: se usará '{RUTA_RESPALDO}' porque no se pudo leer '{RUTA_DATASET}'.")
        columnas, filas = archivos.cargar_dataset(RUTA_RESPALDO)
    return columnas, filas


def generar_resumen_inicial(filas):
    """Genera el resumen del dataset y lo guarda en resumen.json. Retorna el resumen."""
    resumen = analisis.generar_resumen_dataset(filas)
    archivos.guardar_resultado_json(RUTA_RESUMEN, resumen)
    return resumen


# ---------------------------------------------------------------
# Guardar resultados (Funcionalidad obligatoria 1)
# ---------------------------------------------------------------
def pedir_ruta_guardado(sugerido, extension):
    """Pide el nombre del archivo. Retorna la ruta final o None si se cancela."""
    nombre = input(f" Nombre del archivo (Enter = {sugerido}{extension}): ").strip()
    if not nombre:
        nombre = sugerido

    # Se le quita cualquier extensión escrita y se pone la del formato elegido
    ruta = os.path.splitext(nombre)[0] + extension

    if ruta.lower() in ARCHIVOS_PROTEGIDOS:
        print(f" '{ruta}' es un archivo del programa y no se puede sobrescribir.")
        return None
    if os.path.exists(ruta) and not pedir_si_no(f" '{ruta}' ya existe. ¿Sobrescribir?"):
        return None
    return ruta


def preguntar_si_guardar(sugerido, tabla, datos):
    """
    Pregunta si se guarda el resultado en CSV o JSON.
    tabla: lista de diccionarios (para CSV, con encabezados).
    datos: lo que se escribe en JSON.
    """
    if not pedir_si_no("\n ¿Desea guardar este resultado en un archivo?"):
        return

    print(" Formato: 1. CSV   2. JSON")
    formato = input(" Elija el formato (1-2): ").strip()

    if formato == "1":
        ruta = pedir_ruta_guardado(sugerido, ".csv")
        if ruta:
            archivos.guardar_resultado_csv(ruta, tabla)
    elif formato == "2":
        ruta = pedir_ruta_guardado(sugerido, ".json")
        if ruta:
            archivos.guardar_resultado_json(ruta, datos)
    else:
        print(" Formato no válido. No se guardó nada.")


# ---------------------------------------------------------------
# Convertir resultados a tablas (listas de diccionarios) para guardarlos
# ---------------------------------------------------------------
def ranking_a_tabla(ranking, nombre_equipo, nombre_valor):
    """Convierte [(equipo, valor), ...] en [{'posicion':1, nombre_equipo:..., nombre_valor:...}, ...]."""
    return [{"posicion": i, nombre_equipo: equipo, nombre_valor: valor}
            for i, (equipo, valor) in enumerate(ranking, start=1)]


# ---------------------------------------------------------------
# Opciones del menú
# ---------------------------------------------------------------
def opcion_buscar(columnas, filas):
    """Opción 1: búsqueda por texto. Buscar_Texto ya registra cada búsqueda en el historial."""
    print("\n--- BÚSQUEDA POR TEXTO ---")
    encontradas = analisis.Buscar_Texto(columnas, filas)  # diccionarios de la última búsqueda
    if encontradas:
        print(f"\n Última búsqueda: {len(encontradas)} registros.")
        preguntar_si_guardar("busqueda", encontradas, encontradas)


def opcion_estadisticas(columnas, filas):
    """Opción 2: estadísticas básicas del minuto del gol."""
    print("\n--- ESTADÍSTICAS BÁSICAS DEL MINUTO DE REGULACIÓN ---")
    resultado = analisis.estadisticas_basicas(columnas, filas)
    if resultado is None:  # no hubo datos o faltó la columna
        return
    minimo, maximo, promedio = resultado
    datos = {"minimo": minimo, "maximo": maximo, "promedio": round(promedio, 2)}

    archivos.registrar_consulta("estadísticas minuto de gol", 1)
    preguntar_si_guardar("estadisticas", [datos], datos)


def opcion_agrupar(columnas, filas):
    """Opción 3: goles por selección."""
    print("\n--- AGRUPACIÓN POR SELECCIÓN (CATEGORÍA) ---")
    ranking = analisis.agrupar_goles_por_seleccion(columnas, filas)
    if not ranking:
        return
    tabla = ranking_a_tabla(ranking, "seleccion", "goles")

    archivos.registrar_consulta("goles por selección", len(ranking))
    preguntar_si_guardar("goles_por_seleccion", tabla, tabla)


def opcion_mejor_equipo(columnas, filas):
    """Opción 4: mejor equipo de la historia (el submenú está en analisis.py)."""
    print("\n--- ANÁLISIS CRITERIOS MEJOR EQUIPO DE LA HISTORIA ---")
    resultado = analisis.mejor_equipo(columnas, filas)  # última consulta o None
    if resultado is None:  # el usuario volvió sin consultar nada
        return
    tabla = ranking_a_tabla(resultado["ranking"], "equipo", "valor")
    for fila in tabla:
        fila["criterio"] = resultado["criterio"]
    datos = {"criterio": resultado["criterio"],
             "mejores": resultado["mejores"],
             "ranking": ranking_a_tabla(resultado["ranking"], "equipo", "valor")}

    archivos.registrar_consulta("mejor equipo por " + resultado["criterio"],
                                len(resultado["ranking"]))
    preguntar_si_guardar("mejor_equipo", tabla, datos)


def opcion_resumen(resumen):
    """Opción 5: muestra el resumen generado al iniciar (ya está guardado en resumen.json)."""
    print("\n--- RESUMEN DEL DATASET ---")
    print(f" Total de registros       : {resumen['total_registros_procesados']}")
    print(f" Selecciones únicas       : {resumen['total_selecciones_unicas']}")
    print(f" Minuto del gol (máximo)  : {resumen['estadisticas_minuto_gol']['maximo']}")
    print(f" Minuto del gol (mínimo)  : {resumen['estadisticas_minuto_gol']['minimo']}")
    print(f" Minuto del gol (promedio): {resumen['estadisticas_minuto_gol']['promedio']}")
    print(f" (Guardado automáticamente en {RUTA_RESUMEN})")
    archivos.registrar_consulta("resumen del dataset", 1)


def mostrar_recuperado(datos):
    """Muestra un resultado recuperado. Retorna cuántos elementos tenía."""
    if isinstance(datos, dict) and "filas" in datos:  # CSV: {"columnas": [...], "filas": [...]}
        filas = datos["filas"]
        print(f"\n Columnas: {', '.join(datos['columnas'])}")
        for fila in filas[:5]:
            print("  |", " | ".join(fila.values()))
        if len(filas) > 5:
            print(f"  ... y {len(filas) - 5} filas más")
        return len(filas)

    # JSON: se muestra con formato; si es muy largo se recorta
    lineas = json.dumps(datos, ensure_ascii=False, indent=2).split("\n")
    print()
    for linea in lineas[:40]:
        print(" ", linea)
    if len(lineas) > 40:
        print(f"  ... ({len(lineas) - 40} líneas más)")
    return len(datos) if isinstance(datos, list) else 1


def opcion_recuperar():
    """Opción 6: recupera un resultado guardado antes, sin reprocesar el dataset."""
    print("\n--- RECUPERAR UN RESULTADO GUARDADO ---")
    ruta = input(" Nombre del archivo (.csv o .json): ").strip()
    if not ruta:
        print(" No escribiste ningún nombre.")
        return
    datos = archivos.cargar_resultado_anterior(ruta)
    if datos is None:  # archivos.py ya explicó el error
        return
    cantidad = mostrar_recuperado(datos)
    archivos.registrar_consulta("recuperar " + ruta, cantidad)


# ---------------------------------------------------------------
# Función principal
# ---------------------------------------------------------------
def ejecutar_code():
    """Carga los datos, genera el resumen y mantiene el menú hasta que el usuario salga."""
    columnas, filas = cargar_datos()
    if not filas:
        print(" Error: no se pudo cargar ningún dataset. Verifique que el archivo esté en la carpeta.")
        return False
    print(f" Dataset cargado exitosamente: {len(filas)} registros cargados.")

    resumen = generar_resumen_inicial(filas)  # resumen.json automático al iniciar

    while True:  # el menú se repite hasta que el usuario elija salir
        cargar_menu()
        opcion = input(" Seleccione una opción (1-8): ").strip()

        if opcion == "1":
            opcion_buscar(columnas, filas)
        elif opcion == "2":
            opcion_estadisticas(columnas, filas)
        elif opcion == "3":
            opcion_agrupar(columnas, filas)
        elif opcion == "4":
            opcion_mejor_equipo(columnas, filas)
        elif opcion == "5":
            opcion_resumen(resumen)
        elif opcion == "6":
            opcion_recuperar()
        elif opcion == "7":
            archivos.historial_consultas()
        elif opcion == "8":
            print("\n Saliendo del sistema DataLab. ¡Hasta luego!")
            break
        else:
            print(" Opción no válida. Por favor, ingrese un número del 1 al 8.")

    return True  # retorna True al finalizar la ejecución de manera exitosa


if __name__ == "__main__":
    ejecutar_code()
