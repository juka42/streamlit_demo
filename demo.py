import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from helper1_graficos import perfis_de_medias_num, perfis_de_medias_quali

st.title("demonstração do streamlit")
st.sidebar.image("./fgv_logo_menor.png", use_column_width=False)


df_csv = st.sidebar.file_uploader('Arquivo de dados',
                                  type=['csv','zip'],
                                  accept_multiple_files=False,
                                  key="fileUploader")

if df_csv is not None:
    df = pd.read_csv(df_csv)

    variaveis = df.columns

    var = st.sidebar.selectbox('Seleciona a variavel',variaveis)

    # st.info(var_type in ['int64', 'float64', 'int'])

    st.header('Primeiras linhas da base')
    st.dataframe(df.head())

    st.header('Perfil de uma variável')

# def perfis_de_medias(var):
#     var_cat = var + '_cat'
#     df[var_cat] = pd.qcut(df['age'], 4, duplicates='drop')
#
#     fig, ax = plt.subplots(1, 1)
#
#     ax = sns.pointplot(x = var_cat, y = 'survived', data=df)
#
#     st.pyplot(fig)
    var_type = df[var].dtypes


    if var_type in ['int64', 'float64', 'int']:
        n_quebras = st.sidebar.number_input('Numero de quebras:', value=4)
        perfis_de_medias_num(var, df, n_quebras)
    else:
        perfis_de_medias_quali(var, df)
