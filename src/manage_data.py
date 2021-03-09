import pandas as pd

def charge_data():
    restaurants = pd.read_csv('output/restaurants.csv')
    return restaurants

def charge_data2():
    province_data = pd.read_csv('output/province_data.csv')
    return province_data

def rename_id(x):
    x = f"Province {x}"
    return x

def bar_chart():
    data = charge_data()
    data = data.groupby("region").agg({"michelin_stars":'count'}).rename(columns = {"region":"region","region":"Total Michelin Stars"}).reset_index().set_index("region",drop = True)
    return data

def bar_chart_st():
    data = charge_data()
    data = data.groupby("province").agg({"michelin_stars":'count'}).rename(columns = {"province":"province","province":"Total Michelin Stars"}).reset_index().set_index("province",drop = True)
    return data

def province_list():
    data = charge_data()
    return list(data.province.unique())

def region_list():
    data = charge_data()
    return list(data.region.unique())

def graph(region):
    data = charge_data()
    data = data[(data["region"]== f"{province}")]
    data = data[["region","michelin_stars"]].reset_index(drop=True)
    data["region"]= data.index+1
    data["region"]= data.regions.apply(rename_id)
    return data