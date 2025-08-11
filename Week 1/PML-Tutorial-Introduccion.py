#!/usr/bin/env python
# coding: utf-8

# # Introducción a librerías de manipulación de datos
# A través de este tutorial conocerás algunas de las funcionalidades de la librería Pandas, una de las herramientas más importantes para la exploración y manipulación de un conjunto de datos, así como librerías de visualización de datos como Matplotlib y Seaborn. Particularmente, veremos cómo realizar los siguientes procesos:
# 1. Importar las librerías necesarias.
# 2. Cargar un conjunto de datos.
# 3. Describir o perfilar los datos mediante estadística descriptiva.
# 4. Manipular el conjunto de datos: filtrar, extraer filas y columnas.
# 5. Visualizar variables a través de diferentes tipos de gráficos.
#
# El conjunto de datos que utilizaremos corresponde a la caracterización de casas y su precio. Con estos datos podemos, por ejemplo, descubrir una relación entre el área construida, el número de habitaciones, el año de construcción y el precio del inmueble.
#

# ## 1. Importación de librerías requeridas
#
# Iniciaremos importando las librerias básicas: Pandas, Matplotlib y Seaborn

# In[1]:


# librerías del laboratorio
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# revisar versiones de librerías
from importlib.metadata import version

print(f"Versión de Pandas: {version('pandas')}")
print(f"Versión de Matplotlib: {version('matplotlib')}")
print(f"Versión de Seaborn: {version('seaborn')}")


# ## 2. Carga de datos
#
# Pandas permite la lectura de fuentes de datos almacenadas en archivos con varios formatos. Entre los formatos más comunes para el almacenamiento de conjuntos de datos se encuentran los archivos de valores separados por comas (CSV) y JavaScript Object Notation (JSON).
# Para este tutorial usaremos un conjunto de datos en formato CSV, que leeremos utilizando la función de Pandas `read_csv()`. Para que pueda ser leído por Pandas, tenemos que especificar la ruta en la que está almacenado nuestro archivo fuente.
#
# **Nota:** En este caso, el conjunto de datos se encuentra en una carpeta `data`, que a su vez se encuentra en el mismo directorio que este Notebook. En tu caso, puedes cambiar la ruta de acuerdo con la localización de tus archivos en tu entorno.


data = pd.read_csv("Week 1/kc_house_data.csv")


# Pandas transforma el archivo original en un DataFrame, una estructura de datos de dos dimensiones en la que cada dato está representado con una fila, mientras que cada variable está contenida en una columna. Un DataFrame permite guardar datos de distintos tipos, como caracteres o números de punto flotante.
#
# Para ver algunos de los datos de nuestro conjunto, utilizamos la función `head()` que, por defecto, muestra las primeras 5 filas del DataFrame:

# In[4]:


data.head()


# Además, podemos conocer el tamaño de los datos usando `data.shape`:

# In[5]:


data.shape


# Y podemos revisar los tipos de dato de cada columna usando `data.info()`

# In[6]:


data.info()


# ## 3. Descripción de los datos
#
# Una de las formas más sencillas de obtener una descripción de los datos es mediante la función `describe()`, que retorna algunas medidas estadísticas como la media, la desviación estándar, el mínimo y el máximo de los valores para cada variable.

# In[7]:


data.describe()


# Adicionalmente, para una variable, podemos obtener la cantidad de apariciones de cada valor usando la función `value_counts()`. En este caso, veremos la cantidad de casas que hay por año de construcción en nuestro conjunto de datos:

# In[8]:


data["yr_built"].value_counts()


# ## 4. Consulta y modificación de datos
#
# Muchas veces es necesario consultar algún dato en particular, o extraer una variable del conjunto de datos. Para esto, podemos utilizar algunas de las funciones de Pandas que nos permiten filtrar el DataFrame y obtener subconjuntos según nuestras necesidades.
#
# ### Selección de filas
#
# Pandas ofrece localización por índices, `data.iloc[]`, para seleccionar filas utilizando su posición en el DataFrame (que varía desde 0 hasta n-1, siendo n el número de filas). Por ejemplo, seleccionaremos el dato 101, que tiene índice 100:
#

# In[9]:


data.iloc[100]


# Igualmente, podemos utilizar el operador `:` para extraer un subconjunto de filas de nuestros datos. En este caso, si tenemos un intervalo `n:m`, el resultado incluye el dato `n`, pero excluye el dato `m`:

# In[10]:


data.iloc[10:20]


# ### Selección de columnas
#
# Por otro lado, utilizaremos la localización por etiquetas, `data.loc[]`, para obtener columnas (variables) de nuestro conjunto de datos. En este código, el operador `:` indica que queremos todas las filas, mientras que el String (o cadena de caracteres) `'price'` es el nombre de la columna de interés:

# In[11]:


data.loc[:, "price"]


# También podemos utilizar la localización por índices, aunque es menos explícito:

# In[12]:


data.iloc[:, 2]


# Para seleccionar múltiples columnas podemos usar un arreglo de etiquetas en vez de una sola etiqueta:

# In[13]:


data.loc[:, ["price", "sqft_living"]]


# ### Condicionales y filtros
#
# Pandas permite evaluar condicionales para un conjunto de datos utilizando cualquiera de los tipos de localización. En este caso, utilizaremos la localización por etiquetas y compararemos el resultado con un valor. Por ejemplo, evaluaremos si cada casa tiene un precio mayor a 500,000 dólares:

# In[14]:


data.loc[:, "price"] > 500000


# El resultado es una lista o un DataFrame con valores booleanos. En este caso, se tiene una lista de 21,613 posiciones con valores verdaderos o falsos. Esta evaluación nos permite filtrar el DataFrame, colocando la linea de código anterior dentro de una localización por etiquetas:

# In[15]:


data.loc[data.loc[:, "price"] > 500000]


# ## 5. Visualización de datos
#
# Podemos generar gráficos que nos permitan entender un poco mejor la naturaleza de nuestros datos.
#
# ### Matplotlib
#
# Inicialmente vamos a crear una gráfica para observar la distribución de años de construcción en nuestro conjunto de datos. Esta gráfica se crea de la siguiente forma:
#
# * `figure()`: crea un nuevo gráfico, el argumento `figsize` se utiliza para modificar su tamaño, usando valores en pulgadas para cada dimensión. Recuerda que la estructura básica que representa un gráfico es la "figura".
# * `bar()`: especifica que se trata de una gráfica de barras, y la dibuja sobre la figura usando los datos de la variable `x` y de la variable `y`.
# * `title()`: añade un título al gráfico.
# * `xticks()`: modifica las etiquetas del eje x. En este caso, rotamos las etiquetas 90°.
#
# **Nota:** `% matplotlib inline` es un llamado a una función que permite que las gráficas se muestren correctamente en Jupyter Notebooks. Si en algún momento no aparecen tus gráficas, puedes regresar a esta celda, ejecutarla nuevamente y volver al punto en el que estabas.

# In[16]:


try:
	get_ipython().run_line_magic("matplotlib", "inline")
except NameError:
	pass


# In[17]:


plt.figure(figsize=(16, 6))

# Retorna una serie con la cantidad de apariciones de cada valor
plot_data = data["yr_built"].value_counts()

# Retorna todos los valores únicos que puede tomar la variable yr_built
x = plot_data.index
# Retorna las veces que cada valor aparece en los datos
y = plot_data.values
plt.bar(x, y)

plt.title("Distribución de Años de construcción")
plt.xticks(rotation=90)

plt.show()


# Adicionalmente podemos crear histogramas, gráficas que representan la frecuencia de variables con valores numéricos en un intervalo continuo. Para esto, utilizamos la función `hist()`, especificando la variable y el número de intervalos (con el argumento `bins`):

# In[18]:


plt.figure(figsize=(16, 6))

# En este caso utilizamos directamente el DataFrame
# Sin embargo, "x" también puede ser una consulta con localización por índices o etiquetas
x = data["price"]

plt.hist(x, bins=50)
plt.title("Precio")
plt.show()


# Otra gráfica disponible es la de líneas o puntos, que podemos utilizar para observar relaciones entre variables. En este caso, observaremos la relación entre el área social de las casas y su precio. Es importante resaltar que `plot()` está recibiendo los siguientes argumentos:
#
# * `data['sqft_living']`: datos del eje x.
# * `data['price']`: datos del eje y.
# * `'.'`: formato de los puntos. Algunos de los formatos válidos pueden ser `'*'` para estrellas o `'o'` para círculos.
# * `color='blue'`: color de los puntos.

# In[19]:


plt.figure(figsize=(10, 10))

x = data["sqft_living"]
y = data["price"]

plt.plot(x, y, ".", color="blue")
plt.title("Área vs Precio")
plt.xlabel("Área")
plt.ylabel("Precio")
plt.show()


# ### Seaborn
#
# Otra librería para visualización es Seaborn, con la que podemos realizar los mismos tipos de gráficos. Por ejemplo, utilizamos `distplot()` para crear el mismo histograma de los precios, usando los siguientes argumentos:
#
# * `data['price']`: datos del eje x.
# * `kde=True`: este parámetro computa un estimado de la distribución de la variable, que se verá como una curva sobre el histograma.

# In[20]:


plt.figure(figsize=(16, 6))
plt.tight_layout()

x = data["price"]

sns.distplot(x, kde=True)


# Incluso, podemos visualizar las relaciones que hay entre variables, para saber si hay variables que dependen de otras. Para esto, podemos hacer uso de un mapa de calor (con la función `heatmap()`), calculando las correlaciones de nuestro DataFrame usando `data.corr()`:
#
# _Nota: el parámetro `numeric_only=True` evita errores causados por datos que no son números_

# In[21]:


sns.heatmap(data.corr(numeric_only=True))


# El resultado muestra con colores qué tan relacionada está una variable. En este caso, entre más claro sea el color, más relacionadas están las variables de la fila y columna correspondientes.

# ## Cierre
#
# En este tutorial hemos utilizado algunas de las funcionalidades básicas de Pandas para explorar, analizar y consultar un conjunto de datos, además de crear visualizaciones simples de nuestros datos mediante Matplotlib y Seaborn. Estas librerías constituyen la base para el entendimiento de los datos, el paso más importante en la construcción de modelos de aprendizaje automático.
#
# ---
# Para la carga de datos en formato CSV puedes consultar [este enlace](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
#
# Para más información sobre el método `plot()` en Matplotlib puedes consultar [este enlace](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
#
# Finalmente, para obtener más información sobre los tipos de gráficas utilizados con Seaborn puedes consultar la documentación de [histplot()](https://seaborn.pydata.org/generated/seaborn.histplot.html) y de [heatmap()](https://seaborn.pydata.org/generated/seaborn.heatmap.html)
#
# ---
# *Creado por: Nicolás Díaz*
#
# *Última edición: Camilo Rozo*
#
# *Revisado por: Haydemar Nuñez*
#
# *Versión de: Enero 20, 2025*
#
# *Universidad de los Andes*

# In[ ]:
