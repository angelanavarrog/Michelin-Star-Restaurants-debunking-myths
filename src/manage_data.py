# In this file has been defined functions to create an streamlit app.


import pandas as pd

def charge_data():
    #Function to obtain restaurants database info
    restaurants = pd.read_csv('output/restaurants.csv')
    return restaurants

def charge_data2():
    #Function to obtain province database info
    province_data = pd.read_csv('output/province_data.csv')
    return province_data

def rename_id(x):
    x = f"Province {x}"
    return x

"""def rename_r(x):
    x = f"Region {x}"
    return x"""

def bar_chart():
    #Function to represent regional Michelin Star information
    data = charge_data()
    data = data.groupby("region").agg({"michelin_stars":'count'}).rename(columns = {"region":"region","region":"Total Michelin Stars"}).reset_index().set_index("region",drop = True)
    return data

def bar_chart_st():
    #Function to represent proovince Michelin Star information
    data = charge_data()
    data = data.groupby("province").agg({"michelin_stars":'count'}).rename(columns = {"province":"province","province":"Total Michelin Stars"}).reset_index().set_index("province",drop = True)
    return data

def province_list():
    #Function to obtain unique province
    data = charge_data()
    return list(data.province.unique())

def region_list():
    #Function to obtain unique region names
    data = charge_data()
    return list(data.region.unique())

def graph2(region):
    data = charge_data()
    data = data[(data["region"]== f"{region}")]
    return data

def graph(province):
    data = charge_data()
    data = data[(data["province"]== f"{province}")]
    return data

def chart_rates():
    data = charge_data2()
    data = data.groupby("Provincias").agg({"Unemployment rate":'sum'}).rename(columns = {"Provincias":"Provincias","Provincias":"Unemployment rate"}).reset_index().set_index("Provincias",drop = True)
    return data


