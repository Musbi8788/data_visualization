import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'data/san_francisco.csv' 
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)



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

    # Plot the high and low temperature for Francisco.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5, label='High')  # display the dates and highs
    ax.plot(dates, lows, c='blue', alpha=0.5, label='Low')
    ax.legend()

    # Format Plot
    plt.title("Daily high and low temperatures\nSan Francisco  2025", fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # format the xais date labels diagonally
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    # Shade area between highs and lows fill.
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    plt.show()
