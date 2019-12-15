import folium
from folium.plugins import MarkerCluster
import os
import json
from pprint import pprint
from collections import OrderedDict
import pandas as pd


# Opening JSON file that we scraped and reading it as Pandas data frame
df = pd.read_json('data_json.json')
map = folium.Map(location=[45.251670,19.836940], zoom_start=14)
address =45.255203707
address2 = 19.8416504854
tooltip = 'Click For more Info'
#for col in df:
 # val = df[col]
print(df[2])
print(df)


#print(list(df.columns.values))
for i in range(0,len(df)):
  folium.Marker([df.loc[i][2], df.loc[i][3]], popup='<strong>Location One</strong>', tooltip=tooltip).add_to(map)

#for col in df:
 # print(col)


map.save('map.html')#