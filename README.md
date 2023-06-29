# proyecto1_mlops API de datos y recomendaciones de películas

# Introduccion

El proyecto de Sistema de Recomendación de Películas utilizando Machine Learning tiene como objetivo desarrollar un sistema capaz de recomendar películas personalizadas a los usuarios. Mediante el uso de técnicas de aprendizaje automático, el sistema analiza los patrones y preferencias del usuario basándose en datos históricos y características de las películas para ofrecer recomendaciones relevantes y precisas.

El proyecto se divide en dos partes principales: el proceso de ingeniería de datos y el desarrollo del modelo de machine learning. En la etapa de ingeniería de datos, se realiza un proceso de extracción, transformación y carga (ETL) para obtener los datos necesarios. Luego, se utiliza el framework de FastAPI para consumir los datos ya limpios y se implementan varias funciones para realizar consultas y obtener diferente tipo de informacion. Finalmente, se realiza el despliegue del sistema en Render, lo que permite acceder a través de un servicio web.

En la etapa de machine learning, se realiza un análisis exploratorio de datos (EDA) para comprender la distribución, correlaciones y características de los datos. Con base en este análisis, se seleccionan las mejores columnas que utilizará el algoritmo KNN (K-Nearest Neighbors) para realizar las predicciones y recomendaciones. Mediante una función específica, se solicita el nombre de una pelicula y se generan cinco recomendaciones de películas personalizadas.

# Objetivos

El proyecto tiene los siguientes objetivos:


- Realizar un proceso de ingeniería de datos eficiente, incluyendo la extracción, transformación y carga de los datos necesarios para el sistema.
- Utilizar el framework de FastAPI para crear una interfaz web que permita la consulta y obtención de recomendaciones personalizadas.
- Implementar funciones para realizar consultas específicas.
- Desplegar el sistema en Render para que pueda ser accesible a través de un servicio web.
- Realizar un análisis exploratorio de datos para comprender las características y patrones de los datos.
- Seleccionar las mejores columnas y utilizar el algoritmo KNN para realizar las predicciones y recomendaciones de películas.
- Desarrollar un sistema de recomendación de películas utilizando técnicas de machine learning.
- Proporcionar una experiencia de usuario satisfactoria al ofrecer recomendaciones relevantes y precisas basadas en las preferencias del usuario.

Estos objetivos guían el desarrollo del proyecto, permitiendo la creación de un sistema de recomendación de películas efectivo y fácil de usar.

# Datos

En este proyecto, se utilizan tres conjuntos de datos distintos que ya han pasado por el proceso ETL, para diferentes etapas del proceso. A continuación, se describen brevemente ambos conjuntos:

[movies_final](https://github.com/mwmartinez/proyecto1_mlops/blob/main/movies_ml.csv) Este conjunto de datos es el resultado de la etapa de ingeniería de datos (ETL) y utilizado en el desarrollo del framework de FastAPI, Contiene información de las películas para realizar sus consultas.

[movies_eda]() Este conjunto de datos es utilizado en el analisis exploratorio y poder realizar todos los graficos, correlaciones y sacar conclusiones para ser usadas en las predicciones.

[movies_ml](https://github.com/mwmartinez/proyecto1_mlops/blob/main/movies_ml.csv) Este conjunto de datos es utilizado en el proceso de desarrollo del modelo de machine learning.

# Ingenieria de datos

En esta etapa del proyecto, se asumió el rol de un ingeniero de datos para llevar a cabo el proceso de Extracción, Transformación y Carga (ETL) de los datos. El objetivo principal fue obtener dos archivos de tipo CSV llamados "movies" y "credits".

A continuación, se describen las principales transformaciones realizadas durante el proceso de ETL:

- Desanidación de columnas: Si se encontraron columnas anidadas o estructuras de datos complejas, se aplicaron técnicas de desanidación para separar los valores en columnas individuales. Esto permitió una mejor comprensión y manipulación de los datos.

- Tratamiento de valores nulos: Se identificaron y se realizaron acciones para manejar los valores nulos en el conjunto de datos. Esto incluyó opciones como eliminar las filas o columnas con valores nulos, reemplazarlos con valores predeterminados o aplicar técnicas de imputación para llenar los valores faltantes.

- Cambio de tipos de datos: Se realizaron cambios en los tipos de datos de ciertas columnas para asegurar su correcta interpretación. Esto incluyó convertir columnas de tipo texto a fechas, numéricas o categóricas, según fuera necesario.

- Creación de columnas nuevas: Se generaron nuevas columnas a partir de las existentes, utilizando fórmulas, funciones o cálculos específicos. Estas columnas adicionales proporcionaron información adicional o resumida para el análisis posterior.

- Eliminación de columnas innecesarias: Si se identificaron columnas que no aportaban información relevante o duplicada, se eliminaron del conjunto de datos. Esto ayudó a reducir la complejidad y el tamaño del conjunto de datos resultante.

- Unión de archivos: Se combinaron los archivos "movies" y "credits" en un único conjunto de datos, utilizando una o más columnas clave para realizar la unión. Esto permitió tener toda la información relacionada en un único archivo para un análisis más completo.

- Filtrado de datos: Se aplicó un filtrado en el conjunto de datos para crear un dataset de menor tamaño que pudiera ser consumido por la API. Esto implicó seleccionar un subconjunto de filas o columnas basado en criterios específicos, como fechas, categorías o valores específicos.

En resumen, el proceso de ingeniería de datos involucró una serie de transformaciones y manipulaciones en los datos originales, con el fin de obtener nuevos archivos. Estos archivos resultantes fueron optimizados y listos para ser utilizados en etapas posteriores del proyecto, como el desarrollo de la API.

El archivo lo puedes visualizar aqui [ETL.ipynb](https://github.com/mwmartinez/proyecto1_mlops/blob/main/ETL.ipynb)

# API 

se utilizo el framework FastApi para realizar los endpoint en el cual fueron los siguientes

- def **cantidad_filmaciones_mes( *`Mes`* )**: Se ingresa un mes en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.
- def **cantidad_filmaciones_dia( *`Dia`* )**: Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.
- def **score_titulo( *`titulo_de_la_filmación`* )**: Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score. 
- def **votos_titulo( *`titulo_de_la_filmación`* )**: Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. La misma variable deberá de contar con al menos 2000 valoraciones, caso contrario, debemos contar con un mensaje avisando que no cumple esta condición y que por ende, no se devuelve ningun valor.
- def **get_actor( *`nombre_actor`* )**: Se ingresa el nombre de un actor que se encuentre dentro del dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas que en las que ha participado y el promedio de retorno.
- def **get_director( *`nombre_director`* )**: Se ingresa el nombre de un director que se encuentre dentro del dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

el archivo lo puedes visualizar aqui [main.py](https://github.com/mwmartinez/proyecto1_mlops/blob/main/main.py)

# ANALISIS EXPLORATORIO DE LOS DATOS

En este proyecto, se realizó un análisis exploratorio de los datos con el objetivo de obtener un mejor entendimiento del dataset utilizado. Se utilizaron diversas técnicas visuales, como histogramas, scatter plots, boxplots, gráficos de barras, nubes de palabras y correlaciones, para analizar los diferentes tipos de datos numéricos y categóricos presentes en el conjunto de datos.

- Histogramas
Los histogramas permiten visualizar la distribución de datos numéricos. Se utilizaron para analizar variables como la edad, el ingreso, o cualquier otra variable cuantitativa en el conjunto de datos. Los histogramas nos brindaron información sobre la concentración de valores y la forma de la distribución.

- Scatter Plots
Los scatter plots son gráficos que representan la relación entre dos variables numéricas. Se utilizaron para identificar posibles relaciones o patrones entre diferentes variables del conjunto de datos. Estos gráficos nos permitieron detectar la presencia de correlaciones positivas, negativas o ausencia de correlación entre las variables.

- Boxplots
Los boxplots son diagramas que muestran la distribución de una variable numérica a través de su mediana, cuartiles y posibles valores atípicos. Se utilizaron para visualizar la dispersión y la presencia de valores atípicos en variables como el salario, la puntuación, etc.

- Gráficos de Barras
Los gráficos de barras se utilizaron para analizar variables categóricas, como el género, la categoría de productos, etc. Estos gráficos nos permitieron identificar la frecuencia de cada categoría y comparar diferentes categorías entre sí.

- Nubes de Palabras
Las nubes de palabras se utilizaron para visualizar las palabras más frecuentes o importantes en un texto o conjunto de textos. Se emplearon para analizar variables de texto, como las descripciones de productos, reseñas de clientes, etc. Esto nos permitió identificar palabras clave o temas dominantes en los datos.

- Correlación
El análisis de correlación se utilizó para evaluar la relación entre diferentes variables numéricas. Se calcularon coeficientes de correlación, como el coeficiente de correlación de Pearson, para determinar la fuerza y la dirección de la relación entre variables. Esto nos ayudó a identificar posibles dependencias entre variables y comprender mejor su impacto en el conjunto de datos.

En conclusión, mediante el análisis exploratorio de los datos utilizando diversas técnicas visuales, se obtuvo un mejor entendimiento del conjunto de datos. Esto permitió identificar patrones, tendencias, valores atípicos y posibles relaciones entre variables, lo que sentó las bases para el modelo de machine learning.

El archivo lo puedes observar aqui [EDA_ML.ipynb](https://github.com/mwmartinez/proyecto1_mlops/blob/main/EDA_ML.ipynb)

# MACHINE LEARNING

En esta etapa del proyecto, se utilizó el Machine Learning para construir un modelo de recomendación de películas basado en el algoritmo de K-Vecinos (K-Nearest Neighbors). A continuación, se describen los pasos principales seguidos en el proceso:

- Filtrado del dataset: Se aplicó un filtro en el conjunto de datos para seleccionar únicamente las películas estrenadas a partir de 1970, ya que se observó un gran crecimiento a partir de dicho año. Además, se aplicaron filtros adicionales basados en los puntajes obtenidos por las películas, utilizando la columna "vote_average". Estos filtros ayudaron a reducir el conjunto de datos y enfocarse en las películas más relevantes.

- Unión de texto: Se realizó la unión de los textos de las columnas "overview", "genres" y "production_companies" en un solo campo llamado "combined_features". Esta concatenación permitió tener un campo que contiene información relevante sobre la película, que el algoritmo de Machine Learning pueda utilizar para calcular la similitud entre las películas.

- Construcción del modelo de K-Vecinos: Se implementó el algoritmo de K-Vecinos (K-Nearest Neighbors) para construir el modelo de recomendación. Este modelo encuentra las películas más cercanas en función de características similares y genera recomendaciones basadas en esa cercanía.

- Generación de recomendaciones: Una vez construido el modelo de K-Vecinos, se utilizó para generar recomendaciones de películas. El modelo analiza las características y similitudes entre las películas del conjunto de datos y selecciona las películas más cercanas en función de características similares para recomendar al usuario.

En conclusión, mediante el uso de Machine Learning se construyó un modelo de recomendación de películas basado en el algoritmo de K-Vecinos. Este modelo utiliza características similares entre las películas para generar recomendaciones personalizadas. El objetivo es proporcionar al usuario una lista de películas que sean similares a las que le han gustado previamente, basándose en las características de las películas y las preferencias del usuario.

El archivo lo puedes observar aqui [EDA_ML.ipynb](https://github.com/mwmartinez/proyecto1_mlops/blob/main/EDA_ML.ipynb)

# DEPLOY

Para el despliegue de la API, se utilizó la plataforma Render. Los datos del proyecto están listos para ser consumidos y consultados a través del siguiente enlace [proyecto](https://proyecto-machine-learning-operations.onrender.com)

En el enlace al deploy agregas /docs a la direccion web y te dirrecciona a la documentacion de la api y podras utilizar las diferentes consultas.

Al acceder al enlace proporcionado, los usuarios podrán realizar consultas y obtener recomendaciones de películas basadas en el modelo de Machine Learning implementado.

La plataforma Render proporciona un entorno estable y escalable para alojar y ejecutar la API, asegurando un rendimiento confiable y seguro para los usuarios.

# Video

En el siguiente enlace puedes observar la explicacion del proyecto en cada una de sus funciones [video]()

# Herramientas tecnologicas

Durante el desarrollo de este proyecto de Machine Learning, se utilizaron las siguientes herramientas tecnológicas:

[Visual Studio Code](https://code.visualstudio.com/): Se utilizó como entorno de desarrollo integrado (IDE) para escribir y editar el código fuente. Visual Studio Code ofrece una amplia gama de extensiones y funcionalidades que facilitan el desarrollo y la depuración de aplicaciones.

[Python](https://www.python.org/): Se utilizó el lenguaje de programación Python como el principal para la implementación del modelo de Machine Learning. Python es ampliamente utilizado en el ámbito de la ciencia de datos y el aprendizaje automático debido a su gran cantidad de bibliotecas y su facilidad de uso.

[FastAPI](https://fastapi.tiangolo.com/): Se empleó el framework de desarrollo web FastAPI para crear y exponer la API que proporciona las recomendaciones de películas. FastAPI es conocido por su alto rendimiento y facilidad de desarrollo, lo que lo convierte en una excelente opción para construir APIs rápidas y escalables.

[Render](https://render.com/): Se utilizó la plataforma Render para el despliegue de la API. Render es una plataforma de alojamiento y despliegue de aplicaciones que ofrece un entorno estable y escalable. Proporciona una infraestructura confiable para ejecutar la API y asegura un rendimiento óptimo.

Estas herramientas tecnológicas fueron seleccionadas para garantizar un desarrollo eficiente y efectivo del proyecto de Machine Learning. Cada una de ellas desempeña un papel importante en el proceso, desde la escritura del código hasta el despliegue de la API, contribuyendo al éxito general del proyecto.








