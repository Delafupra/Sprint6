import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title('Cuadro de Mandos de Análisis de Vehículos')

# Encabezado de la aplicación
st.header('Análisis Exploratorio de Datos de Vehículos')

# Cargar el conjunto de datos
df = pd.read_csv('vehicles_us.csv')

# Mostrar las primeras filas del conjunto de datos para verificación
st.write(df.head())

# Crear un botón para construir un histograma
hist_button = st.button('Construir histograma')

if hist_button:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig = px.histogram(df, x='odometer', title='Distribución del Odómetro')

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión
    fig = px.scatter(df, x='odometer', y='price', title='Precio vs. Millas Recorridas')

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# (Opcional) Usar casillas de verificación en lugar de botones
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(df, x='odometer', title='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Construir un gráfico de dispersión para las columnas odómetro y precio')
    fig = px.scatter(df, x='odometer', y='price', title='Precio vs. Millas Recorridas')
    st.plotly_chart(fig, use_container_width=True)