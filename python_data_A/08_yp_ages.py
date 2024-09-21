import csv
import matplotlib.pyplot as plt

f = open('python_data_A\csv_data\yp.csv', 'r', encoding='utf8')
data = csv.reader(f)
yp_all = []

for i in data:
    yp_all.append(i)

print(type(yp_all[0][3]))

if "," in yp_all[0][3]:
    yp_all[0][3] = int(yp_all[0][3].replace(",",""))
    
print(type(yp_all[0][3]))