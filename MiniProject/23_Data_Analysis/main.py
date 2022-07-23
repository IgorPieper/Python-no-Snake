import pandas

tabelka = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = []
how_many = []

for n in tabelka["Primary Fur Color"]:
    if n in colors:
        pass
    else:
        colors.append(n)

for n in colors:
    how_many.append(0)

for n in tabelka["Primary Fur Color"]:
    for m in range(0, len(colors)):
        if n == colors[m]:
            how_many[m] += 1

data = {}
color = []
amount = []

for n in range(1, len(colors)):
    color.append(colors[n])

for n in range(1, len(how_many)):
    amount.append(how_many[n])

data["color"] = color
data["amount"] = amount

results = pandas.DataFrame(data)
print(results)
results.to_csv("results.csv")
