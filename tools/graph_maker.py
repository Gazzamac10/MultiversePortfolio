import plotly.express

from tools import ifchelper
from matplotlib import pyplot as plt

style = {
    "figure.figsize": (8, 4),
    "axes.facecolor": (0.0, 0.0, 0.0, 0),
    "axes.edgecolor": "white",
    "axes.labelcolor": "white",
    "figure.facecolor": (1.0, 1.0, 1.0, 0),  # red   with alpha = 30%
    "savefig.facecolor": (0.0, 0.0, 0.0, 0),
    "patch.edgecolor": "#0e1117",
    "text.color": "white",
    "xtick.color": "blue",
    "ytick.color": "blue",
    "grid.color": "blue",
    "font.size": 12,
    "axes.labelsize": 18,
    "xtick.labelsize": 18,
    "ytick.labelsize": 18,
}

def get_elements_graph(file):
    types = ifchelper.get_types(file, "IfcBuildingElement")
    types_count = ifchelper.get_type_occurence(file, types)
    x_values, y_values = ifchelper.get_x_and_y(types_count)

    plt.rcParams.update(style)
    fig, ax = plt.subplots()
    ax.bar(x_values, y_values, width=0.5, align="center", color="blue", alpha=0.5)
    ax.set_title("Building Objects Count")
    ax.tick_params(color="blue", rotation=90, labelsize="7", labelcolor="blue")
    ax.tick_params(axis="x", rotation=90)
    ax.set_xlabel("Element Class")
    ax.set_ylabel("Count")
    ax.xaxis.label.set_color("blue")
    ax.yaxis.label.set_color("blue")

    ax.set_box_aspect(aspect=1 / 2)
    ax.axis()
    # ax.xticks(y_pos, objects, rotation=90, size=10)
    return ax.figure

def get_elements_graph2(df,x,y):
    #types = ifchelper.get_types(file, "IfcBuildingElement")
    #types_count = ifchelper.get_type_occurence(file, types)
    x_values, y_values = df[x],df[y]

    plt.rcParams.update(style)
    fig, ax = plt.subplots()
    ax.bar(x_values, y_values, width=1, align="center", color="red", alpha=0.5)
    #ax.set_title("Building Objects Count")
    ax.tick_params(color="white", rotation=90, labelsize="7", labelcolor="blue")
    ax.tick_params(axis="x", rotation=90)
    ax.set_xlabel("Family Type")
    ax.set_ylabel("Count")
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")

    ax.set_box_aspect(aspect=0.5)
    ax.axis()
    # ax.xticks(y_pos, objects, rotation=90, size=10)
    return ax.figure


def get_high_frequency_entities_graph(file):
    types = ifchelper.get_types(file)
    types_count = ifchelper.get_type_occurence(file, types)
    x_values, y_values = ifchelper.get_x_and_y(types_count, 400)

    plt.rcParams.update(style)
    fig, ax = plt.subplots()
    ax.bar(x_values, y_values, width=0.5, align="center", color="blue", alpha=0.5)

    ax.set_title("IFC entity types frequency")

    ax.tick_params(color="blue", rotation=90, labelsize="7", labelcolor="blue")
    ax.tick_params(axis="x", rotation=90)
    ax.set_xlabel("File Entities")
    ax.set_ylabel("No of occurences")
    ax.xaxis.label.set_color("blue")
    ax.yaxis.label.set_color("blue")

    ax.set_box_aspect(aspect=1 / 2)
    ax.axis()
    # ax.xticks(y_pos, objects, rotation=90, size=10)
    return ax.figure

def get_high_frequency_entities_graph2(file,x,y):
    x_values, y_values = file[x],file[y]

    plt.rcParams.update(style)
    fig, ax = plt.subplots()
    ax.bar(x_values, y_values, width=1, align="center", color="Red", alpha=0.5)

    #ax.set_title("IFC")

    ax.tick_params(color="blue", rotation=90, labelsize="16", labelcolor="blue")
    ax.tick_params(axis="x", rotation=90)
    for i, v in enumerate(y_values):
        ax.text(i, v + 0.1, str(v), color='blue', ha='center', fontsize=12)
    ax.set_xlabel("Family Types")
    ax.set_ylabel("No of occurences")
    ax.xaxis.label.set_color("White")
    ax.yaxis.label.set_color("White")

    ax.set_box_aspect(aspect= 0.5)
    ax.axis()
    # ax.xticks(y_pos, objects, rotation=90, size=10)
    return ax.figure


def load_pie(dataframe,n,v,title,colors):
    import plotly.express as px
    fig = px.pie(dataframe,names=n,values=v,
    color_discrete_sequence=colors,
    title=title)
    #fig.update_layout(showlegend=False)
    fig.update_traces(textinfo='none')
    return fig

def load_pie2(dataframe, n, v, title, colors, traceorder):
    import plotly.express as px
    fig = px.pie(dataframe, names=n, values=v,
                 color_discrete_sequence=colors,
                 title=title,
                 color_discrete_map=traceorder)
    fig.update_traces(textinfo='none')
    return fig


def load_pieTEST(dataframe,n,v):
    import plotly.express as px
    fig = px.pie(dataframe,
        names=n, values=v, color=dataframe[n],
            color_discrete_sequence=px.colors.carto.Earth)
    return fig


def load_graph2(dataframe):
    import plotly.express as px
    fig = px.scatter(
        dataframe,
        x="GDP",
        y="Life expectancy",
        size="Population",
        color="continent",
        hover_name="Country",
        log_x=True,
        size_max=60,
    )
    return fig

def plotlyBar(dataframe,x):
    import plotly.express as px
    fig = px.bar(dataframe, x=dataframe[x],
        color=dataframe[x],color_discrete_sequence=px.colors.carto.Antique)
    fig.update_xaxes(showticklabels=True)  # Hide x axis ticks
    fig.update_yaxes(showticklabels=True)
    return fig

def plotlyBar2(dataframe,x,y):
    import plotly.express as px
    fig = px.bar(dataframe, x=dataframe[x], y=dataframe[y],
        color=dataframe[x],color_discrete_sequence=px.colors.carto.Antique)
    fig.update_xaxes(showticklabels=True,)  # Hide x axis ticks
    fig.update_yaxes(showticklabels=True)
    #fig.update_layout(yaxis_range=[0,100])
    return fig

def plotlyBar2colours(dataframe,x,y):
    import plotly.express as px
    fig = px.bar(dataframe, x=dataframe[x], y=dataframe[y],
        color=dataframe[x],color_discrete_sequence=px.colors.carto.Brwnyl)
    fig.update_xaxes(showticklabels=True,)  # Hide x axis ticks
    fig.update_yaxes(showticklabels=True)
    #fig.update_layout(yaxis_range=[0,100])
    return fig


def plotlyBarSCORS(dataframe,x,y):
    import plotly.express as px
    fig = px.bar(dataframe, x=dataframe[x], y=dataframe[y],
        color=dataframe[x],color_discrete_sequence=px.colors.carto.Bold)
    fig.update_xaxes(showticklabels=True,)  # Hide x axis ticks
    fig.update_yaxes(showticklabels=True)
    #fig.update_layout(yaxis_range=[0,100])
    return fig


def plotlyBox(dataframe,x):
    import plotly.express as px
    fig = px.box(dataframe, y=dataframe[x],
        color_discrete_sequence=px.colors.carto.Earth)
    fig.update_xaxes(showticklabels=False)  # Hide x axis ticks
    fig.update_yaxes(showticklabels=False)
    return fig

def plotlyBox2(dataframe,x,y):
    import plotly.express as px
    fig = px.box(dataframe, x=dataframe[x],y=dataframe[y],
        color_discrete_sequence=px.colors.carto.Aggrnyl)
    fig.update_xaxes(showticklabels=False)  # Hide x axis ticks
    fig.update_yaxes(showticklabels=False)
    return fig


def plotlyHist(dataframe,x,bins):
    import plotly.express as px
    fig = px.histogram(dataframe, x=dataframe[x], nbins = bins,
                       color_discrete_sequence=px.colors.carto.Antique)
    fig.update_xaxes(showticklabels=True)  # Hide x axis ticks
    fig.update_yaxes(showticklabels=True)
    return fig

def plotlyHist2(dataframe,x,y):
    import plotly.express as px
    fig = px.histogram(dataframe, x=dataframe[x], y=dataframe[y],
        color=dataframe[x],color_discrete_sequence=px.colors.carto.Earth)
    fig.update_xaxes(showticklabels=False)  # Hide x axis ticks
    fig.update_yaxes(showticklabels=False)
    return fig

def plotlyScatter(dataframe,x):
    import plotly.express as px
    fig = px.scatter(dataframe, x=dataframe[x],
        color=dataframe[x],color_discrete_sequence=px.colors.carto.Earth)
    fig.update_xaxes(showticklabels=False)  # Hide x axis ticks
    fig.update_yaxes(showticklabels=False)
    return fig
"""
def plotlyScatter2(dataframe,x,y):
    import plotly.express as px
    fig = px.scatter(dataframe, x=dataframe[x], y=dataframe[y],
        color=dataframe[x],color_discrete_sequence=px.colors.carto.Antique)
    fig.update_xaxes(showticklabels=True,)  # Hide x axis ticks
    fig.update_yaxes(showticklabels=True)
    fig.update_layout(yaxis_range=[0,100])
    return fig
"""

def plotlyScatter2(dataframe,x,y):
    import plotly.express as px
    fig = px.scatter(dataframe, x=dataframe[x], y=dataframe[y],
        color=dataframe[x],color_discrete_sequence=px.colors.carto.Antique)
    fig.update_xaxes(showticklabels=True,)  # Hide x axis ticks
    fig.update_yaxes(showticklabels=True, autorange=True)
    return fig

def plotlyscattermatrix(dataframe):
    import plotly.express as px
    fig = px.scatter_matrix(dataframe)
    return fig

def plotlyheatmap(dataframe):
    import plotly.express as px
    fig = px.imshow(dataframe)
    return fig
