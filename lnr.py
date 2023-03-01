import os
import pandas as pd
import streamlit as st
from tools import graph_maker
from tools import SQLin
from PIL import Image
import numpy as np
import pydeck as pdk


p = 'Excel/PM_Carbon_Database_23-03-01.xlsx'

combined_data = pd.read_excel(p)
cd1 = combined_data.set_index('Project Ref')

def Remove_Outlier_Indices(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    trueList = ~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR)))
    return trueList


testhist =  cd1['GIFA (m2)']

nonOutlierList = Remove_Outlier_Indices(testhist)
cd = cd1[nonOutlierList]

graph88 = graph_maker.plotlyScatter2(cd,'Carbon A1-A3\n(kgCO2e)','Foundation Type')

dummies = pd.get_dummies(cd['Project Sector']).rename(columns=lambda x: 'Project Sector_' + str(x))
df1 = pd.concat([cd, dummies], axis=1)

#stagemean = df1.groupby('Calculation Design\nStage').mean()['Carbon A1-A3\n(kgCO2e)']

#print(cd.groupby('Construction Type')['Construction Type'].count())

#print (df1.columns)