import os
import pandas as pd
import streamlit as st
import lnr
from tools import graph_maker
from tools import SQLin
from PIL import Image
import numpy as np
#import seaborn as sns
#import openpyexcel as op
import matplotlib.pyplot as plt
import pydeck as pdk

def makecsv(pa,t, name):
    return t.to_csv(os.path.join(pa, str(name) + '.csv'))

st.set_page_config (layout="wide")

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
st.title("Gary McCarthy")
st.header("Data Fellowship Portfolio")
# Add image
image1  = Image.open('Images/iStock_000070095321_Small.jpg')
resized_image = image1.resize((1800, 800))
st.image(resized_image)
st.markdown("<h3></h3>", unsafe_allow_html=True)


# Add introduction

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3>Personal Background</h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
#st.markdown("<h4>Introduction to Aecom:</h4>", unsafe_allow_html=True)
imageAecom  = Image.open('Images/4af0731342759efd658682b3b606036d.jpeg')
resized_image = imageAecom.resize((400, 100))
st.image(resized_image)
st.write("AECOM is a multinational engineering and construction firm that provides a wide range of professional services"
         " to clients across the globe. Founded in 1990, the company has grown to become one of the largest and most "
         "diverse firms of its kind, with a portfolio that spans across a variety of industries including transportation,"
         " facilities, environmental, energy, and water. AECOM is known for its commitment to innovation, sustainability,"
         " and providing high-quality services to clients. With a talented and experienced team of professionals, "
         "AECOM has the expertise and resources to tackle even the most complex and challenging projects. Whether "
         "working on large-scale infrastructure projects, building sustainable communities, or developing cutting-edge "
         "technologies, AECOM is dedicated to delivering innovative and impactful solutions that make a positive "
         "difference in the world.")
st.markdown("<h4>Aecom and Data:</h4>", unsafe_allow_html=True)
st.write("As one of the largest engineering and construction firms in the world, AECOM has a wealth of data due to its "
         "size and diverse portfolio of work. Despite this, the construction industry as a whole has struggled to "
         "effectively store and analyze this data to uncover patterns and insights that could lead to increased "
         "productivity. AECOM recognizes the importance of harnessing this data and is well-positioned to "
         "lead the charge. AECOM's commitment to innovation and its expertise in managing large-scale "
         "projects make it a natural fit for taking on this challenge. The company understands that data is a valuable "
         "resource that can drive better decision-making, improve efficiency, and ultimately enhance its services and "
         "offerings to clients. By investing in data management systems and tools, and exploring new and innovative ways "
         "to use data, AECOM is positioning itself at the forefront of a revolution in the construction industry's "
         "approach to data.")

st.markdown("<h4>My Role:</h4>", unsafe_allow_html=True)
st.write("As a BIM Co-ordinator and Computational Designer at Aecom, my primary responsibility is to support the "
         "successful delivery of construction projects through the use of Building Information Modelling (BIM) technology. "
         "This involves creating and managing 3D BIM models that provide a virtual representation of the construction project, "
         "including all relevant information and data. I am also responsible for ensuring the models are up-to-date, accurate, "
         "and accessible to all relevant stakeholders. In addition to my role as a BIM Co-ordinator, I am actively exploring "
         "the ways that data can be utilized within my role. The data that is stored in our BIM models is vast and includes "
         "information such as the dimensions and location of building components, materials specifications, and even "
         "schedules and budgets. As technology evolves and the construction industry shifts towards data-driven processes, "
         "I believe that my skills and experience as a computational designer will play a key role in finding innovative ways "
         "to extract, store, and analyze this data to improve Aecom's workflow efficiency and ability to uncover insights and "
         "predictive patterns.")

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)

st.markdown("<h3>Project 1: Automated Data Extraction and Reporting for Building Information Models</h3>", unsafe_allow_html=True)
st.markdown("<h3>Situation</h3>", unsafe_allow_html=True)
st.write("Currently in Aecom, there is a pressing need to improve the accessibility and utilization of data stored in "
         "Building Information Models (BIM). BIM is a digital representation of the physical and functional "
         "characteristics of a facility, and the data stored in these models is critical to the success of a project. "
         "However, accessing this data can be a challenge, as it is stored on a server and requires the use of specialized "
         "software and technical know-how. In this context, my role as a BIM Coordinator and Computational Designer "
         "is to lead a project that automates the extraction and storage of data from BIM models. This project has been "
         "initiated in response to a business need to unlock valuable insights from the data stored in BIM models and "
         "drive increased productivity and data-driven decision making. The key stakeholders in this project include "
         "BIM Managers, Project Managers, and Engineering Leads. These individuals are responsible for ensuring the "
         "successful delivery of projects and need access to the data stored in BIM models to make informed decisions. "
         "By automating the extraction and storage of this data, I will provide these stakeholders with a centralized "
         "database and a dashboard to visualize and analyze the data, making it easily accessible and usable.")
st.markdown("<h3>Task:</h3>", unsafe_allow_html=True)
st.write("To establish an automated proof of concept tool to extract, store and publish data in the most user friendly "
         "and meaningful way, for this i need to consider the following.")

st.write("As mentioned above Aecom currently faces a challenge in extracting data from their Building Information Models (BIMs). "
         "The traditional method of accessing data, which involves opening each individual model and manually setting "
         "up extraction schedules, is time-consuming and inefficient for the thousands of BIMs in their possession. "
         "This hinders their ability to extract meaningful data from these models, which is crucial for further data "
         "analysis and review.")

st.write("Given the significance of data extraction from BIMs, it is commercially important for Aecom to find a solution. "
         "In order to address this challenge, it is essential that a more technical and efficient method of data extraction "
         "is established. This will serve as the foundation for all future data extraction and analysis efforts, and enable "
         "the business to unlock valuable insights from the models.")

st.write("As part of this task, it will be necessary to engage with various stakeholders to gather the necessary information "
         "and requirements to ensure the successful implementation of the data extraction process. The first step is to meet "
         "with IT to understand the company's data policies and architecture. This will provide insight into the technical "
         "aspects of the project and ensure that the extracted data is stored in compliance with the company's data management "
         "practices.")
st.write("Additionally, it is important to engage with BIM Modelers and Managers to understand their needs and "
         "requirements from the data extraction process. This interaction will provide a better understanding of the desired "
         "end-product and the intended use of the extracted data. With this information, it will be easier to determine the "
         "relevant data points that need to be extracted from the models and how to present the findings in a meaningful and "
         "useful manner.")
st.write("Futhermore, a thorough examination of the relevant laws and regulations must be conducted to ensure compliance in "
         "regards to the data extraction process. This evaluation must consider the General Data Protection Regulation (GDPR), "
         "which sets the standards for protecting personal data and privacy. It is essential to evaluate the potential risk of "
         "extracting sensitive or confidential data and to implement measures to store and manage the data in a secure and "
         "compliant manner, in accordance with the provisions set forth by the GDPR."
         "<br><p3>[K1]</p3>",unsafe_allow_html=True)


st.write("Finally, the research and selection of the appropriate database system to store the extracted data must be undertaken. "
         "This requires considering the scalability of the system as the data extraction initiative grows and the volume of "
         "stored data increases. It may also be beneficial to review the practices of other companies in this area to ensure "
         "that best practices are being followed.")


st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h4>Brief overview of “Building Information modeling”</h4>", unsafe_allow_html=True)

image2  = Image.open('Images/bim-adoption-in-europe-banner.png')
resized_image = image2.resize((1000, 600))
st.image(resized_image)

st.write("A Building Information Model (BIM) is a digital representation of a building or infrastructure project that contains structured, \
multi-disciplinary data throughout the entire life cycle of the building. BIM model is typically created using advanced software, which allows \
for the creation of a 3D model of a building with all the necessary information about the building's design, construction, and operation. \
This information can include architectural, structural, mechanical, electrical, and plumbing systems, as well as information about the materials used in the building.\
 BIM models can be used to extract and analyze data to identify patterns, inefficiencies, and potential issues in the building's design, construction, and operation.")
st.write("In terms of parameter information, BIM models can store a wide range of data points, including:")
st.markdown("<p2>- Spatial information, such as the location and size of different elements in the building.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Geometric information, such as the shape and orientation of different elements.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Material information, such as the type and properties of materials used in the building.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Component information, such as the type and properties of different building components.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Functional information, such as the intended use of different spaces in the building.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Cost information, such as the cost of different materials and components used in the building.</p2>", unsafe_allow_html=True)
st.markdown("<p2>- Maintenance information, such as the schedule and procedures for maintaining different building systems.</p2>", unsafe_allow_html=True)
st.write("This information can be used for cost estimation, schedule management, facility management, energy performance analysis, and many other purposes.")
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.write("Common Data Environment (CDE) is a mutually accessible online space where information in a BIM model is shared among all the stakeholders involved \
in a construction project. It serves as a central repository for all the project data, including design documents, specifications, cost estimates, schedules, \
and other relevant information. The CDE is used to manage, organize and store all the data throughout the project lifecycle, from planning and design to construction \
and operations. It ensures that all the stakeholders have access to the most current and accurate information, improving communication, collaboration and coordination \
among the different teams. The CDE also allows for version control and easy access to previous versions of the information model, making it easier to track changes and \
identify any issues that may arise during the project.")

image3  = Image.open('Images/bim-level-2-spider.jpg')
resized_image = image3.resize((1000, 600))
st.image(resized_image)
st.markdown("<h3></h3>", unsafe_allow_html=True)

st.markdown("<h3>Actions:</h3>", unsafe_allow_html=True)
st.markdown("<h4>Planning:</h4>", unsafe_allow_html=True)



st.write("Extraction:")
image3  = Image.open('Images/blog-etl-data-extraction-strategies-300x180.png')
resized_image = image3.resize((400, 300))
#st.image(resized_image)
st.write("In the planning phase of the project, a meeting was held with potential end users and the current BIM Manager. "
         "During this meeting, the question was posed regarding what information would be the most useful to extract from "
         "the models. The objective was to understand the potential business use cases for the data and identify specific "
         "data points that would be relevant to extract. The discussions during the meeting led to the conclusion that the "
         "following information would be highly valuable to extract: model location parameters, elements properties such as "
         "volumes, counts, and lengths, dimension properties and positional coordinates, and any engineering force parameters "
         "that may have been filled out. These data points were deemed critical in helping stakeholders make informed "
         "decisions and drive productivity.")

st.write("To access and automate the extraction of these data points, it is proposed to utilize the software's API in "
         "conjunction with Python code. This will involve researching the API to gain a deeper understanding of its "
         "capabilities and limitations. The aim is to develop a Python script that can access the API and extract the "
         "identified data points from all the elements in the model. This script will play a crucial role in ensuring the "
         "accuracy and efficiency of the data extraction process."
         "<br><p3>[B5]</p3>",unsafe_allow_html=True)

st.markdown("<h3></h3>", unsafe_allow_html=True)

st.write("Storage:")
image3  = Image.open('Images/datastorage.jpg')
resized_image = image3.resize((400, 300))
#st.image(resized_image)


st.write("I encountered a major roadblock in regards to data storage. After speaking with a representative from the IT department, "
         "it became evident that Aecom lacked a clear system for storing large amounts of data. As a result, I determined "
         "that I would need to implement a temporary solution for the time being by utilizing an SqLite Database File for each Model. "
         "I was made aware that the company was in the process of establishing a permanent infrastructure to handle large "
         "databases. This being the case, I made sure to consider all the best practices for data storage as I continued "
         "with my project, with the eventual goal of migrating my data to the company's permanent storage system."
         "<br><p3>[B2, B6]</p3>",unsafe_allow_html=True)

st.write("One of these best practices mentioned was GDPR, or General Data Protection Regulation."
         "This regulation ensures that data is processed lawfully, fairly, and transparently, and that it is collected for specified, "
         "explicit, and legitimate purposes. Additionally, the data must be adequate, relevant, and limited, accurate, "
         "and kept up to date, and processed in a manner that ensures its security.",unsafe_allow_html=True)

st.write("The data that I would extract from the 3D models could contain personal information, but it was deemed not "
         "relevant to the current project. As a solution, I suggested that I anonymize any fields that contained personal "
         "data. All other information extracted would be internal data created and owned by Aecom.")

st.write("Although I was to proceed creating Sqlite Files it was important to ensure that the files were stored in "
         "a secure and accessible location that was compliant with Aecom's security policies. To achieve this, a "
         "SharePoint site was created as the designated storage location for the files. This would allow for easy access "
         "to the files through SQL calls and ensure that they were protected under Aecom's security policies.")

st.write("It's important to note that once the database is created, it's also essential to establish a maintenance "
         "process to ensure that the data remains accurate and up-to-date. This can include regular checks for data "
         "quality and consistency, as well as backups and updates as necessary. Additionally, as the database grows "
         "and evolves, it may be necessary to optimize it for performance and scalability. Planning for maintenance "
         "and scalability from the beginning can help prevent future issues and ensure the database remains a useful "
         "tool for the organization. <br><p3>[K1, K2, K6]</p3>",unsafe_allow_html=True

)

st.markdown("<h3></h3>", unsafe_allow_html=True)

st.write("Visualisation and Dashboarding:")

st.write("With a plan in place for extracting and storing the data, it was important to understand how the data would be presented "
         "to stakeholders. The focus was to analyze the data in a business context and find the best way to visualize it. "
         "It was crucial to remember that this was a proof-of-concept tool, and its main purpose was to demonstrate that data "
         "could be extracted and published in a manner that would allow for future analytics. The project would focus on descriptive "
         "analytics initially, analyzing what is present within a single model. However, the goal was to start comparing against "
         "other models, leading to the use of predictive and prescriptive analytics. With a large amount of data points being "
         "extracted from the model, it was necessary to have a way of filtering the data based on what the user was looking for. "
         "Therefore, it was decided that the best format to present the data would be on an interactive web page. The web page "
         "would allow the user to upload a model file, have the extraction process happen in the background, and then visualize "
         "the data through various charts and graphs, with the ability to filter the data based on the user's needs. "
         "This required research into web development and familiarizing myself with creating an interactive experience with the data. "
         "It was also noted that Aecom branding and company architecture should be applied to the web page."
         "<br><p3>[S9]</p3>",unsafe_allow_html=True)

st.markdown("<h3></h3>", unsafe_allow_html=True)

st.markdown("<h4>Data Preparation:</h4>", unsafe_allow_html=True)
st.write("The process of accessing the Revit API involved using the Python programming language. Through the use of "
         "Python code, I was able to isolate the relevant data points I needed from the model elements within the Revit model. "
         "The Python code enabled me to extract the data points of interest and send them directly to a SQLite database file using SQL language.")


st.write("Below is a snippet of the type of Data that a Bim model contains and an example of the python code that was used to access the API")

image3 = Image.open('Images/InkedRevit1test.jpg')
resized_image3 = image3.resize((800, 600))
image4 = Image.open('Images/IFCPython.JPG')
resized_image4 = image4.resize((800, 600))

col1, col2 = st.columns(2)

with col1:
    st.image(resized_image3)

with col2:
    st.image(resized_image4)

st.write("Below is an example of the Database file that has been extracted")
image1  = Image.open('Images/SQLDB.JPG')
resized_image = image1.resize((1400, 600))
st.image(resized_image)

st.write("Structured data refers to data that has a defined and predictable format, "
         "Unstructured data, on the other hand, refers to data that has no predefined structure or format.")

st.write("After exporting my first 3D model to a database, it became apparent that while the data was structured within "
         "the context of its own model, the data became unstructured when compared to other models. To combine data from "
         "multiple models under a set schema, I created an Entity Relationship Diagram (ERD) to better understand the "
         "relationship between elements from various models. The ERD allowed me to create a unified schema that could "
         "accommodate data from multiple sources and provide a standard structure for querying and analyzing the data."
         "<br><p3>[K5, K10]</p3>",unsafe_allow_html=True)


image1  = Image.open('Images/ERD2.png')
resized_image = image1.resize((1000, 600))
st.image(resized_image)

st.write("Given that the project was a proof of concept and that there was not yet a standard for storing the data, "
         "I made the decision to not fully normalize the database at this stage. However, the ERD diagram that I created "
         "would serve as a reference for a longer-term solution once one was found.")

st.write("Now that I had a functioning extraction and storage process, it was important to ensure that the data being "
         "extracted was accurate. To do this, I ran spot checks by selecting specific elements in the model and comparing "
         "their parameters to those in the database. I used the element ID as a key identifier to find the same element "
         "in both places, and then checked to make sure the parameters were the same.")

st.write("As an example, I selected an element and checked its Gross Volume and Gross Weight parameters in the model "
         "against the same element in the database. This allowed me to verify that the data was being extracted and "
         "stored accurately.")

st.write("Below is an example of the checking preocedure, on the left is an image of the element selected in the 3d "
         "Model and on the right is the corresponding element row in the database, we can see the values are the same "
         "and so can be confident that the extraction process has worked and that the quality of the data is good")


image5 = Image.open('Images/RevitCheck1.JPG')
resized_image5 = image5.resize((800, 600))
image6 = Image.open('Images/DatebaseCheck1.JPG')
resized_image6 = image6.resize((800, 600))

col1, col2 = st.columns(2)

with col1:
    st.image(resized_image5)

with col2:
    st.image(resized_image6)

st.write("Success !!, I have a working extraction and Storage workflow")

st.markdown("<h4>Data Cleaning:</h4>", unsafe_allow_html=True)

st.write("As seen in the image above, the database has various columns with "
         "null or unnecessary data. Despite the data having structure within the context of the model, a schema is "
         "necessary when exporting the data to ensure that every database file can be imported into a data frame in the "
         "same format with consistent data points. To begin this process, I cleaned up the data by removing any null or "
         "empty columns. Then, I referred to the data points discussed in earlier meetings with the stakeholders and "
         "selected only the columns that were of importance. The resulting cleaned data frame is now ready for analysis."
         " Below is an example of the code used to clean the Data and create a Dataframe")

st.markdown("<h3></h3>", unsafe_allow_html=True)

image1  = Image.open('Images/CleanCode1.JPG')
resized_image = image1.resize((800, 600))
st.image(resized_image)

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

arr = os.listdir('Databases')

#inde = 3
#p = './Databases/'+arr[inde]
p = 'Databases/SGCD-ACM-CP-ZZ-M3-SE-000001_2022_Gary.McCarthy@aecom.com_Gary.McCarthy@aecom.ifc.sqlite'

sqtab = SQLin.importtables((p))
tabs = [pd.DataFrame(item)for item in sqtab]
tabsclean = [cleandataframe(item,1)for item in tabs]
tabnames = []
merged_df1 = pd.concat(tabsclean)
merged_df2 = cleandataframe(merged_df1,60)
merged_df = merged_df2.dropna(axis=0, subset=['I_CATEGORY'])


#print(tabs[0].columns)
#prs = './'
#makecsv(prs,merged_df1,'table')


#check = merged_df
#prs = 'Images'
#makecsv(prs,check,'check')


image1  = Image.open('Images/DataframeEthical.JPG')
resized_image = image1.resize((2000, 600))
st.image(resized_image)

st.write("When it comes to the use and collation of data, ethics must always be considered. The potential impacts on "
         "privacy, confidentiality, and reputation can be significant, and so it is crucial that data is handled with "
         "care and in compliance with relevant laws and regulations.")

st.write("After considering the potential ethical implications of the data, I decided it was necessary to remove the "
         "'Edited By' column from the Dataframe. This was because including the names of individuals or third-party "
         "companies who made changes to the BIM models could lead to the false assumption of correlation and causation. "
         "For example, if the analysis showed that a particular company's work was of lower quality, it could be "
         "mistakenly assumed that the involvement of that company caused the poor quality, rather than simply being "
         "correlated with it. Therefore, to avoid any potential negative impact on the reputations of individuals or "
         "companies, it was best to remove the column entirely from the data."
         "<br><p3>[K15]</p3>",unsafe_allow_html=True)


structCATcount = getcountbycat(merged_df,'I_CATEGORY',1)
#strctFRMdf = getDFbycat(merged_df,'Structural Framing',1)
#test = strctfrm.groupby('I_FAMILY AND TYPE')['I_CUT LENGTH'].agg(['count','sum'])
st.markdown("<h3></h3>", unsafe_allow_html=True)


st.write("Dataframe - 08WQ-ACM-XX-XX-M3-S-En_25_10_65-0001-Model")

image1  = Image.open('Images/DataframeClean.JPG')
resized_image = image1.resize((2000, 600))
st.image(resized_image)

st.markdown("<h4>Data Presentation:</h4>", unsafe_allow_html=True)

st.write("User experience (UX) is a crucial aspect of data analytics that determines how effectively users can interact "
         "with data and gain insights. The principles of UX in data analytics include simplicity, clarity, intuitiveness, "
         "consistency, and responsiveness")

st.write("It was important to consider the domain context of the data being analyzed. "
         "This involved understanding the specific requirements and expectations of the users who would be interacting "
         "with the data. For example, it was important to ensure that the web page displaying the data was easy to navigate "
         "and that the information was presented in a clear and concise manner."
         "<br><p3>[K7, S5]</p3>",unsafe_allow_html=True)

st.write("Having a background in BIM, I was well-equipped to understand the potential use cases and presentation methods "
         "for the harvested data. Although this was initially a proof of concept tool, I recognized that the data could "
         "already provide valuable insights to both Engineers and BIM modelers.")


st.write("For Engineers, the tool could assist in rationalizing the number of structural elements used in a design. "
         "By providing a count of structural elements under various categories, the tool could help identify areas "
         "where Engineers can reduce the amount of element sizes used. Additionally, the tool could also assist in "
         "identifying any outliers in the data, such as the use of an obscure section size or design element.")

st.write("Similarly, BIM modelers could use the tool to understand which parameters are being used in the design process. "
         "To present this information effectively, pie charts and bar graphs would be useful, with the ability to switch "
         "between categories for better data breakdown. Overall, the tool has the potential to provide valuable insights "
         "and improve the design process for both Engineers and BIM modelers."
         "<br><p3>[S5]</p3>",unsafe_allow_html=True)

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.title("Structural Category Metrics")
graph1 = graph_maker.load_pieTEST(structCATcount,'I_CATEGORY','Count')
graph2 = graph_maker.plotlyBar2(structCATcount,'I_CATEGORY','Count')
col1, col2, = st.columns([0.55,0.45])
with col1:
    graph1.update_layout(height=500)
    st.plotly_chart(graph1, use_container_width=True)
with col2:
    graph2.update_layout(height=500)
    st.plotly_chart(graph2, use_container_width=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)

st.write("This first chart provides a great overview of a model in a way that was not possible before this process. "
         "Aecom has never had a way to simply visualize the categories that make up a building. Now, I can drill "
         "down further and analyze a single category in a similar way.")

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)

st.write("As part of my research on web development, I ensured that I could implement interactive pull-down menus. "
         "This allows the user to easily switch between categories and view specific information regarding the breakdown "
         "of elements used in the model. Below shows how the Data can be manipulated interactively to display different "
         "breakdowns for the various category's in the model"
         "<br><p3>[K7]</p3>",unsafe_allow_html=True)

cat1 = st.selectbox('Category1',['Structural Framing','Structural Columns','Floors'])

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)

strctFRM = getDFbycat(merged_df,'Structural Framing',1)
structFRMcount = getcountbycat(strctFRM,'I_TYPE',1)

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.title("Structural Framing Metrics")
graph3 = graph_maker.load_pieTEST(structFRMcount,'I_TYPE','Count')
graph4 = graph_maker.plotlyBar2(structFRMcount,'I_TYPE','Count')
col1, col2, = st.columns([0.5,0.5])
with col1:
    graph3.update_layout(height=500)
    st.plotly_chart(graph3, use_container_width=True)
with col2:
    graph4.update_layout(height=500)
    st.plotly_chart(graph4, use_container_width=True)

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)


cat2 = st.selectbox('Category2',['Structural Columns','Structural Framing','Floors'])

strctCOL = getDFbycat(merged_df,'Structural Columns',1)
structCOLcount = getcountbycat(strctCOL,'I_TYPE',1)

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.title("Structural Column Metrics")
graph5 = graph_maker.load_pieTEST(structCOLcount,'I_TYPE','Count')
graph6 = graph_maker.plotlyBar2(structCOLcount,'I_TYPE','Count')
col1, col2, = st.columns([0.5,0.5])
with col1:
    graph5.update_layout(height=500)
    st.plotly_chart(graph5, use_container_width=True)
with col2:
    graph6.update_layout(height=500)
    st.plotly_chart(graph6, use_container_width=True)

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)

st.write("Pie charts and bar graphs were chosen to present the breakdown of elements in terms of count and percentage "
         "of the overall building. This approach enables the user to easily grasp the general makeup of the model.")

st.write("One of the benefits of using data analytics in the context of building and construction is the ability to "
         "identify areas for optimization and improvement. I Added the scatter plot which can be useful in identifying "
         "elements with very low counts, which can indicate areas where rationalization or optimization may be possible.")

st.write("For example, if an engineer notices that there are several members clustered together with similar sizes, "
         "they may decide to increase the size of one of the members by a small amount in order to reduce the overall "
         "number of unique elements used in the design. This can have benefits in terms of cost savings, ease of construction, "
         "and even overall sustainability of the building.")

st.write("I believe that these charts demonstrate that data analytics tools can provide valuable insights to engineers "
         "and designers, enabling them to make informed decisions about the elements used in their designs and "
         "identifying areas where optimization and improvement are possible. To gather feedback I decided to present "
         "my initial findings to the stakeholders. This feedback will be important in shaping the final product "
         "to meet the needs and expectations of the end-users.")

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)

st.write("I presented my work to the stakeholders in a meeting, explaining the completely automated process and how "
         "someone could simply upload a model to a specific area on the SharePoint system, and the tool would run in the "
         "background to produce the dashboard. The feedback was immediate and positive, with stakeholders noting that "
         "the tool would be useful for future analytical comparisons between models and was already valuable for checking "
         "the general make-up of models. I also demonstrated how the scatter plot could be used for potential optimization "
         "checks, and stakeholders agreed that it was a great high-level check, catching issues that were often not identified "
         "until much later in a project.")
st.write("While discussing how I cleaned the data and removed any null or incomplete data, the BIM manager raised an "
         "interesting point about exploring missing data as it could be a parameter that should have been filled in. "
         "They asked if it was possible to use the tool to run an audit on the model to identify any selected parameters "
         "that were missing and if it was correct. Overall, the meeting was very helpful, and we concluded that the tool, "
         "even as a proof of concept, was helpful and should be rolled out to everyone to better understand their models. "
         "I committed to returning to the data and adding an audit function that would show any parameters missing data "
         "as another chart."
         "<br><p3>[B7]</p3>",unsafe_allow_html=True)


def createpercentchecks(table,listofparams):
    checktable = percent_missing = table.isnull().sum() / len(table) *100
    out = []
    for item in listofparams:
        if item in table.columns:
            out.append(item)
    return checktable[out]

listt = ['T_NRM1_CODE','T_NRM1_DESCRIPTION','T_OMNICLASS NUMBER','T_UNICLASS 2015_CODE','T_UNICLASS2015_DESCRIPTION']

checkdataframesAll = ([createpercentchecks(item,listt)for item in tabsclean])

checkdataframes = []
for item in checkdataframesAll:
    if len(item) > 1:
        checkdataframes.append(pd.DataFrame(item).reset_index().rename(columns={'index': 'Parameter', 0: 'Percentage'}))

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)


st.write("Additional Audit charts at the request of the Bim manager, these Bar charts show the percentage of the parameter"
         " fields that have been filled out. These Parameters are being used in further calculations by other software to "
         "calculate embodied Carbon in the design, if these parameters are missing in the model this could lead to errors "
         "in the calculations and could be very misleading when benchmarking designs against Carbon requirements. As can "
         "be seen in this example there is a lot of missing data, All models will now be run through this auditing tool "
         " as part of our QA procedure and will be written into company standards")

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)

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

st.markdown("<h3>Results & Conclusion:</h3>", unsafe_allow_html=True)

st.write("Key achievements and insights from the project were primarily the development of a proof of concept tool that "
         "demonstrated the potential of the data that can now be extracted as part of an automated process. "
         "The tool enabled Aecom to view the raw data in a simple and clear way, providing a high-level overview "
         "of the design. This helped to identify areas where optimization and rationalization were possible, which were "
         "not part of the original scope of works but were a significant addition to the usefulness of the tool under "
         "the current business contex")

st.write("supporting evidence for the project includes the interactive dashboard generated by the tool, which includes "
         "various charts and graphs demonstrating the key parameters of the BIM model. Additionally, the project "
         "documentation and source code could be used as evidence of the technical process used to develop the tool.")

st.write("The stakeholders were very receptive to the project, as evidenced by the suggestions for further development "
         "and the ideas that were sparked during the presentation. It was clear that the potential of harnessing the "
         "data was well understood and appreciated, and that even the initial simple analytics provided by the tool "
         "had immediate value to the business. The positive feedback indicates that the project was a success and has "
         "the potential to be extended further.")

st.write("In hindsight, if I were to run this project again, I would have sought user feedback earlier in the process. "
         "The presentation sparked enthusiasm among stakeholders, generating a flow of ideas that could have been "
         "valuable to the development process had they been shared earlier. Additionally, I would have considered "
         "cleaning the data at an earlier stage of the project, possibly by creating a more comprehensive parameter "
         "list that could have been extracted earlier. Instead, I extracted all parameters and filtered later, "
         "which slowed down the extraction process due to the vast amount of data stored in the models")

st.write("In conclusion, the project was a resounding success in achieving its primary objective of providing a "
         "proof-of-concept tool for extracting, storing, and publishing data from Building Information Models. "
         "The resulting automated process requires no specialist software or expert knowledge, making it accessible "
         "to a wide range of users. While the tool was intended to facilitate future data analytics using predictive "
         "and prescriptive models, it has already proven useful for visualizing a high-level breakdown of models and "
         "identifying simple insights that may have gone unnoticed otherwise. The overwhelmingly positive feedback "
         "from stakeholders further underscores the usefulness of this approach. As a result, I have been tasked with "
         "extending the use of this data to begin statistically analyzing it for further insights and predictive patterns.")

st.markdown("<h3></h3>", unsafe_allow_html=True)
imageproject1K  = Image.open('Images/KSB Tables/Project1-K_2.png')
resized_image = imageproject1K.resize((2000, 600))
st.image(imageproject1K)

st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3></h3>", unsafe_allow_html=True)
st.markdown("<h3>Project 2: Linear Regression Model for Embodied Carbon</h3>", unsafe_allow_html=True)
st.markdown("<h3>Situation</h3>", unsafe_allow_html=True)


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
st.pydeck_chart(deck)

#st.write(LR.temp)
#LR.graphtemp2.update_layout(height=1800)
#st.plotly_chart(LR.graphtemp2, use_container_width=True)

#st.write(lnr.df1)

