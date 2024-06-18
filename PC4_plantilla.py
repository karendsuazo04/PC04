# Este código sirve para instalar Streamlit en tu computadora y hacer un primer programa en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# streamlit hello

# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
#  streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

# Si usas el siguiente código mostrará un título en la aplicación Streamlit. 
# st.title("Nombre de tu blog"): Esta línea está creando un título en la aplicación web.
# Pero, a diferencia de st.markdown, el texto estará alineado a la izquierda y no podrás cambiar el color del texto.

# La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
st.markdown("<h1 style='text-align: center;'>A publicist coding journal</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
# La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
# el atributo style se utiliza para agregar estilos CSS. 
# En este caso, el texto está alineado al centro (text-align: center;). 
# El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

# unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad. 
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

# Creamos dos columnas separadas para la imagen y el texto
col1, col2 = st.columns(2)

# col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
# La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
# Las columnas creadas se asignan a las variables col1 y col2.

# En la primera columna colocamos la imagen
col1.image("karen.jpeg", caption='Karen Davila', width=300)

# col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
# La función image toma como primer argumento la ruta de la imagen que se va a mostrar. 
# En este caso, la imagen es "ellie.png". 
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen, en este caso 'Ellie'. 
# El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

# En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
# Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
# ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

texto = """
Mi nombre es Karen y tengo 19 años. Actualmente vivo en Lima y estoy cursando el quinto ciclo de la carrera de Publicidad en la PUCP. Yo escogí esta carrera porque soy una persona muy curiosa y tengo mucho interés en diversas disciplinas, por lo tanto, cuando estaba en el proceso de escoger una profesión, me di cuenta que la carrera de publicidad se caracteriza por instrumentalizar conocimientos de otras áreas como por ejemplos la psicología, sociología, antropología, etc. En un futuro, me gustaría trabajar en el área de planning de alguna agencia de red como Mccann. Asimismo, un gran sueño a futuro sería poder tener mi propia agencia. En mis ratos libres, me gusta hacer ejercicio como ir al gimnasio o jugar volleyball. También me gusta cocinar comida peruana y aprender idiomas. Hasta el momento hablo inglés y francés a un nivel avanzado, y en un futuro me gustaría aprender alemán y italiano.

"""

# Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
# Mostramos el texto
col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
# La etiqueta <div> se utiliza para agrupar contenido en HTML. 
# En este caso, el texto está justificado (text-align: justify;). 
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto.

# f"": Esta es una cadena de formato en Python. 
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena. 
# En este caso, {texto} se reemplaza por el valor de la variable texto.


# Debajo de las columnas colocamos un subtítulo que describa tu experiencia aprendiendo a programar
# Deben presentar tu experiencia aprendiendo a programar: ¿Cómo te sentiste al principio?, 
# ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
# ¿Qué te gustaría hacer con la programación en el futuro? 

# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Mi experiencia aprendiendo a programar </h2>", unsafe_allow_html=True)

# <h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>: Esta es una cadena de código HTML.
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Mi experiencia aprendiendo a programar 💻") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad.
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
# Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.

# Agregar un  texto para la respuesta
texto_2 = """
Al principio, me sentía un poco intimidada porque siempre había asociado la programación con matemáticas complicadas y lógica avanzada, algo muy alejado de mi campo de estudio. Sin embargo, a medida que avanzaba en las lecciones, me di cuenta de que Python es muy accesible y amigable para principiantes. Una de las cosas que más me gustó fue la posibilidad de ver resultados tangibles rápidamente como la creación de pequeños proyectos visuales como gráficos y visualizaciones de datos. Además, comencé a ver cómo podía aplicar la programación en mi campo de publicidad, como analizar datos de campañas o personalizar estrategias de comunicación. Aprender Python me ha dado una nueva perspectiva y ha ampliado mis habilidades de una manera que nunca imaginé. Ahora me siento más segura y capacitada para enfrentar desafíos tecnológicos en mi carrera
. 
"""

# Mostramos el texto
st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
# La etiqueta <div> se utiliza para agrupar contenido en HTML.
# En este caso, el texto está justificado (text-align: justify;).
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto_2.
# f"": Esta es una cadena de formato en Python.
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena.
# En este caso, {texto_2} se reemplaza por el valor de la variable texto_2.

# Agregamos un subtítulo en la barra lateral
sidebar.markdown("<h1 style='text-align: center;'>Mis primeros gráficos en python</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Los análisis de Ellie</h1>: Esta es una cadena de código HTML.
# La etiqueta <h1> se utiliza para el encabezado principal de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h1> ("Los análisis de Ellie") es el contenido del encabezado.

# Creamos una lista de gráficos
graficos = ['Gráfico de localizacion de peliculas favoritas', 'Histograma de cantidad de goles del Milan', 'Gráfico de goles del Atalanta']

# Creamos un cuadro de selección en la barra lateral
grafico_seleccionado = sidebar.selectbox('Selecciona un gráfico', graficos)
# El cuadro de selección se crea con la función selectbox.
# El primer argumento es el texto que se muestra en el cuadro de selección.
# El segundo argumento es una lista de opciones que se pueden seleccionar.
# En este caso, las opciones son los elementos de la lista graficos.
# La opción seleccionada se asigna a la variable grafico_seleccionado.
# La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
# La función selectbox se utiliza para crear un cuadro de selección en la barra lateral.

# Mostramos el gráfico seleccionado
if grafico_seleccionado == 'Gráfico de localizacion de peliculas favoritas':
    sidebar.markdown("<div style='text-align: justify'>El gráfico es un mapa mundial que muestra los lugares de filmación de algunas películas favoritas. Cada punto azul en el mapa está asociado con una película específica, su director y el año de lanzamiento.Las películas y sus ubicaciones son: Everything Everywhere All at Once dirigida por Daniel Kwan y Daniel Scheinert (2022) en la costa oeste de los Estados Unidos, The Godfather dirigida por Francis Ford Coppola (1972) en la costa este de los Estados Unidos, Inglourious Basterds dirigida por Quentin Tarantino (2009) en Europa, y Parasite dirigida por Bong Joon-ho (2019) en Asia. El mapa usa un color rosa claro para los continentes y está etiquetado con latitud y longitud.</div>", unsafe_allow_html=True)
    sidebar.image("Mapa.png", caption='Gráfico de localizacion de peliculas favoritas', width=500)
    pass
elif grafico_seleccionado == 'Histograma de cantidad de goles del Milan':
    sidebar.markdown("<div style='text-align: justify'>El histograma muestra la distribución de los goles anotados por el Milan en partidos como local. En el eje horizontal se presentan los goles, mientras que en el eje vertical se indica la frecuencia de partidos para cada cantidad de goles. La mayoría de los partidos (alrededor de 9) tuvieron 2 goles anotados, mientras que menos partidos registraron 1, 3, 4 y 6 goles. Solo un partido terminó sin goles. Las barras, de color rosa claro, indican que la concentración más alta de partidos está en los 2 goles, y la distribución de los goles se extiende principalmente de 0 a 6.</div>", unsafe_allow_html=True)
    sidebar.image("Histograma.png", caption='Histograma de cantidad de goles del Milan', width=500)
    pass
elif grafico_seleccionado == 'Gráfico de goles del Atalanta':
    sidebar.markdown("<div style='text-align: justify'>El gráfico es un diagrama de torta que muestra el promedio de goles anotados por el Atalanta como visitante en comparación con otros equipos. La porción rosa del gráfico representa el promedio de los goles del Atalanta como visitante, que constituyen el 42.4%. La porción gris representa el promedio de los goles anotados por este equipo, pero que no fueron mientras jugaban como visitante, los cuales constituyen el 57.6% .</div>", unsafe_allow_html=True)
    sidebar.image("Torta.png", caption='Gráfico de goles del Atalanta', width=500)
    pass

# if grafico_seleccionado == 'Gráfico de Macroareas':: Esta línea verifica si la opción seleccionada es 'Gráfico de Macroareas'.
# Si es así, se ejecuta el código dentro del bloque if.
# En este caso, se muestra un texto y una imagen correspondientes al gráfico de Macroareas.
# El texto y la imagen se muestran en la barra lateral.
# La función markdown se utiliza para mostrar el texto en la barra lateral.
# La función image se utiliza para mostrar la imagen en la barra lateral.
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen.
# El argumento width se utiliza para especificar el ancho de la imagen.
# La palabra clave pass se utiliza para indicar que no se debe hacer nada en caso de que la opción seleccionada no sea 'Gráfico de Macroareas'.
