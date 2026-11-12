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