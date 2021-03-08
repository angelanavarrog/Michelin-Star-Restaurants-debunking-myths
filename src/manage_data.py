import pandas as pd

def charge_data():
    restaurants = pd.read_csv('output/restaurants.csv')
    return restaurants

def charge_data2():
    province_data = pd.read_csv('output/province_data.csv')
    return province_data

def bar_chart_st():
    data = charge_data()
    data = data.groupby("province").agg({"michelin_stars":'count'}).rename(columns = {"province":"province","province":"Total Michelin Stars"}).reset_index().set_index("province",drop = True)
    return data

def province_list():
    data = charge_data()
    return list(data.province.unique())

def province_list():
    data = charge_data()
    return list(data.province.unique())