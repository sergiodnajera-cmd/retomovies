import os
from google.cloud import firestore

# ==========================================
# CONFIGURACION FIREBASE
# ==========================================

JSON_FILE = "firebase-key.json"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(
    BASE_DIR,
    JSON_FILE
)

# Conexion
db = firestore.Client()

print("✅ Conectado a Firestore")

# ==========================================
# DATOS
# ==========================================

movies = [
    {"name":"The Shawshank Redemption","genre":"Drama","director":"Frank Darabont","company":"Castle Rock Entertainment"},
    {"name":"The Godfather","genre":"Crime","director":"Francis Ford Coppola","company":"Paramount Pictures"},
    {"name":"The Dark Knight","genre":"Action","director":"Christopher Nolan","company":"Warner Bros."},
    {"name":"Pulp Fiction","genre":"Crime","director":"Quentin Tarantino","company":"Miramax"},
    {"name":"Forrest Gump","genre":"Drama","director":"Robert Zemeckis","company":"Paramount Pictures"},
    {"name":"Inception","genre":"Science Fiction","director":"Christopher Nolan","company":"Warner Bros."},
    {"name":"Titanic","genre":"Romance","director":"James Cameron","company":"20th Century Fox"},
    {"name":"Avatar","genre":"Science Fiction","director":"James Cameron","company":"20th Century Fox"},
    {"name":"Gladiator","genre":"Action","director":"Ridley Scott","company":"DreamWorks Pictures"},
    {"name":"The Matrix","genre":"Science Fiction","director":"Lana Wachowski","company":"Warner Bros."},
    {"name":"Interstellar","genre":"Science Fiction","director":"Christopher Nolan","company":"Paramount Pictures"},
    {"name":"Joker","genre":"Drama","director":"Todd Phillips","company":"Warner Bros."},
    {"name":"The Lion King","genre":"Animation","director":"Roger Allers","company":"Walt Disney Pictures"},
    {"name":"Finding Nemo","genre":"Animation","director":"Andrew Stanton","company":"Pixar Animation Studios"},
    {"name":"Toy Story","genre":"Animation","director":"John Lasseter","company":"Pixar Animation Studios"},
    {"name":"Up","genre":"Animation","director":"Pete Docter","company":"Pixar Animation Studios"},
    {"name":"Coco","genre":"Animation","director":"Lee Unkrich","company":"Pixar Animation Studios"},
    {"name":"The Avengers","genre":"Action","director":"Joss Whedon","company":"Marvel Studios"},
    {"name":"Iron Man","genre":"Action","director":"Jon Favreau","company":"Marvel Studios"},
    {"name":"Black Panther","genre":"Action","director":"Ryan Coogler","company":"Marvel Studios"},
    {"name":"Doctor Strange","genre":"Action","director":"Scott Derrickson","company":"Marvel Studios"},
    {"name":"Guardians of the Galaxy","genre":"Adventure","director":"James Gunn","company":"Marvel Studios"},
    {"name":"Spider-Man Homecoming","genre":"Action","director":"Jon Watts","company":"Marvel Studios"},
    {"name":"Jurassic Park","genre":"Adventure","director":"Steven Spielberg","company":"Universal Pictures"},
    {"name":"E.T. the Extra-Terrestrial","genre":"Science Fiction","director":"Steven Spielberg","company":"Universal Pictures"},
    {"name":"Jaws","genre":"Thriller","director":"Steven Spielberg","company":"Universal Pictures"},
    {"name":"Saving Private Ryan","genre":"War","director":"Steven Spielberg","company":"DreamWorks Pictures"},
    {"name":"The Silence of the Lambs","genre":"Thriller","director":"Jonathan Demme","company":"Orion Pictures"},
    {"name":"The Green Mile","genre":"Drama","director":"Frank Darabont","company":"Warner Bros."},
    {"name":"Fight Club","genre":"Drama","director":"David Fincher","company":"20th Century Fox"},
    {"name":"Se7en","genre":"Crime","director":"David Fincher","company":"New Line Cinema"},
    {"name":"The Social Network","genre":"Drama","director":"David Fincher","company":"Columbia Pictures"},
    {"name":"La La Land","genre":"Musical","director":"Damien Chazelle","company":"Summit Entertainment"},
    {"name":"Whiplash","genre":"Drama","director":"Damien Chazelle","company":"Bold Films"},
    {"name":"Parasite","genre":"Thriller","director":"Bong Joon-ho","company":"Barunson E&A"}
]

# ==========================================
# CARGA DE DATOS
# ==========================================

for movie in movies:
    db.collection("movies").add(movie)

print(f"✅ Se cargaron {len(movies)} películas correctamente")