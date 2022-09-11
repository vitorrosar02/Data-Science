import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Carrega o modelo e o DataFrame
df = pd.read_csv("Diamonds Prices2022.csv")
pipe = pickle.load(open("MP.pkl", "rb"))


st.title("Prevendo Preço de Diamantes")

# As características do diamante
Quilate = st.selectbox('Quilate', df['carat'].unique())
Corte = st.selectbox('Corte', df['cut'].unique())
Cor = st.selectbox('Cor', df['color'].unique())
Brilho = st.selectbox('Brilho', df['clarity'].unique())
Profundidade = st.selectbox('Profundidade', df['depth'].unique())
Cabeca = st.number_input('Espessura Da Parte Superior')
x = st.number_input('Largura(0-5)')
y = st.number_input('Comprimento(0-5)')
z = st.number_input('Altura(0-10)')

if st.button('Predict Price'):

    query = np.array([Quilate, Corte, Cor, Brilho,
                     Profundidade, Cabeca, x, y, z])

    query = query.reshape(1, 9)

    prediction = str(int(np.exp(pipe.predict(query))))

    st.title("O valor do diamante é US$" + prediction)
