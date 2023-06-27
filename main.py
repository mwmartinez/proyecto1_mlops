from fastapi import FastAPI
import pandas as pd 
import numpy as np
import sklearn
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.neighbors import NearestNeighbors


app = FastAPI(title="Proyecto Machine Learning Operations (MLOps) ",
              description=""" **Realizado por Michael Martinez** [Linkedin](https://www.linkedin.com/in/michael-mart%C3%ADnez/)
              \n En este proyecto, creamos un sistema de recomendación de películas utilizando técnicas de Machine Learning.
              \n El sistema está desarrollado en Python, con la ayuda de FastAPI y Render, para ofrecer una interfaz web interactiva. """
              )

# importamos los datos
movies_final = pd.read_csv('movies_final.csv',parse_dates=['release_date'])
movies_ml = pd.read_csv('movies_ml.csv',parse_dates=['release_date'])

# Función para reconocer el servidor local

@app.get('/')
async def index():
    return {'Hola! Bienvenido a la API de recomedación. Por favor dirigite a /docs'}

@app.get('/about/')
async def about():
    return {'PROYECTO INDIVIDUAL Nº1 -Machine Learning Operations (MLOps)'}


@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes:str):
     # funcion recibe como parametro el mes y retorna la cantidad de peliculas que fueron firmadas en ese mes.
    
    # convertir el mes consultado a minuscula
    mes = mes.lower()
    
    #diccionario de meses con su numero correspondiente
    meses = {
    'enero': 1,
    'febrero': 2,
    'marzo': 3,
    'abril': 4,
    'mayo': 5,
    'junio': 6,
    'julio': 7,
    'agosto': 8,
    'septiembre': 9,
    'octubre': 10,
    'noviembre': 11,
    'diciembre': 12}

    #obtengo el numero del mes consultado
    mes_numero = meses[mes]

    #obtengo los meses en formato numerico y los comparo con el numero del mes consultado y devuelve una serie booleana con valores true
    # Tratamos la excepciòn
    try:
        month_filtered = movies_final[movies_final['release_date'].dt.month == mes_numero]
    except (ValueError, KeyError, TypeError):
        return None

    # Filtramos valores duplicados del dataframe y calculamos
    month_unique = month_filtered.drop_duplicates(subset='id')
    respuesta = month_unique.shape[0]

    #return {f"{respuesta} cantidad de películas fueron estrenadas en el mes de {mes.capitalize()}"}
    return {'mes':mes, 'cantidad':respuesta}

@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia:str):
    # funcion recibe como parametro el dia y retorna la cantidad de peliculas que fueron firmadas en ese dia de la semana.
    
    #diccionario de cada dia, con su valor en ingles para utilixar el metodo day_name()
    days = {
    'lunes': 'Monday',
    'martes': 'Tuesday',
    'miercoles': 'Wednesday',
    'jueves': 'Thursday',
    'viernes': 'Friday',
    'sabado': 'Saturday',
    'domingo': 'Sunday'}

    # convertimos el dia en minuscula y obtengo el dia consultado
    day = days[dia.lower()]

    # obtengo el dia de la columna release_date,Filtramos los duplicados y calculamos
    lista_peliculas_day = movies_final[movies_final['release_date'].dt.day_name() == day].drop_duplicates(subset='id')
    respuesta = lista_peliculas_day.shape[0]

    #return {f"{respuesta} cantidad de películas fueron estrenadas en el dia {dia.capitalize()}"}
    return {'dia':dia, 'cantidad':respuesta}

@app.get('/score_titulo/{titulo}')
def score_titulo(titulo:str):
     # funcion que recibe el nombre de la pelicula y retorna su titulo, año y score
    
    #filtro los datos por medio del titulo y elimino los duplicados
   lista_peliculas_title = movies_final[movies_final['title'] == titulo].drop_duplicates(subset='title')    
   #obtengo el titulo, año y score por su indice
   titulo = str(lista_peliculas_title['title'].iloc[0])
   año = str(lista_peliculas_title['release_year'].iloc[0])
   score =str(lista_peliculas_title['popularity'].iloc[0])
       
   #return {f"la pelicula {titulo} fue estrenada en el año {año} con un score de {score}"}
   return {'titulo':titulo, 'año':año, 'popularidad':score}

@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo:str):
    # funcion que recibe el nombre de la pelicula y retorna su titulo, año, cantidad de votos y promedio de votos
    
    #filtro los datos por medio del titulo y elimino los duplicados
    lista_peliculas_title = movies_final[movies_final['title'] == titulo].drop_duplicates(subset='title')    
    #obtengo el titulo, año, votos y promedio por su indice
    titulo = str(lista_peliculas_title['title'].iloc[0])
    año = str(lista_peliculas_title['release_year'].iloc[0])
    votos = int(lista_peliculas_title['vote_count'].iloc[0])
    votos_promedio = str(lista_peliculas_title['vote_average'].iloc[0])
    
     # Verificar si la variable 'votos' cumple la condición mínima de 2000 valoraciones
    if votos >= 2000:
        #return f"La película {titulo} fue estrenada en el año {año}. La misma cuenta con un total de {votos} valoraciones, con un promedio de {votos_promedio}."
        return {'titulo':titulo, 'año':año, 'voto_total':votos, 'voto_promedio':votos_promedio}    
    else:
        return "La película no cumple con la condición mínima de 2000 valoraciones."
    
@app.get('/get_actor/{nombre_actor}')
def get_actor(nombre_actor:str):
    # funcion que recibe el nombre del actor y retorna nombre,cantidad de peliculas que a participado, retorno conseguido y 
    # promedio del retorno por peliculas
        
    # Filtrar los datos por nombre del actor y eliminar duplicados
    lista_peli_actor = movies_final[movies_final['name_cast'].apply(lambda x: nombre_actor in x)].drop_duplicates(subset='id')
    
    # Verificar si se encontraron registros para el actor
    if len(lista_peli_actor) > 0:
        
        # Obtener las películas en las que ha participado el actor
        peliculas = lista_peli_actor['title'].tolist()        
        cantidad_peliculas = len(peliculas)
        
        #calculamos el retorno y promedio por pelicula
        retorno_conseguido = lista_peli_actor['return'].sum()
        promedio_retorno = retorno_conseguido / cantidad_peliculas
        
        #return f"El actor {nombre_actor} ha participado de {cantidad_peliculas} cantidad de filmaciones, el mismo ha conseguido un retorno de {retorno_conseguido} con un promedio de {promedio_retorno} por filmación"
        return {"nombre": nombre_actor,"cantidad_peliculas": cantidad_peliculas,"retorno_conseguido": retorno_conseguido,"promedio_retorno": promedio_retorno}    
    else:
        return f"No se encontraron registros para el actor {nombre_actor}."
    
@app.get('/get_director/{nombre_director}')
def get_director(nombre_director:str):
    # Filtrar los datos por nombre del director y eliminar duplicados
    lista_peli_director = movies_final[movies_final['name_crew'].apply(lambda x: nombre_director in x)].drop_duplicates(subset='id')
    
    # Verificar si se encontraron registros para el director
    if len(lista_peli_director) > 0:
        # Calcular el éxito del director a través del retorno
        retorno_total = lista_peli_director['return'].sum()
        
        # Crear una lista de diccionarios con la información de cada película
        peliculas_info = []
        for index, row in lista_peli_director.iterrows():
            pelicula_info = {
                "nombre_pelicula": row['title'],
                "fecha_lanzamiento": row['release_date'],
                "retorno_individual": row['return'],
                "costo": row['budget'],
                "ganancia": row['revenue']
            }
            peliculas_info.append(pelicula_info)
        
        return {
            "nombre_director": nombre_director,
            "retorno_total": retorno_total,
            "peliculas_info": peliculas_info
        }
    else:
        return f"No se encontraron registros para el director {nombre_director}."

# Modelo de recomendación

#   Creamos una matriz de conteo usando CountVectorizer que convierte los textos en una matriz de frecuencias de palabras
cv = CountVectorizer(stop_words='english', max_features=5000)
count_matrix = cv.fit_transform(movies_ml['combined_features'])

# Creamos un modelo para encontrar los vecinos mas cercanos en un espacio de caracteristicas
nn = NearestNeighbors(metric='cosine', algorithm='brute')
nn.fit(count_matrix)

# Creamos un indice de titulos de peliculas y eliminamos los duplicados
indices = pd.Series(movies_ml.index, index=movies_ml['title']).drop_duplicates()

#funcion recomendacion
@app.get("/recomendacion/{titulo}")
def recomendacion(titulo: str):
    '''Ingresas un nombre de película y te recomienda 5 similares
    '''
    # Verificamos si el titulo ingresado se encuentra en el dataset
    if titulo not in movies_ml['title'].values:
        return 'La pelicula no se encuentra en el conjunto de la base de datos.'
    else:
        # Obtenemos el índice de la película que coincide con el título
        index = indices[titulo]

        # Obtenemos las puntuaciones de similitud de las 5 peliculas más cercanas
        distances, indices_knn = nn.kneighbors(count_matrix[index], n_neighbors=6)  

        # Obtenemos los indices de las peliculas
        movie_indices = indices_knn[0][1:]  

        # Devolvemos las 5 peliculas mas similares
        return {'lista recomendada': movies_ml['title'].iloc[movie_indices].tolist()}
