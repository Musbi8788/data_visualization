import csv

import matplotlib.pyplot as plt

from datetime import datetime

file_name = 'data/sitka_weather_2018_simple.csv'
with open(file_name) as f:
    reader = csv.reader(f) # read the entire file
    header_row = next(reader) # get first line for the file
    for index, col_row in enumerate(header_row):
        print(index, col_row)
    
    # Get dates high temperatures from this file.
    dates, rain_falls = [], []
    # Loop through the entire file and get the max_tem values
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rain = float(row[3])
        dates.append(current_date)
        rain_falls.append(rain)


    # Plot the high and low temperature.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, rain_falls, c='green')
    # Format Plot
    plt.title("Daily Rain Fall temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate() # draw the date dagonally
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    # plt.savefig('sitka_rainfall.png',    bbox_inches="tight")

    plt.show()

