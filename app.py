import streamlit as st
import pandas as pd


url_data = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/tips.csv"
df = pd.read_csv(url_data)

st.header("Dataset de tips")
st.dataframe(df)

st.subheader("Propina promedio por día de la semana")
tip_by = df.groupby("day")["tip"].mean()
st.bar_chart(tip_by)

st.subheader("Histograma de la cuenta")
ax = df["total_bill"].hist()
st.pyplot(ax.figure)


"""Widgets"""
min_tip = st.slider("Seleccione un valor mínimo", min_value=1.0, max_value=10.0, step=0.5)
st.dataframe(df.query("tip>=@min_tip"))

mostrar = st.button("Mostrar histograma")
if mostrar:
    st.subheader("Histograma de la cuenta")
    ax = df["total_bill"].hist()
    st.pyplot(ax.figure)

