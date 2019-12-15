import folium
from folium.plugins import MarkerCluster
import os
import json
from pprint import pprint
from collections import OrderedDict
import pandas as pd

map = folium.Map(location=[45.251670,19.836940], zoom_start=14)
address =[45.255203707,19.8416504854]
address2 = [45.253337,19.844187]
tooltip = 'Click For more Info'
# Opening JSON file that we scraped and reading it as Pandas data frame
df = pd.read_json('data_json.json')
print(type(df))
for row in df.keys():
  #val = df[row]
  #print(df)
  print(row)
  #folium.Marker(location=[row[0],row[1]], popup='<strong>Location One</strong>', tooltip=tooltip).add_to(map)

#for col in df:
 # print(col)


map.save('map.html')#