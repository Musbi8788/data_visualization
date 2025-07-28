import csv

import matplotlib.pyplot as plt

from datetime import datetime

file_name = 'data/sitka_weather_2018_simple.csv'
with open(file_name) as f:
    reader = csv.reader(f) # read the entire file
    header_row = next(reader) # get first line for the file
    
    # Get dates high temperatures from this file.
    dates, highs, lows = [], [], []
    # Loop through the entire file and get the max_tem values
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5]) # Get the MaxTem results 
        low = int(row[6]) # Get the MinTem results
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    
    

    # Plot the high and low temperature.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5) # display the dates and highs
    ax.plot(dates, lows, c='blue', alpha=0.5)

    # Format Plot
    plt.title("Daily high and low temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate() # draw the date dagonally
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # Add a shading between highs and lows fill.

    plt.show()

