import csv
f = open('python_data_A\csv_data\yp.csv','r', encoding = 'utf8')
data = csv.reader(f , delimiter=',')
# print(data, type(data))
# print(type(f))
header = next(data)
max = -100
max_date = ""
min = 100
min_date = ""
for row in data:
    row[0] = row[0].lstrip('/t')
    if row[-1] == "":
        row[-1] = -999
    if row[-2] == "":
        row[-2] = 999
    row[-1],row[-2] = float(row[-1]),float(row[-2])

    if -999 < row[-2] < min:
        min = row[-2]
        min_date = row[0]
    if max < row[-1] < 999:
        max = row[-1]
        max_date = row[0]
        
print(max_date, max)
print(min_date, min)
        

f.close()