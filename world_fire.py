import csv

from plotly.graph_objs import Layout, Scattergeo

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    lons, lats, brightness = [], [], []
    for row in reader:
        lat = row[0]
        lon = row[1]
        brtns = row= [2]
        
