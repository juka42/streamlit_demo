import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

def perfis_de_medias_num(var,  df_, num_quebras=4):
    var_cat = pd.qcut(df_[var], num_quebras, duplicates='drop')
    fig, ax = plt.subplots(1, 1)
    ax = sns.pointplot(x = var_cat, y = 'survived', data=df_)
    st.pyplot(fig)

def perfis_de_medias_quali(var_,  df_):
    fig, ax = plt.subplots(1, 1)
    ax = sns.pointplot(x = var_, y = 'survived', data=df_)
    st.pyplot(fig)
