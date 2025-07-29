import csv

import matplotlib.pyplot as plt

from datetime import datetime

# Open and the read the  csv files
# Sitka file
file_name = 'data/sitka_weather_2018_simple.csv'
with open(file_name) as f:
    reader = csv.reader(f) # read the entire file
    header_row = next(reader) # get first line for the file
    
    # Get dates high temperatures from this sitka.
    sk_dates, sitka_highs = [], []
    # Loop through the entire file and get the max_tem values
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        sk_high = int(row[5]) # Get the MaxTem results 
        sk_dates.append(current_date)
        sitka_highs.append(sk_high)
    

# Death Valley file
file_name = 'data/death_valley_2018_simple.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    # Get dates, and high and low tempratures for this file.
    dv_dates, death_valley_highs, = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            dv_high = int(row[4])
            
        except ValueError:
            print(f"Missing date for {current_date}")
        else:
            dv_dates.append(current_date)
            death_valley_highs.append(dv_high)


# San Francisco file
filename = 'data/san_francisco.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    # Get dates high temperatures from this file.
    sf_dates, sf_highs = [], []
    # Loop through the entire file and get the max_tem values
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])  # Get the MaxTem results
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            sf_dates.append(current_date)
            sf_highs.append(high)
            


    # Plot the sitka and death valley high temperature.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(sk_dates, sitka_highs, c='red', alpha=0.5, label='Sitka') # display the dates and highs
    ax.plot(dv_dates, death_valley_highs, c='blue', alpha=0.5, label='Death Valley')
    ax.plot(sf_dates, sf_highs, c='orange', label='San Francisco',alpha=0.5)
    ax.legend()
    ax.set_ylim(20, 130)

    # Format Plot
    plt.title("Daily Sitka, Death Valley and San Francisco\nhigh temperatures", fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate() # draw the date diagonally
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.savefig('sitka_dv_sf_high_temps.png')
    plt.show()

