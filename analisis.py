import archivos
#1. BUSCAR POR TEXTO
def verificador_de_estado(): #Esta funcion pregunta al usuario si quiere volvera buscar

    print("1. Salir de la busqueda.")
    print("2. Volver a buscar.")

    YN = input("Escribe un numero valido: ").strip().casefold() #pregunta al usuario que quiere hacer
    if YN == "1":
        return False 
    elif YN == "2":
        return True
    else:
        print("Comando no reconocido.")
        return verificador_de_estado() # se llama a si mismo a que la respuesta sea valida

def validar_termino(): #esta funcion limpia el texto que puso el usuario
    while True:
        termino = input("Que termino quieres buscar?: ").strip().casefold() #recibe y limpia la palabra que se busca
        if not termino:
            print("Por favor ingresa un término válido (no vacío).")
        else:
            break
    return termino
  
def impresor_fila(filas, termino = "SIN VALOR"):#funcion para imprimir las filas 
    for fila in filas:
        for celda in fila:
            if termino in celda.casefold():
                print("|", f"--> {celda} <--", end=" ")#imprime y señala la celda
            else:
                print("|", celda, end=" ") #imprime la celda sin señalar
        print() # da espacio al imprimer el siguiene enunciado
    print() 
    return len(filas)

def Buscar_Texto(columnas, filas):
    estado = True # inicia con estado true para el bucle

    while estado:
        filasParaImprimir = []
        termino = validar_termino() # lo que se busca
        print() #espacio con la siguiene impresion
        impresor_fila([columnas]) #imprime los encabezados
        
        #este bloque for desempaqueta las filas y revisa cada celda
        for fila in filas: 
            for celda in fila.values():
                if termino in celda.casefold():
                    filasParaImprimir.append(fila)
                    break # detiene la revisión de esta fila para no meterla en la lista dos veces
        conteo = impresor_fila([tuple(f.values()) for f in filasParaImprimir], termino) # imprime  todas las  filas que coincidan

        print(f"Se encontraron {conteo} filas con el Termino '{termino}'.")
        archivos.registrar_consulta(termino, conteo)
        estado = verificador_de_estado() #funcion que define si el buscador se acaba o no
    return filasParaImprimir #retorna la lista de los resultados encontrados

#2. ESTADISTICAS BASICAS
def estadisticas_basicas(columnas, filas):
    """Función Obligatoria #2:
    Lee y extrae del archivo CSV con la columna "minute_regulation" y 
    cálcula el mínimo, máximo y promedio.
    """
    #Verificar que la columna exista y que la filas tambien lo tenga antes de continuar
    if not ("minute_regulation" in columnas):
        print("Error, no se encontró la columna.")
        return None
    #Variables acumuladoras:
    TodosLosMinutos = []
    
    for fila in filas: #Recorrer dato por dato según la columna
        valor_texto = fila.get("minute_regulation").strip()
        if valor_texto != "": #Ignorar si hay algun dato vacio
            try:
                valor_numerico = float(valor_texto) #Si llega a ver decimales, se convierte a float.
                TodosLosMinutos.append(valor_numerico)  
            except ValueError: #Si llega a ver un campo con texto, ignorarlo.
                pass

    #valida si recolecto datos
    if not TodosLosMinutos:
        print("Error, no se encontraron datos.")
        return None
    # Operaciones para hallar los datos
    ordenados = sorted(TodosLosMinutos) #Ordena los numero de mayo a menor
    valor_maximo = ordenados[-1]
    valor_minimo = ordenados[0]
    cantidad_datos = len(TodosLosMinutos)

    #Mostrar resultados finales:
    if cantidad_datos > 0:
        promedio = sum(TodosLosMinutos) / cantidad_datos
        print("\n" + "="*55)
        print(" Máximo, Mínimo y Promedio: Minuto de anotación del gol")
        print("="*55)
        print(f" Total de datos procesados: {cantidad_datos}")
        print(f" Minuto Máximo: {valor_maximo:.0f}'")
        print(f" Minuto Mínimo: {valor_minimo:.0f}'")
        print(f" Minuto Promedio: {promedio:.2f}'")
        print("="*55)
        return valor_minimo, valor_maximo, promedio
    else:
        print("No se encontraron datos numéricos.")
        return None
def generar_resumen_dataset(filas):
    """
    Genera un resumen global del dataset.
    Retorna un diccionario con total de registros, selecciones únicas y estadísticas.
    """
    selecciones_unicas = set() # Uso de 'set' para evitar duplicados automáticamente
    minutos_validos = []
    
    for fila in filas:
        equipo = fila.get("team_name", "").strip()
        if equipo:
            selecciones_unicas.add(equipo)
            
        valor_minuto = fila.get("minute_regulation", "").strip()
        if valor_minuto:
            try:
                minutos_validos.append(float(valor_minuto))
            except ValueError:
                pass # Ignorar celdas que no sean numéricas
                    
    
    if minutos_validos:
        maximo = max(minutos_validos)
        minimo = min(minutos_validos)
        promedio = sum(minutos_validos) / len(minutos_validos)
    else:
        maximo = minimo = promedio = 0

    
    resumen = {
        "total_registros_procesados": len(filas),
        "total_selecciones_unicas": len(selecciones_unicas),
        "lista_selecciones": sorted(list(selecciones_unicas)),
        "estadisticas_minuto_gol": {
            "maximo": round(maximo, 1),
            "minimo": round(minimo, 1),
            "promedio": round(promedio, 2)
        }
    }
    
    return resumen
# 3. AGRUPAR GOLES POR SELECCIÓN
    def agrupar_goles_por_seleccion(columnas, filas):
    """
    Agrupa y cuenta cuántos goles hay por cada seleccion nacional ordenados de mayor a menor
    y calcula la proporción de penaltis frente a jugada en cancha"""
    # Sin la columna del equipo no se puede agrupar
    if "team_name" not in columnas:
        print("Error: No se encontró la columna 'team_name'.")
        return []

    conteo_equipos = {}  # equipo -> cantidad de goles
    penaltis = 0
    jugada_regular = 0
    autogoles = 0

    for fila in filas:
        # Contar el gol para el equipo de esta fila
        equipo = fila.get("team_name", "").strip()
        if equipo != "":
            conteo_equipos[equipo] = conteo_equipos.get(equipo, 0) + 1

        # Penalti o jugada regular (solo si el dataset trae esa columna)
        if "penalty" in columnas:
            if fila.get("penalty", "").strip() == "1":
                penaltis += 1
            else:
                jugada_regular += 1

        # Autogoles (solo si el dataset trae esa columna)
        if "own_goal" in columnas:
            if fila.get("own_goal", "").strip() == "1":
                autogoles += 1

    # Mayor a menor; si empatan, orden alfabético
    ranking_equipos = sorted(conteo_equipos.items(), key=lambda par: (-par[1], par[0]))

    print("\n" + "=" * 55)
    print(" Conteo de Goles por Selección (De mayor a menor)  ")
    print("=" * 55)
    for posicion, (equipo, cantidad) in enumerate(ranking_equipos, start=1):
        print(f" {posicion:2d}. {equipo:<18} : {cantidad} gol(es)")

    if "penalty" in columnas:
        total_goles = penaltis + jugada_regular
        porc_pen = (penaltis / total_goles * 100) if total_goles > 0 else 0.0
        porc_reg = (jugada_regular / total_goles * 100) if total_goles > 0 else 0.0
        print("-" * 55)
        print(" Comportamiento Penaltis vs. Jugada en Cancha:")
        print(f" • Jugada regular : {jugada_regular} goles ({porc_reg:.1f}%)")
        print(f" • Tiro penal     : {penaltis} gol(es) ({porc_pen:.1f}%)")
        print(f" • Autogoles      : {autogoles} gol(es)")
    print("=" * 55)
    return ranking_equipos
# 4. MEJOR EQUIPO DE LA HISTORIA  (migrado desde main.py)
def contar_goles(columnas, filas):
    """Recorre las filas y devuelve {equipo: total de goles}."""
    # 'columnas' se conserva como parámetro para mantener la misma llamada
    # que el resto de funciones: funcion(columnas, filas).
    goles = {}  # aquí se acumula: equipo -> cantidad de goles

    # Cada fila del CSV es UN gol, así que basta sumar 1 por fila
    for fila in filas:
        equipo = fila.get("team_name", "").strip()
        if equipo:
            # get(equipo, 0): si el equipo aún no está, empieza en 0
            goles[equipo] = goles.get(equipo, 0) + 1

    return goles


def armar_marcadores(columnas, filas):
    """Devuelve {id_partido: {equipo: goles en ese partido}}."""
    partidos = {}  # id del partido -> marcador de ese partido

    for fila in filas:
        id_partido = fila.get("match_id", "").strip()
        nombre_partido = fila.get("match_name", "").strip()
        equipo = fila.get("team_name", "").strip()

        # Sin estos tres datos no se puede armar el marcador
        if not (id_partido and nombre_partido and equipo):
            continue

        # Primera vez que vemos este partido: creamos su marcador
        if id_partido not in partidos:
            partidos[id_partido] = {}
            # "Argentina vs Chile" -> ["Argentina", "Chile"]
            # Ambos equipos arrancan en 0 para que el que pierda 0-2
            # también aparezca en el marcador.
            separador = " vs " if " vs " in nombre_partido else " v "
            for nombre in nombre_partido.split(separador):
                partidos[id_partido][nombre.strip()] = 0

        # Sumamos el gol de esta fila al equipo que lo anotó
        partidos[id_partido][equipo] = partidos[id_partido].get(equipo, 0) + 1

    return partidos


def contar_partidos_ganados(partidos):
    """Gana el equipo que anotó más goles en cada partido. Devuelve {equipo: victorias}."""
    ganados = {}  # equipo -> cantidad de partidos ganados

    for marcador in partidos.values():
        # Un partido válido tiene exactamente 2 equipos; si no, se ignora
        if len(marcador) != 2:
            continue

        # items() da dos pares (equipo, goles); se reparten en 4 variables
        (equipo_a, goles_a), (equipo_b, goles_b) = marcador.items()

        if goles_a > goles_b:
            ganados[equipo_a] = ganados.get(equipo_a, 0) + 1
        elif goles_b > goles_a:
            ganados[equipo_b] = ganados.get(equipo_b, 0) + 1
        # Si empatan no se suma nada: un empate no es victoria

    return ganados


def armar_ranking(datos):
    """Ordena de mayor a menor; si empatan, orden alfabético. Devuelve lista de (equipo, valor)."""
    # datos.items() -> pares (equipo, valor)
    # key: tupla (-valor, nombre). El signo menos hace que el valor
    # se ordene de mayor a menor, y el nombre desempata alfabéticamente.
    return sorted(datos.items(), key=lambda par: (-par[1], par[0]))


def buscar_mejores(ranking):
    """Devuelve la lista de equipos que comparten el primer puesto."""
    # Si no hay datos, no hay mejores
    if not ranking:
        return []

    # El primero del ranking tiene el valor más alto
    mejor_valor = ranking[0][1]

    # Todos los equipos con ese mismo valor están empatados en el primer puesto
    return [equipo for equipo, valor in ranking if valor == mejor_valor]


def mostrar_resultado(ranking, titulo):
    """Imprime el top 5 y el mejor equipo (o el empate)."""
    print(f"\nTop 5 por {titulo}:")

    # ranking[:5] toma solo los 5 primeros; start=1 numera desde 1
    for posicion, (equipo, valor) in enumerate(ranking[:5], start=1):
        print(f"{posicion}. {equipo}: {valor}")

    mejores = buscar_mejores(ranking)
    if len(mejores) == 1:
        print(f"\nMejor equipo por {titulo}: {mejores[0]}")
    elif len(mejores) > 1:
        # Más de un equipo con el valor máximo -> hay empate
        print(f"\nEmpate en {titulo} entre: {', '.join(mejores)}")
    else:
        print(f"\nNo hay datos suficientes para determinar el mejor en {titulo}.")

    return mejores  # retorna la lista de mejores equipos obtenidos


def mejor_equipo(columnas, filas):
    """
    Pregunta si el mejor equipo se define por goles o por partidos ganados
    y muestra el top 5 con el equipo ganador.
    Devuelve un diccionario con la última consulta hecha (o None si no hizo ninguna).
    """
    # Los datos no cambian, así que se calculan una sola vez (fuera del menú)
    goles = contar_goles(columnas, filas)
    ganados = contar_partidos_ganados(armar_marcadores(columnas, filas))

    resultado = None  # se llena cuando el usuario hace una consulta válida

    # Menú que se repite hasta que el usuario elija volver
    while True:
        print("\n¿Qué hace a una selección la mejor?")
        print("1. Cantidad de goles")
        print("2. Partidos ganados")
        print("3. Volver al menú principal")
        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == "3":
            break  # sale del menú y vuelve al programa principal
        elif opcion == "1":
            datos, titulo = goles, "goles"
        elif opcion == "2":
            datos, titulo = ganados, "partidos ganados"
        else:
            print("Opción no válida. Ingresa 1, 2 o 3.")
            continue  # vuelve a mostrar el menú

        # Con el criterio elegido: ordenar, mostrar y guardar el resultado
        ranking = armar_ranking(datos)
        mejores = mostrar_resultado(ranking, titulo)
        resultado = {"criterio": titulo, "ranking": ranking,
                     "mejores": mejores}

    return resultado
