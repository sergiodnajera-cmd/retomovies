import psycopg2
import streamlit as st


def conectar():

    conn = psycopg2.connect(
        host=st.secrets["POSTGRES_HOST"],
        port=st.secrets["POSTGRES_PORT"],
        database=st.secrets["POSTGRES_DATABASE"],
        user=st.secrets["POSTGRES_USER"],
        password=st.secrets["POSTGRES_PASSWORD"],
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