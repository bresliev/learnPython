import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = data["Primary Fur Color"]
count_colors = color.value_counts()
print(count_colors.values)
print(count_colors.index.values)


count_dict = {"Fur color": count_colors.index.values,
              "Count": count_colors.values}
print(count_dict)
df = pandas.DataFrame(count_dict)
df.to_csv("squirrel_count.csv")
data2 = pandas.read_csv("squirrel_count.csv")
print(data2)