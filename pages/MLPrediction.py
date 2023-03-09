import os
import pandas as pd
import streamlit as st
from tools import graph_maker
from tools import SQLin
from tools import Statshelpers
from PIL import Image
import numpy as np
#import seaborn as sns
#import openpyexcel as op
import matplotlib.pyplot as plt
import pydeck as pdk

st.set_page_config(
        page_title="MLPredictor",
        layout="wide",
        initial_sidebar_state="expanded",
)

# Add custom CSS styles
st.markdown(
    """
    <style>
        h1 {
            color: Black;
            font-family: Arial, sans-serif;
            font-size: 36px;
            text-align: center;
        }
        h2 {
            color: Black;
            font-family: Arial, sans-serif;
            font-size: 65px;
            text-align: center;
        }
        h3 {
            font-weight: bold;
            color: #104E8B;
            font-family: Arial, sans-serif;
            font-size: 24px;
            text-align: left;
        }
        h4 {
            font-weight: bold;
            color: Black;
            font-family: Arial, sans-serif;
            font-size: 20px;
            text-align: left;
        }
        h5 {
            font-weight: bold;
            color: Black;
            font-family: Arial, sans-serif;
            font-size: 16px;
            text-align: right;
        }
        p {
            color: Black;
            font-family: Arial, sans-serif;
            font-size: 18px;
            text-align: left;
            #margin-bottom: 24px;
        }
        p2 {
            color: Black;
            font-family: Arial, sans-serif;
            font-size: 18px;
            text-align: left;
            padding-left: 25px
        }
        p3 {
            color: Red;
            font-family: Arial, sans-serif;
            font-size: 18px;
            text-align: left;
            #margin-bottom: 24px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add title
st.header("ML Predictor")
# Add image
image1  = Image.open('Images/ML1.jpg')
resized_image = image1.resize((1800, 800))
st.image(image1)
st.markdown("<h3></h3>", unsafe_allow_html=True)


df = pd.read_csv('Excel/dfdummies.csv')

st.write(df)