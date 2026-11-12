#1. BUSCAR POR TEXTO
def verificador_de_estado(): #Esta funcion pregunta al usuario si quiere volvera buscar

    print("1. Salir y guardar la busqueda.")
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
                    filasParaImprimir.append(tuple(fila.values()))#  agrega  los valores del diccionario como una lista para imprimir
                    break # detiene la revisión de esta fila para no meterla en la lista dos veces
        conteo = impresor_fila(filasParaImprimir, termino) # imprime  todas las  filas que coincidan

        print(f"Se encontraron {conteo} filas con el Termino '{termino}'.")
        estado = verificador_de_estado() #funcion que define si el buscador se acaba o no
    return filasParaImprimir #retorna la lista para guarda la ultima busqueda

#2. AGRUPAR GOLES POR SELECCIÓN
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
