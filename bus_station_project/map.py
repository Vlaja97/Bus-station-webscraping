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

#with open('data_json.json') as json_file:
#    data = pd.read_json(json_file)
#print (data)

folium.Marker(address, 
               popup='<strong>Location One</strong>',
               tooltip=tooltip).add_to(map)


map.save('map.html')