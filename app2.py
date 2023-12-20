import pandas as pd
import plotly.express as px
import streamlit as st

# lendo arquivo 
car_data = pd.read_csv('vehicles.csv')

# Cabeçalho
st.header('Análise de Dados de Veículos')

# Caixa de seleção para escolher o tipo de gráfico
option = st.selectbox('Selecione o tipo de gráfico:', ('Histograma', 'Gráfico de Dispersão'))
# Verificar a escolha do usuário e criar o gráfico correspondente
if option == 'Histograma':
    # Histograma mais elaborado com cores
    hist = px.histogram(car_data, x='odometer', color='year', title='Histograma de Odômetro com Cores',
                        labels={'odometer': 'Odômetro'})
    # Exibir o histograma Plotly interativo
    st.plotly_chart(hist, use_container_width=True)
else:
    # Gráfico de dispersão com legenda e cores
    scatter = px.scatter(car_data, x='mileage', y='price', color='year', title='Gráfico de Dispersão: Preço x Quilometragem',
                         labels={'mileage': 'Quilometragem', 'price': 'Preço'})
    # Exibir o gráfico de dispersão Plotly interativo
    st.plotly_chart(scatter, use_container_width=True)