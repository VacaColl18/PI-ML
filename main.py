from fastapi import FastAPI
import pandas as pd

df = pd.read_csv('dataset_api.csv')

app = FastAPI()

@app.get('/')
def index():
    return {'Saludo': "Proyecto de Maximiliano Vaca Coll"}

@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma: str):
    conteo = int((df["original_language"] == str(idioma)).sum())
    return {'idioma': idioma, 'cantidad': conteo}

@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula:str):
    pelicula = pelicula.upper()
    pelicula_info = df[df['title'].str.upper() == pelicula]
    if not pelicula_info.empty:
        release_year = int(pelicula_info['release_year'].iloc[0])
        runtime = int(pelicula_info['runtime'].iloc[0])
    else:
        release_year = 'No se encontro la pelicula'
        runtime = 'No se encontro la pelicula'
        pelicula = 'No se encontro la pelicula'
    return {'pelicula':pelicula, 'duracion':runtime, 'anio':release_year}

@app.get('/franquicia/{franquicia}')
def franquicia(franquicia: str):
    production_company = franquicia.upper()
    # Consulta 1: Cantidad de títulos por franquicia
    titulos = df[df['belongs_to_collection'].str.upper() == production_company]['title'].to_dict()
    cantidad = len(titulos)
    # Consulta 2: ganancia total de la franquicia
    gananciatotal = pd.to_numeric(df[df['belongs_to_collection'].str.upper() == production_company]['budget'], errors='coerce') * pd.to_numeric(df[df['belongs_to_collection'].str.upper() == production_company]['return'], errors='coerce')
    gananciatotal = gananciatotal.sum()
    # Consulta 3: Promedio de la ganancia total de la franquicia por pelicula
    promedio = pd.to_numeric(df[df['belongs_to_collection'].str.upper() == production_company]['budget'], errors='coerce') * pd.to_numeric(df[df['belongs_to_collection'].str.upper() == production_company]['return'], errors='coerce')
    promedio = promedio.mean()
    return {'franquicia': franquicia, 'cantidad': cantidad, 'titulos': titulos, 'ganancia_total': gananciatotal, 'ganancia_promedio': promedio}


@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais: str):
    #pais = pais.upper()
    df['production_countries'] = df['production_countries'].apply(lambda x: [] if pd.isnull(x) else x)
    cantidad = int(df[df['production_countries'].apply(lambda x: pais in x if x is not None else False)]['title'].count())
    return {'pais': pais, 'cantidad': cantidad}


@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora:str):
    # Consulta 1: Cantidad de títulos por compañía de producción
    titulos = int(df[df['production_companies'].str.contains(productora, na=False)]['title'].count())
    # Consulta 2: Suma de revenue por compañía de producción
    revenue_total = int(df[df['production_companies'].str.contains(productora, na=False)]['revenue'].sum())
    return {'productora': productora, 'revenue_total': revenue_total, 'cantidad': titulos}




@app.get('/get_director/{nombre_director}')
def get_director(nombre_director: str):
    df_filtrado = df[df['director_name'] == nombre_director]
    promedio_return = df_filtrado['return'].mean()
    df_indexado = df_filtrado.set_index('title')
    lista_peliculas = df_filtrado['title'].tolist()
    dict_anios = dict(zip(df_indexado.index, df_indexado['release_year'].tolist()))
    dict_return = dict(zip(df_indexado.index, df_indexado['return'].tolist()))
    dict_budget = dict(zip(df_indexado.index, df_indexado['budget'].tolist()))
    dict_revenue = dict(zip(df_indexado.index, df_indexado['revenue'].tolist()))
    return {'director':nombre_director, 'retorno_total_director':promedio_return, 
    'peliculas':lista_peliculas, 'anio':dict_anios, 'retorno_pelicula':dict_return, 
    'budget_pelicula':dict_budget, 'revenue_pelicula':dict_revenue}

    # ML
"""@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''
    return {'lista recomendada': respuesta}"""


