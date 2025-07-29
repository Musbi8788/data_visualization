import csv

import matplotlib.pyplot as plt

from datetime import datetime

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
    

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header)
    # for index , column_reader in enumerate(header_row):
    #     print(index, column_reader)

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
            


    # Plot the sitka and death valley high temperature.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(sk_dates, sitka_highs, c='red', alpha=0.5, label='Sitka') # display the dates and highs
    ax.plot(dv_dates, death_valley_highs, c='blue', alpha=0.5, label='Death Valley')
    ax.legend()
    ax.set_ylim(20, 130)

    # Format Plot
    plt.title("Daily Sitka and Death Valley high temperatures - 2018", fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate() # draw the date diagonally
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.fill_between(sk_dates, sitka_highs, death_valley_highs, facecolor='blue', alpha=0.1) # Shade the area between Sitka and Death Valley highs fill.
    plt.savefig('sitka_death_valley_high_temps.png')
    plt.show()

