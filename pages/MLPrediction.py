import os
import pandas as pd
import streamlit as st

#import Controller as ct
import Controller
from tools import graph_maker
from tools import SQLin
from tools import Statshelpers
from PIL import Image
import numpy as np
#import seaborn as sns
#import openpyexcel as op
import matplotlib.pyplot as plt
import pydeck as pdk
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def makecsv(t, name):
    path = 'Excel'
    return t.to_csv(os.path.join(path, str(name) + '.csv'))

#st.set_page_config(page_title="My Streamlit App", page_icon=":rocket:", layout="wide", initial_sidebar_state="expanded")

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
#image1  = Image.open('Images/ML1.jpg')
#resized_image = image1.resize((1800, 800))
#st.image(image1)
st.markdown("<h3></h3>", unsafe_allow_html=True)

#fp = os.path.abspath("Excel/dfdummies.csv")
#pdd = pd.read_csv(fp)

df = Controller.dfdummies
df = df.iloc[:,5:]
df = df.drop(columns=['Has Basement_No','Has Transfer Deck_No'])

# target series
y = df['Total A1-A5w']

# predictor matrix
X = df[['Total Kg']]

lr=LinearRegression()
lr.fit(X,y)

st.write('Predicted Total A1-A5w: '+str(lr.predict([[713042111.249708]])))

# target series
y2 = df['A1_A5_kgCO2e_msq']

# predictor matrix
#X2 = df[['GIA']]
X2 = df[['GIA','Storeys','Has Basement_Yes','Has Transfer Deck_Yes','Grid_X','Grid_Y','Building Use_Education',
         'Building Use_Healthcare','Building Use_Office','Building Use_Residential',
         'Typology_CLT, Glulam and Steel Column Hybrid','Typology_Composite Cell Beams with Metal Decking',
         'Typology_Composite Rolled Steel with Metal Decking','Typology_Non-Composite Rolled Steel with PCC Planks',
         'Typology_One-Way Spanning RC','Typology_PT RC Flat Slab','Typology_Precast Hollowcore with In-situ RC Beams',
         'Typology_RC Flat Slab','Typology_RC Rib Slab','Typology_Steel Frame with CLT Slabs','Typology_Two-way RC Slab']]


#X2 = df[['GIA','Storeys','Has Basement_Yes','Has Transfer Deck_Yes']]

#X2 = df.drop(columns=['A1_A5_kgCO2e_msq','Grid_Y','Total A1-A5w','Grid_X','A5atCO2'])

st.write(df)

#makecsv(X2,'X2')

#lr2=LinearRegression()
#lr2.fit(X2,y2)

X_train, X_test, y_train, y_test = train_test_split(X2,y2,train_size=0.8,random_state=100)

lr3=LinearRegression()
lr3.fit(X_train,y_train)

trainscore2 = lr3.score(X_train,y_train)
testscore2 = lr3.score(X_test,y_test)

st.write('Training score: ' + str(trainscore2))
st.write('Testing score: ' + str(testscore2))

lr4=LinearRegression()
lr4.fit(X_train,y_train)


#preds = lr4.predict([[25088,2,0,0,12,12,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0]])
#preds = lr4.predict([[278460,13,0,0]])

#st.write(preds)


dif = testscore2-trainscore2
st.write(dif)

scatterCARB = graph_maker.plotlyscattermatrix(X2.iloc[:,:4])
scatterCARB.update_layout(height=1600)
st.plotly_chart(scatterCARB, use_container_width=True)

actuals = y2
predteest = lr4.predict(X2)

dict = {'Actuals' : actuals, 'Predictions' : predteest}
checkdict = pd.DataFrame.from_dict(dict)

st.write(checkdict)
st.write(actuals.max())

graph111 = graph_maker.plotlyScatter2(checkdict,'Actuals','Predictions')
graph111.update_layout(height=600)
st.plotly_chart(graph111, use_container_width=True)