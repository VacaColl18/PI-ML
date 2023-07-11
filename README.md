# Proyecto Personal: Machine Learning Operations (MLOps)
¡Bienvenid@ a mi proyecto personal de Machine Learning Operations (MLOps)!

## Descripción del proyecto

En este proyecto, asumí el rol de un MLOps Engineer en una start-up que provee servicios de agregación de plataformas de streaming. El objetivo principal fue crear un sistema de recomendación como mi primer modelo de Machine Learning para solucionar un problema de negocio. Al revisar los datos disponibles, encontré que la calidad de los mismos era baja y no estaban listos para su procesamiento. Esto implicó realizar un trabajo de Data Engineering para transformar los datos y obtener un Minimum Viable Product (MVP) para el cierre del proyecto.

El proyecto abordó el ciclo de vida completo de un proyecto de Machine Learning, desde el tratamiento  de datos hasta el entrenamiento y mantenimiento del modelo de ML. Además, se desarrolló una API utilizando el framework FastAPI para disponibilizar los datos de la empresa y se implementaron diferentes consultas para interactuar.
También realicé un análisis exploratorio de datos (EDA) para investigar las relaciones entre las variables del dataset, identificar outliers o anomalías, y descubrir patrones interesantes que podrían ser útiles en análisis posteriores. Tamnien, desarrollé un sistema de recomendación basado en películas similares utilizando técnicas de cálculo de similitud.

## Tareas realizadas

Durante el desarrollo del proyecto, se llevaron a cabo las siguientes tareas:
Transformaciones de datos (ETL)

Se realizaron transformaciones de datos para prepararlos para su uso en el sistema de recomendación. Estas transformaciones incluyeron:

Desanidar campos anidados como belongs_to_collection y production_companies para poder utilizarlos en consultas posteriores.

Rellenar los valores nulos de los campos revenue y budget con 0.

Eliminar los valores nulos del campo release date.

Establecer el formato de las fechas en AAAA-mm-dd y crear la columna release_year para extraer el año de la fecha de estreno.

Crear la columna return para calcular el retorno de inversión dividiendo los campos revenue entre budget, asignando 0 en caso de que no haya datos disponibles.

Eliminar las columnas innecesarias como video, imdb_id, adult, original_title, poster_path y homepage.

## Desarrollo de la API (FastAPI)

Se desarrolló una API utilizando el framework FastAPI para disponibilizar los datos de la empresa. Se implementaron las siguientes consultas:

peliculas_idioma(Idioma: str): Devuelve la cantidad de películas producidas en un idioma especificado.

peliculas_duracion(Pelicula: str): Devuelve la duración y el año de una película específica.

franquicia(Franquicia: str): Devuelve la cantidad de películas, ganancia total y promedio de una franquicia específica.

peliculas_pais(Pais: str): Devuelve la cantidad de películas producidas en un país especificado.

productoras_exitosas(Productora: str): Devuelve el revenue total y la cantidad de películas realizadas por una productora específica.

get_director(nombre_director): Devuelve el éxito de un director específico medido a través del retorno, junto con el nombre de cada película, fecha de lanzamiento, retorno individual, costo y ganancia.

## Deployment

El proyecto se deployó utilizando el servicio Render para que la API sea consumible desde la web. Puedes acceder a la API y consultar la documentación en el siguiente enlace: https://proyectoml-vacacoll18.onrender.com/docs

## Análisis exploratorio de datos (EDA)

Se realizó un análisis exploratorio de datos (EDA) para investigar las relaciones entre las variables del dataset y descubrir patrones. Se utilizaron técnicas de visualización y se generaron gráficas. El EDA se llevó a cabo sin utilizar librerías para obtener un mayor conocimiento y práctica en los conceptos y tareas involucradas en el análisis exploratorio.

## Sistema de recomendación

Se desarrolló un sistema de recomendación basado en películas similares. Se calculó la similitud de puntuación entre una película dada y el resto de películas utilizando técnicas de cálculo de similitud. Las películas se ordenaron según el score de similaridad y se generó una lista de Python con los 5 nombres de películas con mayor puntaje, en orden descendente. Esta función adicional, llamada recomendacion(titulo), fue implementada en la API.

## Repositorio y archivos relevantes

En el repositorio de GitHub GitHub - VacaColl18/PI-ML, puedes encontrar los siguientes archivos relevantes:

ETL: El archivo ETL contiene el código y los detalles de las transformaciones de datos realizadas en el proyecto.

Funciones: En el archivo de funciones, se encuentran los códigos correspondientes a las funciones implementadas para los endpoints de la API. Cada función se asocia a una consulta específica mencionada previamente.

EDA: El archivo EDA contiene el código y las visualizaciones generadas durante el análisis exploratorio de datos. Aquí se exploraron lasrelaciones entre las variables del dataset, se identificaron outliers o anomalías y se buscaron patrones interesantes.

Además de estos archivos, el repositorio también puede contener otros recursos relevantes como datos adicionales, documentación adicional o notebooks utilizados en el proceso de desarrollo.

# Conclusiones

En este proyecto personal de Machine Learning Operations (MLOps), asumí el rol de un MLOps Engineer y trabajé en la creación de un sistema de recomendación de películas para una start-up de agregación de plataformas de streaming. Realicé tareas de Data Engineering, desarrollé una API utilizando FastAPI, realicé análisis exploratorio de datos (EDA) y creé un sistema de recomendación basado en películas similares.

A lo largo del proyecto, adquirí experiencia en el manejo y transformación de datos, implementé consultas en una API, realicé análisis exploratorio de datos y utilicé técnicas de cálculo de similitud para recomendar películas. El despliegue de la API permitió que los departamentos de Analytics y Machine Learning pudieran consumir los datos y utilizar el sistema de recomendación en sus procesos.

El repositorio de GitHub https://github.com/VacaColl18/PI-ML contiene todos los archivos relevantes y el código desarrollado durante el proyecto. También puedes acceder a la API y consultar la documentación en el siguiente enlace: https://proyectoml-vacacoll18.onrender.com/docs

¡Gracias por revisar mi proyecto personal de MLOps! Si tienes alguna pregunta o necesitas más información, no dudes en contactarme.


