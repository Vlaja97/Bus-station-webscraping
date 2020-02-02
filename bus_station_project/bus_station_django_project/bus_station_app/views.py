from django.shortcuts import render
import request
import folium
import pickle
import json
import pandas as pd
from django.http import HttpResponse

def base(request):
    return render(request, 'base.html')

def show_map(request):
    with open('test83.json', 'r') as json_file:
        data = json.load(json_file)
        # Creating Folium map
        map = folium.Map(location=[45.251670,19.836940], zoom_start=15,width='75%', height='75%')
        tooltip = 'Click For more Info'
        # Creating Folium markers for bus stops
        for i in range(0,len(data)):
            folium.Marker([data[i]['Latitude'], data[i]['Longtitude']], popup=data[i]['Name'], tooltip=tooltip).add_to(map)
        

        map.save(r'/home/vlada/Documents/Projects/Bus-station/Bus-station-webscraping/bus_station_project/bus_station_django_project/bus_station_app/templates/map.html')
    
    context = {'my_map': map}
    #if i put 'base.html' it wont show map but is rendering right template
    return render(request, 'map.html', context)

