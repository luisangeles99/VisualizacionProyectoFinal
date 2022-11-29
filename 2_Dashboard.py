import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.info('Menú de navegación')

a, b = st.columns([2, 10])

with a:
    st.text("")
    st.image("logo.jpeg")
with b:
    st.title("Dashboard dinámico")


