"""

División de Trabajo:
Integrante 1:
Hace el esqueleto del archivo, se encargar de la carga y el provcesamiento del archivo csv.
Integrante 2:
Se encarga de el desarrollo de la primera función obligatoria. 
Integrante 3:
Se encarga de el desarrolllo de la segunda función obligatoria.
Integrante 4:
Define y desarrolla la función opcional para el código.
Integrante 5:
README.md, Video y Producto Creativo (Póster Digital)
Integrante 6:
Documento de contribuciones (1 página) + Verificación y pruebas del repositorio
"""

def cargar_archivo(ruta_documento):
    """
    Guía para usarlo:
    Lee el archivo CSV utilizando la función nativa open() y procesa cada línea con el método .split(',').

    Parámetros:
        ruta_documento: Ruta del archivo csv con los 50 registros iniciales

    Retorna:
        tupla: (nombres_columna, fila_):
            -nombres_columna: lista con los nombres de las columnas    
            -fila_#: Listas de listas donde contempla las filas y sus valores
    """

    #inciar tuplas
    #hacer el open
    #sino esta vacion recorrer y llenar las tuplas
    #retornar las tuplas

    columnas = []
    filas = []

    with open(ruta_documento, mode='r', encoding='utf-8') as f:#Invoca el gestor de contexto en modo lectura, soportando caracteres especiales y tildes
        Lineas = f.readlines()#Lee la totalidad del archivo
        if len(Lineas) > 0:#Verifica si la lista tiene archivos
            columnas = Lineas[0].strip().split(',')# hagarra los encabezados y los guarda limpios

            for Linea in Lineas[1:]:#itera toda la lista
                Linea_nueva = Linea.strip()#Limpia la linea
                if Linea_nueva:#verifica si esta vacia
                    arreglo_filas = Linea_nueva.split(',')#Divide toda la fila en un arreglo
                    filas.append(arreglo_filas)#los agrega a la lista previamente creada
    return columnas, filas
#1. BUSCAR POR TEXTO
def impresor_fila(fila, termino = "SIN VALOR"):#funcion para imprimir las filas
        
        for celda in fila: #selecciona cada celda de la fila a imprimir

            if termino in celda.casefold():#verifica si es el termino y lo señala
                print("|", f"--> {celda} <--", end=" ")#imprime y señala la celda

            else:
                print("|", celda, end=" ") #imprime la celda sin señalar
            
        print() # da espacio al imprimer el siguiene enunciado
        print() 

def verificador_de_estado(): #verifica si continua en en el apartado de buqueda

    YN = input("Deseas volver a buscar? Y/N: ").strip().casefold() #pregunta al usuario que quiere hacer

    if YN == "n":
        return False #devuelve false para salir del apartado de busqueda
    
    elif YN == "y":
        return True #devuelve true para seguir en el apartado de busqueda

    else:
        print("Comando no reconocido.")
        return verificador_de_estado() # se llama a si mismo a que la respuesta sea valida
    
def Buscar_Texto(columnas, filas):

    estado = True # inicia con estado true para el bucle

    while estado:
        termino = input("Que termino quieres buscar?: ").strip().casefold() #recibe y limpia la palabra que se busca
        print() #espacio con la siguiene impresion
        contador = 0 #establece cuantas filas se enccontraron con ese termino
        fila_procesada = 0 #establece que fila ya se imprimio
        impresor_fila(columnas) #imprime los encabezados

        for fila in filas: #selecciona una por una cada fila

            for celda in fila: #seleciona cada celda de la fila

                if termino in celda.casefold(): # compara las celdas con en termino

                    if fila_procesada != fila[0]: #evita imprimir la misma fila dos veces
                        impresor_fila(fila, termino) #imprime la fila y señala el termino
                        fila_procesada = fila[0] #odtiene el valor de la fila que ya se imprimio
                        contador += 1 # suma a la cantidad de registros encontrados

        print(f"Se encontraron {contador} filas con el Termino '{termino}'.") #imprime la cantidad de registros encontrados
        estado = verificador_de_estado() #funcion que define si el buscador se acaba o no
        contador = 0 #reinicia el contador

def estadisticas_basicas(columnas, filas):
    """Función Obligatoria #2:
    Lee y extrae del archivo CSV con la columna "minute_regulation" y 
    cálcula el mínimo, máximo y promedio.
    """
    indice_minuto = -1 #Buscar columna objetivo
    for i in range(len(columnas)):
        if columnas[i].strip() == "minute_regulation":
            indice_minuto = i
            break
    #Verificar que la columna exista antes de continuar
    if indice_minuto == -1: 
        print("Error, no se encontró la columna.")
        return
    #Variables acumuladoras:
    total_suma = 0
    cantidad_datos = 0
    valor_maximo = None 
    valor_minimo = None
    
    for fila in filas: #Recorrer dato por dato según la columna
        if len(fila) > indice_minuto: #Verificar que la fila si tenga suficientes elementos
            valor_texto = fila[indice_minuto].strip()
            if valor_texto != "": #Ignorar si hay algun dato vacio
                try:
                    valor_numerico = float(valor_texto) #Si llega a ver decimales, se convierte a float.
                    
                    total_suma += valor_numerico #Acumulador para el promedio
                    cantidad_datos += 1
                    #Buscar máximo:
                    if valor_maximo is None or valor_numerico > valor_maximo: 
                        valor_maximo = valor_numerico
                    #Buscar mínimo:
                    if valor_minimo is None or valor_numerico < valor_minimo:
                        valor_minimo = valor_numerico
                except ValueError: #Si llega a ver un campo con texto, ignorarlo.
                    pass
    #Mostrar resultados finales:
    if cantidad_datos > 0:
        promedio = total_suma / cantidad_datos
        print("\n" + "="*55)
        print(" Máximo, Mínimo y Promedio: Minuto de anotación del gol")
        print("="*55)
        print(f" Total de datos procesados: {cantidad_datos}")
        print(f" Minuto Máximo: {valor_maximo:.0f}'")
        print(f" Minuto Mínimo: {valor_minimo:.0f}'")
        print(f" Minuto Promedio: {promedio:.2f}'")
        print("="*55)
    else:
        print("No se encontraron datos numéricos.")
        return None
                    
#3. AGRUPAR GOLES POR SELECCIÓN
def agrupar_goles_por_seleccion(columnas, filas):
    """
    Agrupa y cuenta cuántos goles hay por cada seleccion nacional ordeanos de mayor a menor 
    y calcula la proporción de penaltis frente a jugada en cancha"""
    indice_equipo = -1
    indice_penalti = -1
    indice_autogol = -1

    for i in range(len(columnas)):
         nombre_col = columnas[i].strip()
        if nombre_col == "team_name":
            indice_equipo = i
        elif nombre_col == "penalty":
            indice_penalti = i
        elif nombre_col == "own_goal":
            indice_autogol = i

    if indice_equipo == -1:
        print("Error: No se encontró la columna 'team_name'.")
        return []

    conteo_equipos = {}
    penaltis = 0
    jugada_regular = 0
    autogoles = 0

    for fila in filas:
        if len(fila) > indice_equipo:
            equipo = fila[indice_equipo].strip()
            if equipo != "":
                conteo_equipos[equipo] = conteo_equipos.get(equipo, 0) + 1

        if indice_penalti != -1 and len(fila) > indice_penalti:
            if fila[indice_penalti].strip() == "1":
                penaltis += 1
            else:
                jugada_regular += 1

        if indice_autogol != -1 and len(fila) > indice_autogol:
            if fila[indice_autogol].strip() == "1":
                autogoles += 1

    ranking_equipos = sorted(conteo_equipos.items(), key=lambda par: (-par[1], par[0]))

    print("\n" + "=" * 55)
    print(" Conteo de Goles por Selección (De mayor a menor)")
    print("=" * 55)
    for posicion, (equipo, cantidad) in enumerate(ranking_equipos, start=1):
        print(f" {posicion:2d}. {equipo:<18} : {cantidad} gol(es)")

    if indice_penalti != -1:
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
        
#4.MEJOR EQUIPO DE LA HISTORIA
def mejor_equipo(columnas, filas):
    """
    Pregunta si el mejor equipo se define por goles o por partidos ganados
    y muestra el top 5 con el equipo ganador.
    """
 
    # posiciones de las columnas que necesitamos
    i_partido = columnas.index("match_id")
    i_nombre_partido = columnas.index("match_name")
    i_equipo = columnas.index("team_name")  # equipo al que se le acredita el gol
 
    goles = {}     # equipo -> total de goles
    partidos = {}  # id del partido -> {equipo: goles en ese partido}
 
    for fila in filas:
        equipo = fila[i_equipo]
        id_partido = fila[i_partido]
 
        goles[equipo] = goles.get(equipo, 0) + 1
 
        # "Argentina vs Chile" -> crea el marcador con ambos equipos en 0
        if id_partido not in partidos:
            partidos[id_partido] = {}
            for nombre in fila[i_nombre_partido].split(" vs "):
                partidos[id_partido][nombre] = 0
 
        partidos[id_partido][equipo] += 1
 
    # gana el equipo que anotó más goles en ese partido
    ganados = {}
    for marcador in partidos.values():
        (equipo_a, goles_a), (equipo_b, goles_b) = marcador.items()
        if goles_a > goles_b:
            ganados[equipo_a] = ganados.get(equipo_a, 0) + 1
        elif goles_b > goles_a:
            ganados[equipo_b] = ganados.get(equipo_b, 0) + 1
 
    while True:
        print("\n¿Qué hace a una selección la mejor?")
        print("1. Cantidad de goles")
        print("2. Partidos ganados")
        print("3. Volver al menú principal")
        opcion = input("Elige una opción (1-3): ").strip()
 
        if opcion == "3":
            break
        elif opcion == "1":
            datos = goles
            titulo = "goles"
        elif opcion == "2":
            datos = ganados
            titulo = "partidos ganados"
        else:
            print("Opción no válida. Ingresa 1, 2 o 3.")
            continue
 
        # mayor a menor; si empatan, orden alfabético
        ranking = sorted(datos.items(), key=lambda par: (-par[1], par[0]))
 
        print(f"\nTop 5 por {titulo}:")
        for posicion, (equipo, valor) in enumerate(ranking[:5], start=1):
            print(f"{posicion}. {equipo}: {valor}")
 
        mejor_valor = ranking[0][1]
        mejores = [equipo for equipo, valor in ranking if valor == mejor_valor]
 
        if len(mejores) == 1:
            print(f"\nMejor equipo por {titulo}: {mejores[0]}")
        else:
            print(f"\nEmpate en {titulo} entre: {', '.join(mejores)}")
 #
def cargar_menu():

    print("\n" + "="*55)
    print("   DATALAB - EXPLORADOR DE GOLES DEL MUNDIAL   ")
    print("="*55)
    print("1. Buscar registros por texto (Texto)")
    print("2. Ver estadísticas básicas del minuto de los goles")
    print("3. Agrupar goles por Selección (Categoría)")
    print("4. Analizar criterios del 'Mejor Equipo de la Historia'")
    print("5. Salir")
    print("="*55)

def ejecutar_code():
    Data_set = "goals_pequeno.csv"
    try:# intenta realizar la acción y si dispara un error manda el except
        columnas, filas = cargar_archivo(Data_set)
        print(f" Dataset cargado exitosamente: {len(filas)} registros cargados.")
    except FileNotFoundError:# si no puede abrir el archivo dispara esto
        print(f" Error: No se encontró el archivo '{Data_set}'. Verifique la ruta.")
        return
    
    while True:# inicia el while para siempre hasta que usen el breka
        cargar_menu()
        opcion = input(" Seleccione una opción (1-5): ").strip()
            
        if opcion == "1":
            print("\n--- BÚSQUEDA POR TEXTO ---")
            Buscar_Texto(columnas, filas)
                    
        elif opcion == "2":
            print("\n--- ESTADÍSTICAS BÁSICAS DEL MINUTO DE REGULACIÓN ---")
            estadisticas_basicas(columnas, filas)
                    
        elif opcion == "3":
            print("\n--- AGRUPACIÓN POR SELECCIÓN (CATEGORÍA) ---")

        elif opcion == "4":
            print("\n--- ANÁLISIS CRITERIOS MEJOR EQUIPO DE LA HISTORIA ---")
            mejor_equipo(columnas, filas)
        elif opcion == "5":
            print("\n Saliendo del sistema DataLab. ¡Hasta luego!")
            break
        else:
            print(" Opción no válida. Por favor, ingrese un número del 1 al 5.")
    
ejecutar_code()
