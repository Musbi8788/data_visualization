import csv

from plotly.graph_objs import Layout, Scattergeo

from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    lons, lats, scans, brightness = [], [], [], []
    for row in reader:
        lat = float(row[0])
        lon = float(row[1])
        brightness_value = int(float(row[2]))
        scan_value = float(row[3])
        lats.append(lat)
        lons.append(lon)
        brightness.append(brightness_value)
        scans.append(scan_value)

# Map the global fire data
data = [
    {
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'marker': {
            'size': [scan * 5 for scan in scans],
            'color': brightness,  # Detemind colour used
            'colorscale': 'Rainbow',  # metermind which color to display
            'reversescale': True,  # determind how the color will be reversed
            'colorbar': {
                'title': 'Fire Scan Width'  # Display title on the sidebar color
            },
        },

    },
]
# set the map title
my_layout = Layout(title='Global Fires - 1 Day Snapshot (2018)')

# configure the data and it's layout into a dict
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fire.html')
