import csv

# with open('weather_data.csv', mode='r') as data_file:
#     data = data_file.readlines()

temperatures = []
with open('weather_data.csv', mode='r') as data_file:
    data = csv.reader(data_file)
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

print(temperatures)
