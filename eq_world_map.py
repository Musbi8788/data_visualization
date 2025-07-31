import json

from plotly.graph_objs import Layout
from plotly import offline

# Explore the structure of the data
filename = 'data/eq_data_30_days_m1.json'
with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)  # store the entire json data

all_eq_dicts = all_eq_data['features']  # get all the feature in the eq data

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']  # Get the mag value
    lon = eq_dict['geometry']['coordinates'][0]  # Get lon
    lat = eq_dict['geometry']['coordinates'][1]  # Get lat
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Map the earthequakes
data = [
    {
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'marker': {
            'size': [3*mag for mag in mags],
            'color': mags, # Detemind colour used
            'colorscale': 'Rainbow',  # metermind which color to display
            'reversescale': True, # determind how the color will be reversed
            'colorbar': {
                'title': 'Magnitude' # Display title on the sidebar color
                        },
            },
        
    },
]
my_layout = Layout(title='Global Earthquakes') # set the map title

fig = {'data':data, 'layout':my_layout} # configure the data and it's layout into a dict
offline.plot(fig, filename='global_earthquakes.html')
