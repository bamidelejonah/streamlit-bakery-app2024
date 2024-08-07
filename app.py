import streamlit as st
import numpy as np
import pandas as pd


def load_data():
    file = 'bakerysales.csv'
    df = pd.read_csv(file)
    return df.head(100)

# load the dataset
df = load_data()

# display the table
st.dataframe(df)
