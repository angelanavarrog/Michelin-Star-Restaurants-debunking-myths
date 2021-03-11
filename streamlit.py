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
# Spanish Michelin awarded restaurant app"""
)

# Dataframe restaurants database
st.write( """
### Restaurants dataframe""")

restaurants = dat.charge_data()
st.dataframe(dat.charge_data())

st.write("""
## ** Hypothesis 1: "Awarded restaurants are equally distributed per Spanish regions.**
""")


# Dataframe that matches regions and number of Michelin Star associated
st.write( """
### How are Michelin Stars distributed per region?""")
graph1 = dat.bar_chart()
st.bar_chart(graph1)


st.write("""***Hypothesis number 1 is not true: the distribution of restaurants per region is not equal.***

The total amount of awarded resturants in Spain is of 220.

At the top end is ***Catalonia, with 54 (around 25% of the restaurants)***. At the other end of the scale is ***Extremadura, with just one*** award-winning restaurant, it represents a ***0.04%***.

Is there any relation with the population of each region?
""")

st.write( """### Restaurants located in Spain map""")
# Incluir mapa con restaurantes representados
st.map(dat.charge_data())


# Region select box
region = st.selectbox(
    "Choose a region",dat.region_list())
st.write("You selected:",region)


# Bar graph that shows the province restaurants distribution 
datapragh = dat.graph2(region)
fig1 = px.bar(datapragh, x = "michelin_stars", y = "region", title = f"Amount of restaurants in {region}",
labels = {"index": "restaurant"},
)
st.plotly_chart(fig1)
# Pie chart to show regional distribution per number of stars
st.write( """
### Restaurant awarded distribution""")
fig2 = px.pie(dat.graph2(region), "michelin_stars")
st.plotly_chart(fig2)


# Dataframe restaurants per province database and graph distribution
st.write( """
### How are Michelin Stars distributed per province?""")
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

st.write( """### Michelin Stars per region and province""")

fig4 = px.sunburst(
    dat.charge_data(),
    path=['region', 'province'],
    values = 'michelin_stars',
)
st.plotly_chart(fig4)