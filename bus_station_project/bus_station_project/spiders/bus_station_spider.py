import scrapy
import json
import csv
import sys
from pprint import pprint
import pandas as pd
from collections import defaultdict
import re
import ast

class BusStationSpider(scrapy.Spider):
    name = "bus_station"
    allowed_domains = ['www.gspns.rs']
    # Getting url from local bus company and scraping data for each bus
    start_urls = ['http://www.gspns.rs/mreza-get-stajalista-tacke?linija=1']
    lists = []

    def parse(self, response):
        parsed_json = json.loads(response.body)
        # Split Data by PIPE ' | '
        split_by_pipe = [line.split('|') for line in parsed_json]
       # print(split_by_pipe)

        # Divide bus lines for each buss
        buses = [x[0] for x in split_by_pipe]
        
        parsed_buses_temp = [x.split(',') for x in buses]
        #print(parsed_buses_temp)
        # Find Longtitude and Latitude
        longtitude = [x[1] for x in split_by_pipe]
        latitude = [x[2] for x in split_by_pipe]
        #print(latitude)
        # Convert to list of floats
        parsed_lon = [float(x) for x in longtitude]
        parsed_lat = [float(x) for x in latitude]
        
        
        # Name of the Bus station
        name_of_bus_station = [x[3] for x in split_by_pipe]
        #print(longtitude)
  
        # Pair Data in dict
        #result = defaultdict(dict)
        #for name_of_bus_station, b, ln, lg in zip(name_of_bus_station, parsed_buses_temp, parsed_lon, parsed_lat):
         #   result[name_of_bus_station] = {1: b, 2: ln, 3: lg}
        #pprint (result)
        result = list(zip(name_of_bus_station,parsed_buses_temp,parsed_lon,parsed_lat))
        


        with open('data_json.json', 'w') as outfile:
            json.dump(result, outfile, indent=4)
        #pprint(result)
        
        

        
