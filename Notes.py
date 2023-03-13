#Carbon A1-A3 and A1-A5 are closely correlated which is to be expected

#I removed any outliers in terms of project value

#I removed any that were not whole Building data, as I wanted like for like

# to include the categorical features in my regression model I will need to use dummy variables
# do the same with Calculated design stage
# do the same with Superstructure Type
# do the same with Foundation Type
# do the same with Ground Floor Type
# do the same for Basement type
# do the same for construction type

#remove Cladding type from the dataframe too many categories may revist this because I know that Cladding does impact Carbon
# remove uk district from the dataframe as it should not be relevant and I don't wan tot create any more features using dummy variables

#project sector has multiple categories and so I did a count on them to find out if I need to make dummy variables of all of them
#print (cd.groupby('Project Sector')['Project Sector'].count())

#Show that Carbon a1-A3 is correlated with a1-a5 so I can choose to review one of them

# Note that all the Carbon grapsh are correlated closely and so this can cause issues in the regression model
#we don't want independant variables that are closely correlated to each other


#descriptive analyisis presecriptive analysis of the eco.zero tool.
#explain how it will be a good prescriptive analaysis of the the tool tiself but not of the real world data
#because of the randomised nature of the controlling parameters, it means there are combinations that would never have been used in the real world
# and the eco.zero tool is there for that exact reason


Situation - General talk about how now we have Data extracted from models we can now start to analyse the data and try to find insights
due to carbon measurements being at the forefront of peoples minds it was decided that I should tart trying to calculate Embodied carbon
from the volumes I have taken out of the models, Aecom have already got a lot of data stored as Part of their Eco.Zero initiative and
we have a spreadsheet with all the Carbon rates for various materials which can be applied to building typologies.

The plan would be to use the data extracted, create Carbon calculations by combining the Carbon factors and Rates from the current Eco.Zero databse
with the volumes and parameters extracted to start storing embodied Carbon data for all Aecom buildings,
Once I have this Data I can then create a linear regression model using the data and
create a tool that can help in predicting what a buildings Embodied carbon might be before we start the design.
I can then use this to measure against current benchmarking criteria to make sure Aecom are adhering to the current standards that it has set itself





roadmap

intro-
Carbon explain carbon impact and the comercial response to iter(explina how predicting is best at the start
explain how you calculate carbon



