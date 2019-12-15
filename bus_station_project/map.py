import folium
from folium.plugins import MarkerCluster
import os
import json
from pprint import pprint
from collections import OrderedDict
import pandas as pd
import pickle


# Opening JSON file that we scraped and reading it as Pandas data frame
#df = json.loads('data_json.json')

with open('data.pickle', 'rb') as pickle_file:
  data = pickle.load(pickle_file)

  map = folium.Map(location=[45.251670,19.836940], zoom_start=14)
  address =45.255203707
  address2 = 19.8416504854
  tooltip = 'Click For more Info'
  #for col in df:
  # val = df[col]
  print(type(data[0][2]))
  #pprint(data)
  #for each in toilets.iterrows():
  #    popup = 'Add <b>test</b>'
   #   print(list([each[1].GeoY,each[1].GeoX]))
  #    print(list(OSGB36toWGS84(each[1]['GeoX'],each[1]['GeoY'])))
  #   folium.Marker(list(OSGB36toWGS84(each[1]['GeoX'],each[1]['GeoY'])), popup=popup).add_to(marker_cluster)

  #print(list(df.columns.values))
  for i in range(0,len(data)):
   folium.Marker([data[i][3], data[i][2]], popup='<strong>Location One</strong>', tooltip=tooltip).add_to(map)

  #for col in df:
  # print(col)


  map.save('map.html')#