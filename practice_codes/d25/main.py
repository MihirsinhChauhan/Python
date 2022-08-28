# with open("226 weather-data.csv") as weather_data:
#    weather_data_list = weather_data.readlines()
#    for data in weather_data_list:
#       weather_data_list[weather_data_list.index(data)] = data.strip()
#
#    print(weather_data_list)

# import csv
#
# with open("226 weather-data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temp = []
#     for row in data:
#         try:
#             temp.append(int(row[1]))
#
#         except:
#             pass
#
# print(temp)

# import pandas
# data = pandas.read_csv("226 weather-data.csv")
# #print(data)
# # temp_list  = data["temp"].to_list()
# # print(data["temp"].mean())
# # print(data["temp"].max())
#
# # print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.temp*9/5+ 32)

import pandas

data = pandas.read_csv("228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
gray_sq = 0
cinnamon_sq = 0
black_sq = 0

color_data = data["Primary Fur Color"].to_list()
for color in color_data:
    if color == "Gray":
        gray_sq += 1
    elif color == "Cinnamon":
        cinnamon_sq += 1
    else:
        black_sq += 1
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_sq, cinnamon_sq, black_sq]
}

sq_fur_data = pandas.DataFrame(data_dict)
sq_fur_data.to_csv("sq_fur_data.csv")
