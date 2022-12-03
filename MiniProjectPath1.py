import pandas
import matplotlib.pyplot as plt
''' 
The following is the starting code for path1 for data reading to make your first step easier.
'dataset_1' is the clean data for path1.
'''
dataset_1 = pandas.read_csv('NYC_Bicycle_Counts_2016_Corrected.csv')
dataset_1['Brooklyn Bridge']      = pandas.to_numeric(dataset_1['Brooklyn Bridge'].replace(',','', regex=True))
dataset_1['Manhattan Bridge']     = pandas.to_numeric(dataset_1['Manhattan Bridge'].replace(',','', regex=True))
dataset_1['Queensboro Bridge']    = pandas.to_numeric(dataset_1['Queensboro Bridge'].replace(',','', regex=True))
dataset_1['Williamsburg Bridge']  = pandas.to_numeric(dataset_1['Williamsburg Bridge'].replace(',','', regex=True))
dataset_1['Williamsburg Bridge']  = pandas.to_numeric(dataset_1['Williamsburg Bridge'].replace(',','', regex=True))

# print(dataset_1.to_string()) #This line will print out your data


def overall_traffic():

    # You want to install sensors on the bridges to estimate overall traffic across all the bridges.
    # But you only have enough budget to install sensors on three of the four bridges.
    # Which bridges should you install the sensors on to get the best prediction of overall traffic?

    i = 0
    man_bridge_total = 0
    brook_bridge_total = 0
    queen_bridge_total = 0
    william_bridge_total = 0

    while i < 214:
        man_bridge_total += man_bridge[i]
        brook_bridge_total += brook_bridge[i]
        queen_bridge_total += queen_bridge[i]
        william_bridge_total += william_bridge[i]
        i += 1

    print('                  Total Traffic      Average')
    print('Mannhattan Bridge', man_bridge_total, '          ', int(man_bridge_total / 214))
    print('Brooklyn Bridge  ', brook_bridge_total, '           ', int(brook_bridge_total / 214))
    print('Queensboro Bridge', queen_bridge_total, '           ', int(queen_bridge_total / 214))
    print('William Bridge   ', william_bridge_total, '          ', int(william_bridge_total / 214))

    plt.plot(man_bridge)
    plt.plot(brook_bridge)
    plt.plot(queen_bridge)
    plt.plot(william_bridge)
    plt.title("Traffic Each Day")
    plt.xlabel('Day')
    plt.ylabel('Traffic')
    plt.legend(['Mannhattan Bridge', 'Brooklyn Bridge', 'Queensboro Bridge', 'William Bridge'])
    plt.show()
    return


def traffic_prediction():

    # The city administration is cracking down on helmet laws, and wants to deploy police officers on days with high
    # traffic to hand out citations. Can they use the next day's weather forecast
    #  (low/high temperature and precipitation) to predict the total number of bicyclists that day?

    temp_average = [0] * 214
    i = 0
    while i < 214:
        temp_average[i] = (temp_high[i] + temp_low[i]) / 2
        i += 1

    plt.plot(temp_average, total_traffic)
    plt.title("Temperature and Total Traffic Comparison")
    plt.ylabel('Traffic')
    plt.xlabel('Average Temperature')
    plt.legend(['Total Traffic'])
    plt.show()

    plt.hist(y=, x=, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
    plt.title("Precipitation and Total Traffic Comparison")
    plt.ylabel('Traffic')
    plt.xlabel('Precipitation')
    plt.legend(['Total Traffic'])
    plt.show()

    return


def day_prediction():

    # Can you use this data to predict what day (Monday to Sunday) is today based on the number of
    # bicyclists on the bridges?

    total_traffic_days = [0] * 7
    day = 5
    i = 0

    while i < 214:
        total_traffic_days[day] = total_traffic[i]
        i += 1
        day += 1
        if day == 7:
            day = 0
    print('Day:     Sunday     Monday   Tuesday   Wednesday  Thursday Friday   Saturday')
    print('Traffic', tuple(total_traffic_days))

    plt.plot(total_traffic_days)
    plt.title("Traffic on Each Day of the Week")
    plt.ylabel('Traffic')
    plt.xlabel('Weekday')
    plt.legend(['Total Traffic'])
    plt.show()

    return


if __name__ == "__main__":
    man_bridge = dataset_1['Manhattan Bridge']
    brook_bridge = dataset_1['Brooklyn Bridge']
    queen_bridge = dataset_1['Queensboro Bridge']
    william_bridge = dataset_1['Williamsburg Bridge']
    total_traffic = (dataset_1['Total'])
    precipitation = dataset_1['Precipitation']
    temp_high = dataset_1['High Temp']
    temp_low = dataset_1['Low Temp']

    #overall_traffic()
    traffic_prediction()
    #day_prediction()

