import csv

import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header)
    for index , column_reader in enumerate(header_row):
        print(index, column_reader)

    # Get dates, and high and low tempratures for this file.
    dates, highs, lows, rains = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
            low = int(row[5])
            rain = int(float(row[3]))
        except ValueError:
            print(f"Missing date for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            rains.append(rain)

    # Plot the high and low temperature.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)  # display the dates and highs
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.plot(dates, rains, c='green', alpha=0.5)


    # Format Plot
    plt.title("Daily high and low temperatures - 2018\nDeath Velley, CA", fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # draw the date dagonally
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    # Add a shading between highs and lows fill.
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    plt.show()
