import psycopg2

HOST = "pg-ad2a99d-sergiodnajera-3ffc.d.aivencloud.com"
PORT = "22344"
DATABASE = "defaultdb"
USER = "avnadmin"

# REEMPLAZA POR TU PASSWORD
PASSWORD = "PASSWORD_OCULTO"

def conectar():

    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        sslmode="require"
    )

    return conn


def insertar_visita(email, comentario):

    conn = conectar()

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO people(email, comment)
        VALUES (%s, %s)
        """,
        (email, comentario)
    )

    conn.commit()

    cur.close()
    conn.close()


def obtener_visitas():

    conn = conectar()

    cur = conn.cursor()

    cur.execute(
        """
        SELECT email, comment
        FROM people
        ORDER BY id DESC
        """
    )

    datos = cur.fetchall()

    cur.close()
    conn.close()

    return datos