import csv
import pandas

# with open("weather_data.csv") as file:
#     data = file.readlines()
# data = [i.strip(chr(10)) for i in data]
# print("data")
# print(data)
#
# print("csv")
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for i in data:
#         if i[1] != "temp":
#             temperature.append(int(i[1]))
# print(temperature)
data = pandas.read_csv("weather_data.csv")
# print("pandas")
# print(type(data["temp"]))
# print(type(data))
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
# data_list = data["temp"].to_list()
# print("list")
# print(data_list)

# avg = sum(data_list) / len(data_list)
# print(data)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.temp*9/5 +32)