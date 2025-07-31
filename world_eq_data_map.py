import json 

from plotly.graph_objs import Layout
from plotly import offline

# Explore the structure of the data
filename = 'data/world_eq.json'
with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)  # store the entire json data

# Set the world data title
wld_eq_title = all_eq_data['metadata']['title']

all_eq_dicts = all_eq_data['features']
mags , lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Draw the map
data = [
    {
        'type': 'scattergeo', 
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker': {
            'size': [3*mag for mag in mags],
            'color': mags,  # Detemind colour used
            'colorscale': 'Bluered',  # metermind which color to display
            'reversescale': True,  # determind how the color will be reversed
            'colorbar': {
                'title': 'Magnitude'  # Display title on the sidebar color
            },
        },
    }
]

my_layout = Layout(title=wld_eq_title)

fig = {
    'data': data, 'layout': my_layout
}

offline.plot(fig, filename='world_eq_data.html')