import csv

import matplotlib.pyplot as plt

from datetime import datetime

file_name = 'data/sitka_weather_07-2018_simple.csv'
with open(file_name) as f:
    reader = csv.reader(f) # read the entire file
    header_row = next(reader) # get first line for the file
    
    # Get dates high temperatures from this file.
    dates, highs = [], []
    # Loop through the entire file and get the max_tem values
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5]) # Get the MaxTem results start from the values becuase we already get the headings.
        dates.append(current_date)
        highs.append(high)

    
    

    # Plot the high temperature.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red') # display the dates and highs

    # Format Plot
    plt.title("Daily high temperatures, July 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate() # draw the date dagonally
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

