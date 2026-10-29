from postgres_utils import conectar

try:

    conn = conectar()

    print("Conexion PostgreSQL correcta")

    conn.close()

except Exception as e:

    print(e)