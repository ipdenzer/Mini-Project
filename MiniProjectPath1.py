import pandas
import matplotlib.pyplot as plt
import statistics
import numpy as np


''' 
The following is the starting code for path1 for data reading to make your first step easier.
'dataset_1' is the clean data for path1.
'''
dataset_1 = pandas.read_csv('NYC_Bicycle_Counts_2016_Corrected.csv')
dataset_1['Total']                = pandas.to_numeric(dataset_1['Total'].replace(',','', regex=True))
dataset_1['Brooklyn Bridge']      = pandas.to_numeric(dataset_1['Brooklyn Bridge'].replace(',','', regex=True))
dataset_1['Manhattan Bridge']     = pandas.to_numeric(dataset_1['Manhattan Bridge'].replace(',','', regex=True))
dataset_1['Queensboro Bridge']    = pandas.to_numeric(dataset_1['Queensboro Bridge'].replace(',','', regex=True))
dataset_1['Williamsburg Bridge']  = pandas.to_numeric(dataset_1['Williamsburg Bridge'].replace(',','', regex=True))

def overall_traffic():

    # You want to install sensors on the bridges to estimate overall traffic across all the bridges.
    # But you only have enough budget to install sensors on three of the four bridges.
    # Which bridges should you install the sensors on to get the best prediction of overall traffic?

    i = 0
    bridges_traffic = [0] * 4
    while i < 214:
        j = 0
        while j < len(bridges_traffic):
            bridges_traffic[j] += (bridge_data[j])[i]
            j += 1
        i += 1

    print('                  Total Traffic      Average')
    print('Brooklyn Bridge    ', bridges_traffic[0], '         ', int(bridges_traffic[0] / 214))
    print('Manhattan Bridge  ', bridges_traffic[1], '        ', int(bridges_traffic[1] / 214))
    print('William Bridge     ', bridges_traffic[2], '        ', int(bridges_traffic[2] / 214))
    print('Queensboro Bridge  ', bridges_traffic[3], '         ', int(bridges_traffic[3] / 214))

    all_traffic_sum = (bridges_traffic[0] + bridges_traffic[1] + bridges_traffic[2] + bridges_traffic[3])

    print("\nBrooklyn Traffic Contribution: ", (bridges_traffic[0] / all_traffic_sum * 100))
    print("Manhattan Traffic Contribution: ", (bridges_traffic[1] / all_traffic_sum * 100))
    print("William Traffic Contribution: ", (bridges_traffic[2] / all_traffic_sum * 100))
    print("Queensboro Traffic Contribution: ", (bridges_traffic[3] / all_traffic_sum * 100))

    plt.plot(bridge_data[0])
    plt.plot(bridge_data[1])
    plt.plot(bridge_data[2])
    plt.plot(bridge_data[3])
    plt.title("Traffic Each Day Since April 1")
    plt.xlabel('Days Since April 1')
    plt.ylabel('Traffic')
    plt.legend(['Brooklyn Bridge', 'Manhattan Bridge', 'William Bridge', 'Queensboro Bridge'])
    plt.show()
    return


def traffic_prediction():

    # The city administration is cracking down on helmet laws, and wants to deploy police officers on days with high
    # traffic to hand out citations. Can they use the next day's weather forecast
    #  (low/high temperature and precipitation) to predict the total number of bicyclists that day?

    temp_average = [0] * 214
    i = 0
    peak_precipitation = []

    while i < 214:
        temp_average[i] = (temp_high[i] + temp_low[i]) / 2
        if precipitation[i] == 0:
            peak_precipitation.append(total_traffic[i])
        i += 1

    z = np.polyfit(temp_average, total_traffic, 2)
    predict = np.poly1d(z)

    corr_matrix = np.corrcoef(temp_average, predict(temp_average))
    corr = corr_matrix[0, 1]
    R_sq = corr ** 2
    print(R_sq)

    percent_precip = int((sum(peak_precipitation) / sum(total_traffic)) * 100)
    print(percent_precip, "percent of the traffic is at 0 precipitation")

    print("Standard Deviation :", (statistics.stdev(peak_precipitation)))

    plt.plot(temp_average, total_traffic, 'o')
    plt.title("Temperature and Total Traffic Comparison")
    plt.ylabel('Total Traffic')
    plt.xlabel('Average Temperature (Fahrenheit)')
    plt.legend(['Data'])
    plt.show()

    plt.plot(precipitation, total_traffic, 'o')
    plt.title("Precipitation and Total Traffic Comparison")
    plt.ylabel('Total Traffic')
    plt.xlabel('Precipitation (inches)')
    plt.legend(['Data'])
    plt.show()

    fig, ax = plt.subplots(figsize=(12, 5))
    ax2 = ax.twinx()
    ax.set_title('Precipitation and Temperature vs Total Traffic')
    ax.set_xlabel('Total Traffic')
    ax.plot(total_traffic, precipitation, 'o', color='red')
    ax2.plot(total_traffic, temp_average, 'o')
    ax.set_ylabel('Precipitation (inches)')
    ax2.set_ylabel('Average Temperature (Fahrenheit)')
    ax.legend(['Precipitation', 'Temperature'])
    ax2.legend(['Temperature'], loc='upper center')

    plt.show()

    return


def day_prediction():

    # Can you use this data to predict what day (Monday to Sunday) is today based on the number of
    # bicyclists on the bridges?

    i = 0
    sunday, monday, tuesday, wednesday, thursday, friday, saturday = [], [], [], [], [], [], []
    while i < 214:
        if day[i] == 'Sunday':
            sunday.append(total_traffic[i])
        elif day[i] == 'Monday':
            monday.append(total_traffic[i])
        elif day[i] == 'Tuesday':
            tuesday.append(total_traffic[i])
        elif day[i] == 'Wednesday':
            wednesday.append(total_traffic[i])
        elif day[i] == 'Thursday':
            thursday.append(total_traffic[i])
        elif day[i] == "Friday":
            friday.append(total_traffic[i])
        else:
            saturday.append(total_traffic[i])
        i += 1

    avg_traffic_day = [sunday, monday, tuesday, wednesday, thursday, friday, saturday]
    days = [0, 1, 2, 3, 4, 5, 6]
    for i in days:
        avg_traffic_day[i] = int(sum(avg_traffic_day[i]) / len(avg_traffic_day[i]))

    print('\nAverage Traffic Per Day')
    print('Day of the week: Sunday  Monday Tuesday Wednesday Thursday Friday Saturday')
    print('Average Traffic:', avg_traffic_day)

    max_traffic = [max(sunday), max(monday), max(tuesday), max(wednesday), max(thursday), max(friday), max(saturday)]
    min_traffic = [min(sunday), min(monday), min(tuesday), min(wednesday), min(thursday), min(friday), min(saturday)]

    print("\nMaximum Traffic Per Day:", max_traffic)
    print("Minimum Traffic Per Day:", min_traffic)
    print("Standard Deviation:     ", [int(statistics.stdev(sunday)), int(statistics.stdev(monday)),
                 int(statistics.stdev(tuesday)), int(statistics.stdev(wednesday)), int(statistics.stdev(thursday)),
                 int(statistics.stdev(friday)), int(statistics.stdev(saturday))])

    plt.plot(days, avg_traffic_day)
    plt.title("Average Traffic on Each Day of the Week")
    plt.ylabel('Average Traffic')
    plt.xlabel('Sunday    Monday    Tuesday  Wednesday  Thursday     Friday    Saturday')
    plt.legend(['Data'])
    plt.show()

    plt.plot(sunday, 'o')
    plt.plot(monday, 'o')
    plt.plot(tuesday, 'o')
    plt.plot(wednesday, 'o')
    plt.plot(thursday, 'o')
    plt.plot(friday, 'o')
    plt.plot(saturday, 'o')
    plt.title("Total Traffic on Each Day of the Week")
    plt.ylabel('Traffic')
    plt.xlabel('Days')
    plt.legend(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
    plt.show()

    plt.plot(saturday, 'o')
    plt.title("Total Traffic on Saturday")
    plt.ylabel('Traffic')
    plt.xlabel('Days')
    plt.legend(['Saturday'])
    plt.show()

    plt.plot(monday, 'o')
    plt.title("Total Traffic on Monday")
    plt.ylabel('Traffic')
    plt.xlabel('Days')
    plt.legend(['Monday'])
    plt.show()

    plt.plot(tuesday, 'o')
    plt.plot(thursday, 'o')
    plt.title("Total Traffic on Tuesday and Wednesday")
    plt.ylabel('Traffic')
    plt.xlabel('Days')
    plt.legend(['Tuesday', 'Thursday'])
    plt.show()
    return


if __name__ == "__main__":
    bridge_data = [dataset_1['Brooklyn Bridge'], dataset_1['Manhattan Bridge'], dataset_1['Williamsburg Bridge'],
                   dataset_1['Queensboro Bridge']]
    total_traffic = dataset_1['Total']
    precipitation = dataset_1['Precipitation']
    temp_high = dataset_1['High Temp']
    temp_low = dataset_1['Low Temp']
    day = dataset_1['Day']

    overall_traffic()
    traffic_prediction()
    day_prediction()

    #Newester




