import streamlit as st
import Src.manage_data as dat
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
### How are Michelin Stars distributed per province?""")
graph1 = dat.bar_chart_st()
st.dataframe(graph1)

st.bar_chart(graph1)

province = st.selectbox(
    "Choose a province",dat.province_list())

st.write( """
### Province: populationd and employment and unemployment rates""")
province_data = dat.charge_data2()
st.dataframe(dat.charge_data2())


