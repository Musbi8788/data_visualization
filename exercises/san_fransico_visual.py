import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'data/san_fransico.csv' 
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    # Loop through the hearder row
    for index, col_row in enumerate(header):
        print(index, col_row)

    # Get dates high temperatures from this file.
    dates, highs, lows = [], [], []
    # Loop through the entire file and get the max_tem values
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])  # Get the MaxTem results
            low = int(row[5])  # Get the MinTem results
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # Plot the high and low temperature for Fransico.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)  # display the dates and highs
    ax.plot(dates, lows, c='blue', alpha=0.5)

    # Format Plot
    plt.title("Daily high and low temperatures - 2025", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # draw the date dagonally
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    # Add a shading between highs and lows fill.
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    plt.show()
