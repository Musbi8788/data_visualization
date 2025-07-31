import json

# Explore the structure of the data
filename = 'data/eq_1_day_m1.json'
with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f) # store the entire json data

all_eq_dicts = all_eq_data['features'] # get all the feature in the eq data

mags ,lons, lats= [], [] ,[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag'] # Get the mag value
    lon = eq_dict['geometry']['coordinates'][0] # Get lon
    lat = eq_dict['geometry']['coordinates'][1] # Get lat
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
print(mags[:10]) # display the first 10 mags in a list
print(lons[:10])
print(lats[:10])