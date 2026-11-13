# ⚽ DataLab: Goles de la Copa Mundial (The Com)
Herramienta modular de análisis de datos desarrollada en Python 3 para la consulta, el recorrido y la estadística de una base de datos compuesta por los goles hechos en toda la historia de la Copa Mundial Masculina de la FIFA. 


## 👥 Integrantes del Grupo (The Com)
* Juan José Riaño Carreño
* Sebastián Meneses Forero
* Daniel Felipe Pachón Perilla
* Emanuel Campo
* Johan Mateo Acosta
* Juan Pablo Rozo Martínez

## 📊 Dataset

* **Descripción y Origen:** Registro histórico (obtenido de Kaggle) sobre goles anotados en ediciones de la Copa Mundial de la FIFA. Contiene variables cualitativas y cuantitativas asociadas a los partidos, selecciones, jugadores y el tiempo de juego.
* **Archivos disponibles en el repositorio:**
  * `goals_pequeno.csv`: compuesto por las primeras 50 filas de la base de datos original
  * `goals_completo.csv`: Dataset completo con más de 200 registros.
* **Campos clave analizados:**
  - `match_id` y `match_name`: Identificador y nombre del partido disputado.
  - `team_name`: Selección nacional que anota el gol.
  - `family_name`: Apellido del jugador anotador.
  - `minute_regulation`: Minuto reglamentario en que se anotó el gol.
  - `own_goal`: Indicador (`1` o `0`) si fue autogol.
  - `penalty`: Indicador (`1` o `0`) si fue cobro desde el punto penal.
## ❓ Preguntas de Investigación
1. ¿Qué selección nacional anota la mayor cantidad de goles?
2. ¿En qué minuto del partido se concentra la mayor cantidad de anotaciones?
3. ¿Cuál es el comportamiento de los goles de penalti vs. jugada en cancha?

## 📁 Estructura del Repositorio

```text
Proyecto_Programaci-n/
├── main.py                              # Menú interactivo principal y control de flujo en consola
├── analisis.py                          # Funciones de búsqueda, estadísticas, rankings y resumen global
├── archivos.py                          # Carga/guardado en CSV y JSON, y gestión del historial
├── goals_completo.csv                   # Dataset completo de goles del Mundial
├── goals_pequeno.csv                    # Muestra inicial de 50 registros (Entrega 1)
├── historial.csv                        # Registro automático de búsquedas (fecha, término y resultados)
├── resumen.json                         # Resumen estadístico generado automáticamente al iniciar
├── contribuciones_datalab.pdf           # Documento de aportes por integrante
├── datalab GOLES DE LA COPA MUNDIAL.pdf # Diagrama de flujo de datos y ficha del proyecto
└── README.md                            # Documentación general e instrucciones de ejecución
```
## 🚀 Instrucciones de Ejecución 
1. Asegúrate de tener instalado **Python 3.x**.
2. Clona el repositorio o descarga los archivos en tu equipo.
3. Abre en tu editor de codigo la carpeta completa del repositorio ya descomprimido
4. desde la terminal ingresa la dirección para que el main corra perfectamente
5. Ejecuta el programa principal desde tu terminal o consola:
   ```bash
   python main.py
