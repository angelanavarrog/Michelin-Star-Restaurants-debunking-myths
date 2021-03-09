import streamlit as st
import src.manage_data as dat
import plotly.express as px
from PIL import Image

imagen = Image.open("images/image1.jpg")

st.image(imagen)
st.write( """
# Api created to visualize Michelin Restaurant database"""
)

st.write( """
### Restaurants dataframe""")

restaurants = dat.charge_data()
st.dataframe(dat.charge_data())

st.write( """
### How are Michelin Stars distributed per region""")
graph1 = dat.bar_chart()
st.dataframe(graph1)

region = st.selectbox(
    "Choose a region",dat.region_list())

st.bar_chart(graph1)

st.write( """
### How are Michelin Stars distributed per province?""")
graph2 = dat.bar_chart_st()
st.dataframe(graph2)

st.bar_chart(graph2)

province = st.selectbox(
    "Choose a province",dat.province_list())
st.write("You selected this option ",province)

datapragh = dat.graph(province)
fig = px.line(datapragh, y = "michelin_stars", title = f"Amount of restaurants in {province}",
labels = {"index": "province"}
)
st.plotly_chart(fig)


st.write( """
### Province: populationd and employment and unemployment rates""")
province_data = dat.charge_data2()
st.dataframe(dat.charge_data2())


