import scrapy
import json
import csv
import sys
from pprint import pprint
import pandas as pd
import re
import ast
import pickle
import os

class BusStationSpider(scrapy.Spider):
    name = "bus_station"
    allowed_domains = ['www.gspns.rs']
    # Getting url from local bus company and scraping data for each bus
    start_urls = ['http://www.gspns.rs/mreza-get-stajalista-tacke?linija=83']
    lists = []
    for url in start_urls:
        def parse(self, response):
            parsed_json = json.loads(response.body)
            # Split Data by PIPE ' | '
            split_by_pipe = [line.split('|') for line in parsed_json]

            # Divide bus lines for each buss
            buses = [x[0] for x in split_by_pipe]
            parsed_buses_temp = [x.split(',') for x in buses]

            # Find Longtitude and Latitude
            longtitude = [x[1] for x in split_by_pipe]
            latitude = [x[2] for x in split_by_pipe]
        
            # Convert to list of floats
            parsed_lon = [float(x) for x in longtitude]
            parsed_lat = [float(x) for x in latitude]
            
            
            # Name of the Bus station
            name_of_bus_station = [x[3] for x in split_by_pipe]
    
            # Pair Data in Tuple
            # Maybe is better to create Dictionaries!

            
    
            

            result = [{"Name": n,"buses": b,"Latitude": lat,"Longtitude": lon} for n, b, lat, lon in zip(name_of_bus_station, parsed_buses_temp, parsed_lat, parsed_lon)]

            #path = '/home/vlada/Documents/Projects/Bus-station/Bus-station-webscraping/bus_station_project/bus_station_django_project/bus_station_app'
            with open(r'/home/vlada/Documents/Projects/Bus-station/Bus-station-webscraping/bus_station_project/bus_station_django_project/test83.json', 'w') as outfile:
                json.dump(result, outfile)
        
        
        

        
