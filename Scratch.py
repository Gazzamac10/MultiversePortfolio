
st.markdown("<p2>- Review the API documentation for the BIM software and identify the relevant data points that can "
            "be extracted from the models.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Write a Python script that accesses the API and extracts the identified data points from all the "
            "elements in the model, including a key element ID, element type, and element <p2>geometry.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Set up a database to store the extracted data and design the structure and schema to optimize data "
            "querying and analysis.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Use the Python script to populate the database with the extracted data.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Create interactive visualizations and reports using the data stored in the database. The goal is to "
            "present the data in an easy to understand and meaningful way for <p2>stakeholders to make informed decisions. "
            "This could involve using various software tools to create charts, graphs, or other types of visualizations "
            "that highlight trends or <p2>patterns in the data.</p2>", unsafe_allow_html=True)




st.write("The first step in extracting and storing the relevant data from the BIM model was to identify the stakeholders who would be using the data and gather their \
specific needs and requirements. To do this, a meeting was held with Paul Witham, the BIM manager. During the meeting, Paul emphasized the importance of having the \
information accurate and up-to-date. Based on Paul's input, the available data points in the BIM model were reviewed, and those that were relevant to his needs were selected. \
Industry standards and best practices were consulted to ensure the data points chosen were appropriate.")

image4  = Image.open('Images/Revit1test.JPG')
resized_image = image4.resize((1000, 600))
st.image(resized_image)

st.write("The next step in the project was to determine the appropriate method for storing the data. After careful consideration, \
it was decided that using a SQLite database would be the most efficient option due to the lack of available company infrastructure for other database systems. \
To ensure that the data was stored in the most efficient way possible, an Entity Relationship Diagram (ERD) was created to establish the relationships between \
the different tables in the database. The data within the 3D model was structured, but when compared to data from other models, it was unstructured, \
so the ERD and database schema were designed to effectively store the data and support the queries and operations that would be performed on it.")

image5  = Image.open('Images/ERD2.png')
resized_image = image5.resize((1000, 600))
st.image(resized_image)

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)


st.write("In order to save time, the decision was made not to fully normalize the database at this stage, but to return to the ERD when a long-term strategy \
for data storage had been established. In the meantime, the focus was on keeping the database as simple as possible by extracting each category of element into \
its own table, along with all relevant parameter values.")
st.write("The process of creating a script to batch export models to IFC files using Python was a multi-step process that included:")
st.markdown("<p2>- Importing necessary modules: The first step was to import the necessary modules or libraries in Python that were required for the script, \
including the BIM software's API module, the IFC export <p2>module, and any other necessary libraries for reading and manipulating data.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Connecting to the BIM software: The script established a connection to the BIM software using the API module by providing \
the necessary credentials and connecting to the software's API <p2>endpoint.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Identifying models to be exported: The script identified the models that needed to be exported by searching for models in a specific folder. \
All the models present in that folder were considered for <p2>export.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Extracting data: The script then used a loop to extract the necessary data from the identified models using the API's functions and methods.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Transforming data to IFC format: The data was then transformed to the IFC format using the IFC export module or library.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Error handling: The script included error handling to ensure that any issues that may occur during the process were properly \
handled and reported.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Testing the script: The script was tested with sample data to ensure that it was working as expected and that the exported models \
were in the correct format.o</p2>", unsafe_allow_html=True)
st.write("Overall, the process of creating the script was successfully completed and the script was able to batch export models to IFC files using Python.")
st.markdown("<h3></h3>", unsafe_allow_html=True)
image5  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio_230202\\Images\\code1.jpg')
resized_image = image5.resize((800, 600))
st.image(resized_image)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
image5  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio_230202\\Images\\ifc.jpg')
resized_image = image5.resize((800, 600))
st.image(resized_image)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.write("My next step was to write some code that could extract the relevant data points from the IFC file and store them in the SQLite database.")
image5  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio_230202\\Images\\code2.jpg')
resized_image = image5.resize((800, 600))
st.image(resized_image)
st.write("Figure 6 is an example of code that uses the ifcopenshell library to open and read the IFC file, and the sqlite3 library to connect to \
and interact with the SQLite database. The script starts by connecting to the IFC file and the SQLite database. It then iterates through all the \
elements in the IFC file using the by_type method, which is a built-in method of the ifcopenshell library and extracts the element's name and category. \
For each category of element, the script will create a new table in the SQLite database with columns 'id', 'name', 'category' and any relevant data points, \
the table name will be the category name. After that, it uses the execute method of sqlite3 to insert the element's name and category into the appropriate table \
(related to the category of the element). Finally, it commits the changes made to the SQLite database and closes the connection.")
image5  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio_230202\\Images\\SQLit.jpg')
resized_image = image5.resize((1200, 600))
st.image(resized_image)
st.markdown("<h3></h3>", unsafe_allow_html=True)
image5  = Image.open('C:\\Users\\mccarthyg\\PycharmProjects\\Streamlit-Portfolio_230202\\Images\\Model check.jpg')
resized_image = image5.resize((1200, 600))
st.image(resized_image)
st.write("To spot check the Data I returned to the model and extracted the model element Id number and then searched in the database for the same one.")
st.write("Figure 8 above shows the matched element in the model with the stored database element and a check on Gross_Volume and Gross_weight parameter values to see if they matched up.")
st.write("Success !! I have a working Database file representing a 3d Model.")
st.write("Once I had the data in the SQLite database, I had to extract it in a way that would allow me to present it in a simple and accessible format. \
I decided to use a web page with interactive menus, which would allow users to switch between different parameters and view the charts accordingly.  \
In order to accomplish this, I first had to extract the data from the SQLite database and convert it into a format that could be easily used in the web page. \
This involved writing code to connect to the database, retrieve the relevant data, and convert it into a Pandas DataFrame.")

def cleandataframe(df,thresh):
    dfna = df.fillna(np.NaN).reset_index(drop=True)
    return dfna.dropna(axis=1, thresh=thresh)

def getDFbycat(df1,category,thresh):
    dfna = df1[df1['I_CATEGORY'] == category]
    dfna = dfna.fillna(np.NaN).reset_index(drop=True)
    return dfna.dropna(axis = 1, thresh = thresh)

def getcountbycat(catDF,param,tol):
    dfall = catDF.groupby(param)['I_CATEGORY'].count().reset_index(name='Count')
    return (dfall[dfall['Count']>tol])

arr = os.listdir('./Databases')

inde = 2
p = './Databases/'+arr[inde]

sqtab = SQLin.importtables((p))
tabs = [pd.DataFrame(item)for item in sqtab]
merged_df = pd.concat(tabs)
merged_df = cleandataframe(merged_df,60)


structCATcount = getcountbycat(merged_df,'I_CATEGORY',1)
strctFRMdf = getDFbycat(merged_df,'Structural Framing',1)
#test = strctfrm.groupby('I_FAMILY AND TYPE')['I_CUT LENGTH'].agg(['count','sum'])
st.markdown("<h3></h3>", unsafe_allow_html=True)

st.title("DataFrame Review")
st.write(strctFRMdf)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.write("Once the data was in the pandas DataFrame, I used Matplotlib to create the visuals for the dashboard. "
         "These visuals were then embedded in the web page. This approach allowed for a more dynamic and interactive "
         "experience for the user.")

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.title("Structural Category Metrics")
graph1 = graph_maker.load_pieTEST(structCATcount,'I_CATEGORY','Count')
graph2 = graph_maker.plotlyBar(structCATcount,'I_CATEGORY','Count')
col1, col2, = st.columns([0.55,0.45])
with col1:
    graph1.update_layout(height=500)
    st.plotly_chart(graph1, use_container_width=True)
with col2:
    graph2.update_layout(height=500)
    st.plotly_chart(graph2, use_container_width=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.write("I presented this proof-of-concept to internal stakeholders. "
         "They were impressed with the interactive capabilities and suggested "
         "I include a model health tab that would show some charts with object counts and frequency "
         "of entities from the model. To implement this, I had to extract additional data from the SQLite database "
         "and use it to create the charts for the model health tab. This addition made the dashboard even more useful "
         "for stakeholders as it provided them with more information about the model's health and allowed them to "
         "make more informed decisions. Below are examples of the model health data that was requested")

strctFRM = getDFbycat(merged_df,'Structural Framing',1)
structFRMcount = getcountbycat(strctFRM,'I_TYPE',1)

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.title("Structural Framing Metrics")
graph3 = graph_maker.load_pieTEST(structFRMcount,'I_TYPE','Count')
graph4 = graph_maker.plotlyBar(structFRMcount,'I_TYPE','Count')
col1, col2, = st.columns([0.5,0.5])
with col1:
    graph3.update_layout(height=500)
    st.plotly_chart(graph3, use_container_width=True)
with col2:
    graph4.update_layout(height=500)
    st.plotly_chart(graph4, use_container_width=True)


strctCOL = getDFbycat(merged_df,'Structural Columns',1)
structCOLcount = getcountbycat(strctCOL,'I_TYPE',1)

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.title("Structural Column Metrics")
graph5 = graph_maker.load_pieTEST(structCOLcount,'I_TYPE','Count')
graph6 = graph_maker.plotlyBar(structCOLcount,'I_TYPE','Count')
col1, col2, = st.columns([0.5,0.5])
with col1:
    graph5.update_layout(height=500)
    st.plotly_chart(graph5, use_container_width=True)
with col2:
    graph6.update_layout(height=500)
    st.plotly_chart(graph6, use_container_width=True)

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h4>Conclusion:</h4>", unsafe_allow_html=True)
st.write("In conclusion, the proof-of-concept project was a success. We were able to extract, "
         "store and visualize data from Building Information Models using a code-based approach. "
         "The use of Python and libraries such as Pandas Dataframes and Matplotlib allowed us to easily "
         "extract the data we needed and present it in a way that was most useful for stakeholders.")
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.write("The interactive web page we created was well received by internal stakeholders and provided "
         "them with valuable insights and information about the models. With this proof-of-concept, "
         "we can now move forward and extract data from all models across the company. This data can "
         "be used for analytics and predictive model making, which will lead to improvements in overall "
         "project delivery. It will be important to keep in mind privacy regulations such as GDPR in the "
         "future, but for now, I can focus on the possibilities that this data can bring to the company.")
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.write("Completing this project has helped my professional development and I have established myself within "
         "Aecom as someone who understands the potential of what harnessing this Data could mean to project accuracy "
         "and productivity. This has meant that I have been given the time and backing to pursue the next steps "
         "of Analysing the stored Data.")

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3>Project 2: Machine Learning Carbon Prediction Model</h3>", unsafe_allow_html=True)

st.markdown("<h4>Objective</h4>", unsafe_allow_html=True)
st.write("The next project builds upon the findings and data collected in the previous project by utilizing machine "
         "learning techniques to predict Embodied Carbon in construction projects. By utilizing regression algorithms, "
         "the aim is to accurately predict Embodied Carbon based on the characteristics of the construction project, "
         "as well as any other relevant factors. This prediction will provide valuable insight into the potential environmental "
         "impact of a construction project and will assist in making informed decisions towards a more sustainable construction process.")
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)

collatedata = pd.read_csv('PM_Carbon_Database_11-02-2022test.csv', encoding='ISO-8859-1')
st.write(collatedata)




"""
##"speak about how the daya started of showing what was presetn and that the columns that were missing were removed during cleaning but that on " \
#"reflection it apprerad that data that was missing could actuaally be an error in the modloing process or cuold be a client " \
#"requirement that had been missed, therefore it was requested that specific parameters be checked in the model as an audit " \
#"and those checks to be reported back to the user in a format that means the user could rectify the problem by filling in " \
#"the parameters that had been missed "

#'say that the data that was missing was potentially as important as the data that was present in the context of bussiness use case for the tool'
"""

"""
Descriptive, predictive, and prescriptive analytics are three primary types of data analytics used in various industries.

Descriptive analytics involves analyzing past data to identify patterns and trends, providing insights into what 
happened and why. This type of analysis can help businesses understand their historical performance, identify areas of 
opportunity, and pinpoint potential issues.

Predictive analytics, on the other hand, involves analyzing data to make predictions about the future. This type of 
analysis uses historical data to identify patterns and trends, and then uses that information to predict future outcomes. 
Predictive analytics can help businesses anticipate future trends, make better decisions, and optimize their operations.

Prescriptive analytics takes predictive analytics one step further by providing specific recommendations on what actions 
to take based on the predictions made. This type of analysis uses machine learning algorithms to identify the best course 
of action to take, given the predicted outcomes. Prescriptive analytics can help businesses optimize their operations, 
reduce costs, and improve overall performance.

In data analytics projects, it is important to determine which type of analytics is most appropriate for the specific 
    goals of the project. Descriptive analytics is useful for gaining an understanding of past performance, while 
    predictive and prescriptive analytics can be used to make data-driven decisions for the future.
"""


cat = st.selectbox('Category',sorted((set(structCATcount.I_CATEGORY.tolist()))))

strctFRM = getDFbycat(merged_df,cat,1)
structFRMcount = getcountbycat(strctFRM,'I_TYPE',1)

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)

st.title(cat)
graph3 = graph_maker.load_pieTEST(structFRMcount,'I_TYPE','Count')
graph4 = graph_maker.plotlyBar(structFRMcount,'I_TYPE','Count')

col1, col2, = st.columns([0.5,0.5])
with col1:
    graph3.update_layout(height=500)
    st.plotly_chart(graph3, use_container_width=True)
with col2:
    graph4.update_layout(height=500)
    st.plotly_chart(graph4, use_container_width=True)


strctFRM = getDFbycat(merged_df,cat,1)
structFRMcount = getcountbycat(strctFRM,'I_TYPE',1)
newframe = (structFRMcount.set_index('I_TYPE'))

fig = px.scatter(
    structFRMcount,
    x="Count",
    y='I_TYPE',
    size="Count",
    color='I_TYPE',
    hover_name='I_TYPE',
    log_x=True,
    size_max=55,
    color_discrete_sequence=px.colors.carto.Earth
)
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='grey')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='grey')
st.plotly_chart(fig, use_container_width=True)




col1, col2, = st.columns([0.5,0.5])
graph100 = graph_maker.plotlyBar2(checkdataframes[0],'Parameter','Percentage')
graph200 = graph_maker.plotlyBar2(checkdataframes[1],'Parameter','Percentage')
with col1:
    st.write("Structural Framing")
    graph1.update_layout(height=500)
    st.plotly_chart(graph100, use_container_width=True)
with col2:
    st.write("Structural Columns")
    graph2.update_layout(height=500)
    st.plotly_chart(graph200, use_container_width=True)

col1, col2, = st.columns([0.5,0.5])
graph300 = graph_maker.plotlyBar2(checkdataframes[2],'Parameter','Percentage')
graph400 = graph_maker.plotlyBar2(checkdataframes[3],'Parameter','Percentage')
with col1:
    st.write("Structural Foundations")
    graph1.update_layout(height=500)
    st.plotly_chart(graph300, use_container_width=True)
with col2:
    st.write("Structural Floors")
    graph2.update_layout(height=500)
    st.plotly_chart(graph400, use_container_width=True)



dict = {'lat' : [50.82083333], 'lon' : [0.13750000]}
map = pd.DataFrame.from_dict(dict)

# Define your pydeck chart
layer = pdk.Layer(
    "ScatterplotLayer",
    map,
    get_position=["lon", "lat"],
    get_color=[200, 30, 0, 160],
    get_radius=1200,
    pickable=True
)

view_state = pdk.ViewState(
    longitude= 0.13750000,
    latitude= 50.82083333,
    zoom=6,
    pitch=0,
    bearing=-0,
    height=500,
    width=1000
)

# Combine the layer and viewport into a pydeck.Deck object
deck = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style='mapbox://styles/mapbox/light-v9')

# Display the pydeck chart using st.pydeck_chart()
#st.pydeck_chart(deck)