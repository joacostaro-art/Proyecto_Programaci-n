# ⚽ DataLab: Goles de la Copa Mundial (The Com)
Herramienta de análisis de datos desarrollada en el leguaje Python, sirve para, la consulta, el recorrido y la estadistica de una base de datos compuesta de los goles hechos en toda la historia de los mundiales de futbol. 


## 👥 Integrantes del Grupo (The Com)
* Juan José Riaño Carreño
* Sebastián Meneses Forero
* Daniel Felipe Pachón Perilla
* Emanuel Campo
* Johan Mateo Acosta
* Juan Pablo Rozo Martínez

## 📊 Dataset

* **Descripción y Origen:** Registro histórico sobre goles anotados en ediciones de la Copa Mundial Masculina de la FIFA. Contiene variables cualitativas y cuantitativas asociadas a los partidos, selecciones, jugadores y el tiempo de juego.
* **Archivos disponibles en el repositorio:**
  * `goals_pequeno.csv`: compuesto por las primeras 50 filas de la base de datos original
  * `goals_completo.csv`: Dataset completo con más de 200 registros.
* **Campos clave analizados:**
  * `match_name`: Partido disputado.
  * `team_name`: Selección nacional que anota el gol.
  * `family_name`: Apellido del jugador anotador .
  * `minute_regulation`: Minuto reglamentario en que se anotó el gol.
  * `own_goal`: Indicador booleano/entero si fue autogol.
  * `penalty`: Indicador booleano/entero si fue cobro desde el punto penal.
## ❓ Preguntas de Investigación
1. ¿Qué selección nacional anota la mayor cantidad de goles?
2. ¿En qué minuto del partido se concentra la mayor cantidad de anotaciones?
3. ¿Cuál es el comportamiento de los goles de penalti vs. jugada en cancha?

## 📁 Estructura del Repositorio
```text
Proyecto_Programaci-n/
├── README.md           # Carta de presentación e instrucciones para ejecutar el codigo.
├── goals_completo      # Dataset completo con más de 200 registros.
├── goals_pequeno.csv   # Compuesto por las primeras 50 filas de la base de datos original
└── main.py             # Codigo principal para recorrer la base de datos, ademas de diversas funciones.
```
## 🚀 Instrucciones de Ejecución 
1. Asegúrate de tener instalado **Python 3.x**.
2. Clona el repositorio o descarga los archivos en tu equipo.
3. Abre en tu editor de codigo la carpeta completa del repositorio ya descomprimido
4. desde la terminal ingresa la dirección para que el main corra perfectamente
5. Ejecuta el programa principal desde tu terminal o consola:
   ```bash
   python main.py
