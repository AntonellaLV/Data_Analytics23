# Importar módulo
import psycopg2
import config

# Establece la conexión a la base de datos
conn = psycopg2.connect(
    host="localhost",
    database="InfoDataAnalytics23",
    user="postgres",
    password="admin",
    port="5432"
)

try:
    # Crea un cursor a partir de la conexión
    cursor = conn.cursor()

    # Ejecuta una consulta SELECT en una tabla específica
    cursor.execute("SELECT * FROM agents")
    rows = cursor.fetchall()

    # Imprime los resultados
    for row in rows:
        print(row)

    # Cierra el cursor
    cursor.close()

finally:
    # Cierra la conexión con la base de datos
    conn.close()

