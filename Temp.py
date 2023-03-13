st.markdown("<h3>Project 2: Linear Regression Model for Embodied Carbon</h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3>Situation</h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)

imageCarbonFactors  = Image.open('Images/Carbon Rates.png')
resized_image = imageCarbonFactors.resize((2000, 600))
st.image(imageCarbonFactors)

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)

lrpath2 = 'Excel/EcoZeroGenerated17.csv'
df1 = pd.read_csv(lrpath2)

dfa = df1[(df1['Total Kg'] > 0) & (df1['A1_A5_kgCO2e_msq'] > 0)]
dfe = dfa.iloc[:,1:].reset_index()
dfr = dfe.drop('index', axis=1).rename_axis('Project No')
dft = dfr.drop(['D'], axis=1)

outliersample1 =  dft['GIA']
nonOutlierList = Statshelpers.Remove_Outlier_Indices(outliersample1)
dfclean1 = dft[nonOutlierList]

outliersample2 =  dfclean1['Cost']
nonOutlierList = Statshelpers.Remove_Outlier_Indices(outliersample2)
dfclean2 = dfclean1[nonOutlierList]

outliersample3 =  dfclean2['Total A1-A5w']
nonOutlierList = Statshelpers.Remove_Outlier_Indices(outliersample3)
dfclean3 = dfclean2[nonOutlierList]

outliersample4 =  dfclean3['A1_A5_kgCO2e_msq']
nonOutlierList = Statshelpers.Remove_Outlier_Indices(outliersample4)
dfclean4 = dfclean3[nonOutlierList]

dfcl = dfclean4

heatall = dft.corr()

heatall1 = graph_maker.plotlyheatmap(heatall)
heatall1.update_layout(height=1600)
st.plotly_chart(heatall1, use_container_width=True)

TypGiaBOX = graph_maker.plotlyBox2(dft,'Typology',"GIA")
TypGiaBOX.update_layout(height=500, width=300)
st.plotly_chart(TypGiaBOX, use_container_width=True)

TypGiaBOX = graph_maker.plotlyBox2(dfclean1,'Typology',"GIA")
TypGiaBOX.update_layout(height=500, width=300)
st.plotly_chart(TypGiaBOX, use_container_width=True)

TypGiaCOST = graph_maker.plotlyBox2(dfclean1,'Typology',"Cost")
TypGiaCOST.update_layout(height=500, width=300)
st.plotly_chart(TypGiaCOST, use_container_width=True)

TypGiaCOST = graph_maker.plotlyBox2(dfclean2,'Typology',"Cost")
TypGiaCOST.update_layout(height=500, width=300)
st.plotly_chart(TypGiaCOST, use_container_width=True)

TypA1_A5 = graph_maker.plotlyBox2(dfclean2,'Typology',"Total A1-A5w")
TypA1_A5.update_layout(height=500, width=300)
st.plotly_chart(TypA1_A5, use_container_width=True)

TypA1_A5 = graph_maker.plotlyBox2(dfclean3,'Typology',"Total A1-A5w")
TypA1_A5.update_layout(height=500, width=300)
st.plotly_chart(TypA1_A5, use_container_width=True)

TypGiaM2_2 = graph_maker.plotlyBox2(dfclean3,'Typology',"A1_A5_kgCO2e_msq")
TypGiaM2_2.update_layout(height=500, width=300)
st.plotly_chart(TypGiaM2_2, use_container_width=True)

TypGiaM2_2 = graph_maker.plotlyBox2(dfclean4,'Typology',"A1_A5_kgCO2e_msq")
TypGiaM2_2.update_layout(height=500, width=300)
st.plotly_chart(TypGiaM2_2, use_container_width=True)

scatterALL = graph_maker.plotlyscattermatrix(dfcl)
scatterALL.update_layout(height=1600)
st.plotly_chart(scatterALL, use_container_width=True)

st.write(dft.corr())

scatterCARB = graph_maker.plotlyscattermatrix(dfcl.iloc[:,:7])
scatterCARB.update_layout(height=1600)
st.plotly_chart(scatterCARB, use_container_width=True)

scatteretotalACvstotalA5 = graph_maker.plotlyScatter2(dfcl,'Total A-C','Total A1-A5w')
scatteretotalACvstotalA5.update_layout(height=600)
st.plotly_chart(scatteretotalACvstotalA5, use_container_width=True)

df2 = dfcl.iloc[:,5:]
df2 = df2.drop(columns=['Total A-C'])

dfdummies = pd.get_dummies(df2, columns=['Typology', 'Building Use','Has Basement'])

#st.write(df2)

df2corr = graph_maker.plotlyheatmap(dfdummies.corr())
df2corr.update_layout(height=1600)
st.plotly_chart(df2corr, use_container_width=True)


scattertotalKGvstotalA1A5 = graph_maker.plotlyScatter2(dfdummies,'Total Kg','Total A1-A5w')
scattertotalKGvstotalA1A5.update_layout(height=600)
st.plotly_chart(scattertotalKGvstotalA1A5, use_container_width=True)


typA1A5average = df2.groupby('Typology').mean()['A1_A5_kgCO2e_msq'].reset_index()

typA1A5average = graph_maker.plotlyBar2(typA1A5average,'Typology','A1_A5_kgCO2e_msq')
typA1A5average.update_layout(height=600)
st.plotly_chart(typA1A5average, use_container_width=True)

Basement = df2.groupby('Has Basement').mean()['Total A1-A5w'].reset_index()

basementvsA1A5 = graph_maker.plotlyBar2(Basement,'Has Basement','Total A1-A5w')
basementvsA1A5.update_layout(height=600)
st.plotly_chart(basementvsA1A5, use_container_width=True)


buildinguse = df2.groupby('Building Use').mean()['A1_A5_kgCO2e_msq'].reset_index()

usevsA5average = graph_maker.plotlyBar2(buildinguse,'Building Use','A1_A5_kgCO2e_msq')
usevsA5average.update_layout(height=600)
st.plotly_chart(usevsA5average, use_container_width=True)


typecount = df2.groupby('A1_A5_kgCO2e_msq').mean()['Total A1-A5w'].reset_index()

graph111 = graph_maker.plotlyScatter2(typecount,'A1_A5_kgCO2e_msq','Total A1-A5w')
graph111.update_layout(height=600)
st.plotly_chart(graph111, use_container_width=True)


dfml1 = dfdummies
dfml1a = dfml1.drop(columns=['Has Basement_No','Grid_X','Grid_Y','Bays_X','Bays_Y'])
dfml2 = dfml1.drop(columns=['Has Basement_No'])

st.write(dfml2)

# target series
y2 = dfml2['A1_A5_kgCO2e_msq']
# predictor matrix

X2 = dfml2[['Storeys','Has Basement_Yes','Building Use_Education',
         'Building Use_Healthcare','Building Use_Office','Building Use_Residential','Grid_X','Grid_Y','Bays_X','Bays_Y',
         'Typology_CLT, Glulam and Steel Column Hybrid','Typology_Composite Cell Beams with Metal Decking',
         'Typology_Composite Rolled Steel with Metal Decking','Typology_Non-Composite Rolled Steel with PCC Planks',
         'Typology_One-Way Spanning RC','Typology_PT RC Flat Slab','Typology_Precast Hollowcore with In-situ RC Beams',
         'Typology_RC Flat Slab','Typology_RC Rib Slab','Typology_Steel Frame with CLT Slabs','Typology_Two-way RC Slab']]


X2a = dfml2[['Storeys','Total Kg','Total A1-A5w']]


#X2 = dfml2[['Storeys','Has Basement_Yes','Building Use_Education',
         #'Building Use_Healthcare','Building Use_Office','Building Use_Residential']]

#'Building Use_Office','Building Use_Residential','Has Basement_Yes']]

X_train, X_test, y_train, y_test = train_test_split(X2,y2,train_size=0.8,random_state=100)

lr3=LinearRegression()
lr3.fit(X2,y2)

trainscore2 = lr3.score(X_train,y_train)
testscore2 = lr3.score(X_test,y_test)

st.write('Training score: ' + str(trainscore2))
st.write('Testing score: ' + str(testscore2))

dif = testscore2-trainscore2
st.write(dif)

lr4=LinearRegression()
lr4.fit(X_train,y_train)

lr5=LinearRegression()
lr5.fit(X2a,y2)

actuals = y2
preds = lr3.predict(X2)
preds2 = lr5.predict(X2a)

dict = {'Actuals' : actuals, 'Predictions' : preds, 'Predictions2' : preds2}
checkdict = pd.DataFrame.from_dict(dict)

st.write(checkdict)

graph111 = graph_maker.plotlyScatter2(checkdict,'Predictions','Actuals')
graph111.update_layout(height=600)
st.plotly_chart(graph111, use_container_width=True)

rmse=np.sqrt(mean_squared_error(preds,actuals))
st.write(rmse)
mae=mean_absolute_error(preds,actuals)
st.write(mae)

st.write(lr4.score(X2,y2))

carbonhistgraph = graph_maker.plotlyHist(dfml2,'A1_A5_kgCO2e_msq',30)
carbonhistgraph.update_layout(height=600)
st.plotly_chart(carbonhistgraph, use_container_width=True)

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)

st.markdown("<h6>ML Embodied Carbon Predictor</h6>", unsafe_allow_html=True)
# Add image
col1, col2, col3 = st.columns([1,8,1])
image1  = Image.open('Images/EcoPredict9.png')
resized_image = image1.resize((1200, 250))
with col2:
    st.image(resized_image)

Usage_Options =['Education','Healthcare','Office','Residential']

typology_Options =['CLT, Glulam and Steel Column Hybrid','Composite Cell Beams with Metal Decking','Composite Rolled Steel with Metal Decking',\
'Non-Composite Rolled Steel with PCC Planks','One-Way Spanning RC','PT RC Flat Slab',\
'Precast Hollowcore with In-situ RC Beams','RC Flat Slab','RC Rib Slab','Steel Frame with CLT Slabs',\
'Two-way RC Slab']

def createindexforTyp(selected):
    l = [0,0,0,0,0,0,0,0,0,0,0]
    index = typology_Options.index(selected)
    return l[:index]+[1]+l[index+1:]

def createindexforUsage(selected):
    l = [0,0,0,0]
    index = Usage_Options.index(selected)
    return l[:index]+[1]+l[index+1:]

def createBoolBasement(Bool):
    if Bool == 'Yes':
        return 1
    else:
        return 0

col1, col2, col3, col4 = st.columns([0.25,0.25,0.25,0.25])
with col1:
    Useage = st.selectbox('Usage_Options', ['Education','Healthcare','Office','Residential'])
with col2:
    Storeys = st.selectbox('Storeys', [i+1 for i in range(35)])
with col3:
    Basement = st.selectbox('Basement', ['Yes','No'])
with col4:
    Typology = st.selectbox('Typology', typology_Options)

col1, col2, col3, col4 = st.columns([0.25,0.25,0.25,0.25])
with col1:
    Grid_X = st.selectbox('Grid_X_Spacing', [i+5 for i in range(7)])
with col2:
    Grid_Y = st.selectbox('Grid_Y_Spacing', [i+6 for i in range(11)])
with col3:
    Bays_X = st.selectbox('Bays_X', [i+1 for i in range(20)])
with col4:
    Bays_Y = st.selectbox('Bays_Y', [i+1 for i in range(20)])


typ = createindexforTyp(Typology)
B_Use = createindexforUsage(Useage)
Boolbase = createBoolBasement(Basement)

params = [Storeys,Boolbase]+B_Use+[Grid_X,Grid_Y,Bays_X,Bays_Y]+typ
paramsALT = [[Storeys,Boolbase]+B_Use+[Grid_X,Grid_Y,Bays_X,Bays_Y]+createindexforTyp(item) for item in typology_Options]

result = "Predicted Carbon Intensity Rate A1_A5_kgCO2e_msq = "+str(lr3.predict([params])[0])
st.markdown("<h3>{}</h3>".format(result), unsafe_allow_html=True)
alternateDF = pd.DataFrame([lr3.predict([item])[0]for item in paramsALT])
alternateDF['Typology'] = typology_Options
#alternateDF.index = typology_Options
alternateDF.columns = ['A1_A5_kgCO2e_msq', *alternateDF.columns[1:]]

alternateoptions = graph_maker.plotlyBar2colours(alternateDF,'Typology','A1_A5_kgCO2e_msq')
alternateoptions.update_layout(height=400)
st.plotly_chart(alternateoptions, use_container_width=True)

def findrating(number):
    if number > 0 and number < 51:
        return "A++"
    elif number > 50 and number < 101:
        return "A+"
    elif number > 100 and number < 151:
        return "A"
    elif number > 150 and number < 201:
        return "B"
    elif number > 200 and number < 251:
        return "C"
    elif number > 250 and number < 301:
        return "D"
    elif number > 300 and number < 351:
        return "E"
    elif number > 350 and number < 401:
        return "F"
    elif number > 400 :
        return "G"


scorsDF = alternateDF
scorsDF.index = alternateDF['Typology']
scorsDF = scorsDF.drop(['Typology'], axis=1)

rate = [findrating(item)for item in alternateDF['A1_A5_kgCO2e_msq']]

scorsDF.insert(1, "Scors Rating", rate)

st.markdown("<h3></h3>", unsafe_allow_html=True)
col1, col2, = st.columns([0.25,0.5])
with col2:
    st.write(scorsDF)
with col1:
    imageCarbonFactors  = Image.open('Images/Scors.JPG')
    resized_image = imageCarbonFactors.resize((400, 425))
    st.image(resized_image)
