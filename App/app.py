# Libraries
import streamlit as st
import pickle as pkl
import joblib as jbl
import matplotlib.pyplot as plt

# Page Configuration

st.set_page_config(
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.title("NN-Predict")