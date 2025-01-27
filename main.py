import streamlit as st
import pandas as pd


titanic = pd.read_csv("titanic.csv")

st.title("Titanic, Supervivientes:")

"""
 Objetivo: Usando https://docs.streamlit.io/develop/api-reference crear 3 elementos para mostrar datos de Titanic.
 Los datos están en Pandas ->  
    Ejemplos - ayuda: 
        https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html
        https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html

"""
# Alex Añade 👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻
# Mostrar tabla inicial con "Age" y "Sex"
st.subheader("Datos de Edad y Género")
st.table(titanic[["Age", "Sex"]].head(10))  # Muestra las primeras 10 filas como ejemplo

# 1️⃣ Filtro interactivo por clase de pasajero
st.subheader("🎫 Filtro por Clase de Pasajero")
clases = titanic["Pclass"].unique()
clase_seleccionada = st.selectbox("Selecciona una clase:", clases)

# Filtrar datos según la clase seleccionada
titanic_clase = titanic[titanic["Pclass"] == clase_seleccionada]
st.write(f"Pasajeros en Clase {clase_seleccionada}: {len(titanic_clase)}")
st.dataframe(titanic_clase[["Name", "Pclass", "Age", "Sex", "Survived"]])

# 2️⃣ Estadísticas básicas: Edad de los pasajeros
st.subheader("📊 Estadísticas Básicas de Edad")
st.write("Calcula estadísticas descriptivas de la edad de los pasajeros:")
st.write(titanic["Age"].describe())

# 3️⃣ Gráfico: Supervivencia por género
st.subheader("🧑‍🤝‍🧑 Supervivencia por Género")
supervivencia_genero = titanic.groupby("Sex")["Survived"].mean()
st.bar_chart(supervivencia_genero)
