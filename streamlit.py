# Streamlit app file 
# It is mandatory to enter into the terminal: "$streamlit run streamlit.py" . A window in Chrome.
# A new conda enviroment to make it run, with Python 3.7.10 .

import streamlit as st
import src.manage_data as dat
import plotly.express as px
from PIL import Image
import folium
from streamlit_folium import folium_static


imagen = Image.open("images/image1.jpg")

# Portada y título

st.image(imagen)
st.write( """
# Spanish Michelin awarded restaurant app 
## Created to easily find awarded restaurants based on location and prices."""
)

# Dataframe restaurants database
st.write( """
### Restaurants dataframe""")

restaurants = dat.charge_data()
st.dataframe(dat.charge_data())

st.write("""
## ** Awarded restaurants distribution per Spanish regions.**
""")



# Dataframe that matches regions and number of Michelin Star associated

graph1 = dat.bar_chart()
st.bar_chart(graph1)

st.write( """### Restaurants located in Spain map""")
# Incluir mapa con restaurantes representados
st.map(dat.charge_data())

st.write( """
### Stars distribution""")

fig = px.sunburst(
    dat.charge_data(),
    path=['region'],
    values = 'michelin_stars',
)
st.plotly_chart(fig)


st.write( """### Michelin Stars per region and province""")

fig4 = px.sunburst(
    dat.charge_data(),
    path=['region', 'province'],
    values = 'michelin_stars',
)
st.plotly_chart(fig4)


st.write( """
## How are Michelin Stars distributed in a selected region?""")

# Region select box
region = st.selectbox(
    "Choose a region",dat.region_list())
st.write("You selected:",region)


# Bar graph that shows the province restaurants distribution 
datapragh = dat.graph2(region)
fig1 = px.bar(datapragh,y = "michelin_stars", title = f"Amount of restaurants in {region}",
labels = {"index": "restaurant"},
)
st.plotly_chart(fig1)


# Pie chart to show regional distribution per number of stars
st.write( """
### Restaurant awarded distribution""")
fig2 = px.pie(dat.graph2(region), "michelin_stars")
st.plotly_chart(fig2)

# Box to show regional average price distribution 

st.write( """
### Regional average price""")
fig8 = px.box(dat.graph2(region), "price_average")
st.plotly_chart(fig8)

# Dataframe restaurants per province database and graph distribution
st.write( """
## How are Michelin Stars distributed per province?""")
graph2 = dat.bar_chart_st()
st.dataframe(graph2)

st.bar_chart(graph2)

# Province select box
province = st.selectbox(
    "Choose a province",dat.province_list())
st.write("You selected:",province)

# Bar graph that shows the province restaurants distribution 
datapragh = dat.graph(province)
fig3 = px.bar(datapragh, y = "michelin_stars", title = f"Amount of restaurants in {province}",
labels = {"index": "restaurant"}
)
st.plotly_chart(fig3)



# Box to show regional average price distribution 

st.write( """
### Province average price""")
fig8 = px.box(dat.graph(province), "price_average")
st.plotly_chart(fig8)