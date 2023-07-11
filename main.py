from fastapi import FastAPI
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('dataset_api.csv')
df_modelo = pd.read_csv('dataset_modelo10k.csv')

app = FastAPI()

@app.get('/')
def index():
    return {'Saludo': "PI-ML SH de Maximiliano Vaca Coll"}

@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma: str):
    conteo = int((df["original_language"] == str(idioma)).sum())
    idioma = idioma.upper()
    return {'idioma': idioma, 'cantidad': conteo}

@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula: str):
    pelicula = pelicula.lower()
    pelicula_info = df[df['title'].str.lower() == pelicula]
    if not pelicula_info.empty:
        release_year = int(pelicula_info['release_year'].iloc[0])
        runtime = int(pelicula_info['runtime'].iloc[0])
    else:
        release_year = 'No se encontro la pelicula'
        runtime = 'No se encontro la pelicula'
        pelicula = 'No se encontro la pelicula'
        pelicula = pelicula.title()
    return {'pelicula':pelicula, 'duracion':runtime, 'anio':release_year}


@app.get('/franquicia/{franquicia}')
def franquicia(franquicia: str):
    production_company = franquicia.upper()
    # Cantidad de títulos por franquicia
    titulos = df[df['belongs_to_collection'].str.upper() == production_company]['title'].to_dict()
    cantidad = len(titulos)
    # ganancia total de la franquicia
    gananciatotal = pd.to_numeric(df[df['belongs_to_collection'].str.upper() == production_company]['budget'], errors='coerce') * pd.to_numeric(df[df['belongs_to_collection'].str.upper() == production_company]['return'], errors='coerce')
    gananciatotal = gananciatotal.sum()
    # Promedio de la ganancia total de la franquicia por pelicula
    promedio = pd.to_numeric(df[df['belongs_to_collection'].str.upper() == production_company]['budget'], errors='coerce') * pd.to_numeric(df[df['belongs_to_collection'].str.upper() == production_company]['return'], errors='coerce')
    promedio = promedio.mean()
    franquicia = franquicia.title()
    return {'franquicia': franquicia, 'cantidad': cantidad, 'titulos': titulos, 'ganancia_total': gananciatotal, 'ganancia_promedio': promedio}


@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais: str):
    df['production_countries'] = df['production_countries'].apply(lambda x: [] if pd.isnull(x) else x)
    cantidad = int(df[df['production_countries'].apply(lambda x: pais in x if x is not None else False)]['title'].count())
    pais = pais.title()
    return {'pais': pais, 'cantidad': cantidad}


@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora:str):
    # Cantidad de títulos por compañía de producción
    titulos = int(df[df['production_companies'].str.contains(productora, na=False)]['title'].count())
    # Suma de revenue por compañía de producción
    revenue_total = int(df[df['production_companies'].str.contains(productora, na=False)]['revenue'].sum())
    return {'productora': productora, 'revenue_total': revenue_total, 'cantidad': titulos}




@app.get('/get_director/{nombre_director}')
def get_director(nombre_director: str):
    df_filtrado = df[df['director_name'] == nombre_director]
    df_indexado = df_filtrado.set_index('title')
    promedio_return = df_filtrado['return'].mean()
    lista_peliculas = df_filtrado['title'].tolist()
    dict_anios = dict(zip(df_indexado.index, df_indexado['release_year'].tolist()))
    dict_return = dict(zip(df_indexado.index, df_indexado['return'].tolist()))
    dict_budget = dict(zip(df_indexado.index, df_indexado['budget'].tolist()))
    dict_revenue = dict(zip(df_indexado.index, df_indexado['revenue'].tolist()))
    return {'director':nombre_director, 'retorno_total_director':promedio_return, 
    'peliculas':lista_peliculas, 'anio':dict_anios, 'retorno_pelicula':dict_return, 
    'budget_pelicula':dict_budget, 'revenue_pelicula':dict_revenue}

    # ML
@app.get('/recomendacion/{titulo}')
def get_recomendacion(titulo: str):
    reference_index = df_modelo[df_modelo['title'] == titulo].index[0]

    # Obtener el vector de características del título de referencia
    reference_vector = df_modelo.iloc[reference_index, 3:]  # Columnas de género

    # Calcular la similitud del coseno entre el vector de referencia y todos los demás vectores
    similarity_scores = cosine_similarity([reference_vector], df_modelo.iloc[:, 3:])

    # Obtener los índices de las 5 películas más similares
    top_indices = similarity_scores.argsort()[0][-6:-1]  # Excluimos el índice de referencia

    # Obtener los títulos de las películas recomendadas
    recommended_titles = df_modelo.iloc[top_indices]['title']

    return {'lista recomendada': recommended_titles}