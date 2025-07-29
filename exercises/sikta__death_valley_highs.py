import csv

import matplotlib.pyplot as plt

from datetime import datetime

file_name = 'data/sitka_weather_2018_simple.csv'
with open(file_name) as f:
    reader = csv.reader(f) # read the entire file
    header_row = next(reader) # get first line for the file
    
    # Get dates high temperatures from this sitka.
    dates, sitka_highs = [], []
    # Loop through the entire file and get the max_tem values
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        sk_high = int(row[5]) # Get the MaxTem results 
        dates.append(current_date)
        sitka_highs.append(sk_high)
    

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header)
    # for index , column_reader in enumerate(header_row):
    #     print(index, column_reader)

    # Get dates, and high and low tempratures for this file.
    dates, death_valley_highs, = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            dv_high = int(row[4])
            
        except ValueError:
            print(f"Missing date for {current_date}")
        else:
            dates.append(current_date)
            death_valley_highs.append(dv_high)
            


    # Plot the sitka and death valley high temperature.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, sitka_highs, c='red', alpha=0.5) # display the dates and highs
    ax.plot(dates, death_valley_highs, c='blue', alpha=0.5)

    # Format Plot
    plt.title("Daily Sitka and Death Valley high temperatures - 2018", fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate() # draw the date dagonally
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.fill_between(dates, sitka_highs, death_valley_highs, facecolor='blue', alpha=0.1) # Add a shading between sitka and death vally highs fill.
    plt.savefig('sikta_death_valley_high_tem.png')
    plt.show()

