import streamlit as st
import pandas as pd
from google.cloud import firestore
from google.oauth2 import service_account
from postgres_utils import insertar_visita, obtener_visitas

# ==================================================
# CONFIGURACION FIREBASE
# ==================================================

credenciales = service_account.Credentials.from_service_account_info(
    {
        "type": "service_account",
        "project_id": st.secrets["FIREBASE_PROJECT_ID"],
        "private_key": st.secrets["FIREBASE_PRIVATE_KEY"],
        "client_email": st.secrets["FIREBASE_CLIENT_EMAIL"],
        "token_uri": "https://oauth2.googleapis.com/token",
    }
)

db = firestore.Client(
    project=st.secrets["FIREBASE_PROJECT_ID"],
    credentials=credenciales
)

# ==================================================
# FUNCIONES
# ==================================================

def cargar_movies():

    docs = db.collection("movies").stream()

    movies = []

    for doc in docs:
        movies.append(doc.to_dict())

    return pd.DataFrame(movies)


def buscar_por_titulo(df, titulo):

    if titulo.strip() == "":
        return pd.DataFrame()

    resultado = df[
        df["name"].str.contains(
            titulo,
            case=False,
            na=False
        )
    ]

    return resultado


def buscar_por_director(df, director):

    resultado = df[
        df["director"] == director
    ]

    return resultado


def insertar_filme(name, genre, director, company):

    nuevo_filme = {
        "name": name,
        "genre": genre,
        "director": director,
        "company": company
    }

    db.collection("movies").add(nuevo_filme)

# ==================================================
# CARGA DATASET BASE
# ==================================================

df_movies = cargar_movies()

# ==================================================
# DASHBOARD
# ==================================================

st.title("Netflix App")

st.write(f"Total filmes visualizados: {len(df_movies)}")

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.header("Opciones")

# ==================================================
# PUNTO 5 - MOSTRAR TODOS LOS FILMES
# ==================================================

mostrar_filmes = st.sidebar.checkbox(
    "Mostrar todos los filmes"
)

if mostrar_filmes:
    st.header("Todos los filmes")
    st.dataframe(df_movies)

# ==================================================
# PUNTO 6 - BUSCAR POR TITULO
# ==================================================

st.sidebar.subheader("Buscar filme")

titulo_busqueda = st.sidebar.text_input(
    "Título del filme"
)

if st.sidebar.button("Buscar Filme"):

    resultado_busqueda = buscar_por_titulo(
        df_movies,
        titulo_busqueda
    )

    st.header("Resultado búsqueda")

    st.write(
        f"Total encontrados: {len(resultado_busqueda)}"
    )

    st.dataframe(resultado_busqueda)

# ==================================================
# PUNTO 7 - FILTRAR POR DIRECTOR
# ==================================================

st.sidebar.subheader("Seleccionar Director")

directores = sorted(
    df_movies["director"].unique()
)

director_seleccionado = st.sidebar.selectbox(
    "Director",
    directores
)

if st.sidebar.button("Filtrar Director"):

    resultado_director = buscar_por_director(
        df_movies,
        director_seleccionado
    )

    st.header(
        f"Películas de {director_seleccionado}"
    )

    st.write(
        f"Total filmes encontrados: {len(resultado_director)}"
    )

    st.dataframe(resultado_director)

    # ==================================================
# PUNTO 8 - NUEVO FILME
# ==================================================

st.sidebar.subheader("Nuevo Filme")

nuevo_nombre = st.sidebar.text_input(
    "Name"
)

nueva_company = st.sidebar.text_input(
    "Company"
)

nuevo_director = st.sidebar.text_input(
    "Director"
)

nuevo_genero = st.sidebar.text_input(
    "Genre"
)

if st.sidebar.button("Crear nuevo filme"):

    if (
        nuevo_nombre
        and nueva_company
        and nuevo_director
        and nuevo_genero
    ):

        insertar_filme(
            nuevo_nombre,
            nuevo_genero,
            nuevo_director,
            nueva_company
        )

        st.sidebar.success(
            "Filme creado correctamente"
        )
        
        st.rerun()

    else:

        st.sidebar.error(
            "Complete todos los campos"
        )

# ==================================================
# LIBRO DE VISITAS
# ==================================================

st.sidebar.subheader("Libro de visitas")

email_visita = st.sidebar.text_input(
    "Email"
)

comentario_visita = st.sidebar.text_area(
    "Comentario"
)

if st.sidebar.button("Registrar Visita"):

    if email_visita and comentario_visita:

        insertar_visita(
            email_visita,
            comentario_visita
        )

        st.sidebar.success(
            "Visita registrada correctamente"
        )

    else:

        st.sidebar.error(
            "Capture email y comentario"
        )

if st.sidebar.button("Ver visitas"):

    visitas = obtener_visitas()

    st.header("Libro de visitas")

    st.write(
        f"Total comentarios: {len(visitas)}"
    )

    for idx, visita in enumerate(
        visitas,
        start=1
    ):

        email = visita[0]
        comentario = visita[1]

        st.write(
            f"{idx}. {comentario}"
        )

        st.caption(email)

        st.divider()

