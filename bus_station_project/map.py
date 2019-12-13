import folium
from folium.plugins import MarkerCluster
import os
import json
from pprint import pprint
from collections import OrderedDict
import pandas as pd

map = folium.Map(location=[45.251670,19.836940], zoom_start=14)
address =[45.255203707,19.8416504854]
tooltip = 'Click For more Info'
# Opening JSON file that we scraped and reading it as Pandas
with open('data_json.json') as json_file:
    data = pd.read_json(json_file)
#print (data)



#folium.Marker(data[], popup='<strong>Location One</strong>', tooltip=tooltip).add_to(map)
#for i in range(0,len(data)):
  #  folium.Marker([data.row[i]['longtitude'], data.row[i]['latitude']], popup=data.row[i]['busses']).add_to(map)


#folium.Marker(location=[data['busses':'latitude']]).add_to(map)
print(data[: ,'BUL. CARA LAZARA - URBIS'])


map.save('map.html')