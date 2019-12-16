from django.shortcuts import render
import requests
import folium
import pickle
import json
from django.http import HttpResponse



def base(request):
    return render(request, 'base.html')

def show_map(request):
    with open('data.pickle', 'rb') as pickle_file:
        data = pickle.load(pickle_file)
        print(data)
        # Creating Folium map
        map = folium.Map(location=[45.251670,19.836940], zoom_start=15,width='75%', height='75%')
        tooltip = 'Click For more Info'
        
        # Creating Folium markers for bus line
        for i in range(0,len(data)):
            folium.Marker([data[i][3], data[i][2]], popup=data[i][0], tooltip=tooltip).add_to(map)

        map.save(r'C:\Users\wlajk\Documents\Projects\bus-staion-webscraping\Bus-station-webscraping\bus_station_project\bus_station_django_project\bus_station_app\templates\map.html')
    return render(request, 'map.html')

