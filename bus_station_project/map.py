import folium
from folium.plugins import MarkerCluster
import os
import json
from pprint import pprint
from collections import OrderedDict
import pandas as pd
import pickle


# Opening PICKLE file that we scraped and reading it 
with open('data.pickle', 'rb') as pickle_file:
  data = pickle.load(pickle_file)
  # Creating Folium map
  map = folium.Map(location=[45.251670,19.836940], zoom_start=15,width='75%', height='75%')
  tooltip = 'Click For more Info'
 
  # Creating Folium markers for bus line
  for i in range(0,len(data)):
    folium.Marker([data[i][3], data[i][2]], popup=data[i][0], tooltip=tooltip).add_to(map)

  map.save('map.html')