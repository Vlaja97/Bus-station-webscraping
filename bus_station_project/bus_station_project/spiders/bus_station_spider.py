import scrapy
import json
import csv
import sys
from pprint import pprint
import pandas
from collections import defaultdict


class BusStationSpider(scrapy.Spider):
    name = "bus_station"
    allowed_domains = ['www.gspns.rs']
    start_urls = ['http://www.gspns.rs/mreza-get-stajalista-tacke?linija=1']
    lists = []

    def parse(self, response):
        parsed_json = json.loads(response.body)
        # Split Data by PIPE ' | '
        split_by_pipe = [line.split('|') for line in parsed_json]

        # Divide bus lines for each buss
        busses = [x[0] for x in split_by_pipe]

        # Find Longtitude and Latitude
        longtitude = [x[1] for x in split_by_pipe]
        latitude = [x[2] for x in split_by_pipe]
        #print(longtitude, latitude)

        # Name of the Bus station
        name_of_bus_station = [x[3] for x in split_by_pipe]

        # Pair Data in dict
        result = defaultdict(dict)
        for name_of_bus_station, b, ln, lg in zip(name_of_bus_station, busses, longtitude, latitude):
            result[name_of_bus_station] = {'busses': b, 'longtitude': ln, 'latitude': lg}
        pprint (result)

        with open('data_json.json', 'w') as outfile:
            json.dump(result, outfile, indent=4)

        
        

        
