# https://www:.mois.go.kr/

import csv
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc

font_path = "python_data_A/src/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

f = open('python_data_A/csv_data/age.csv', 'r', encoding='utf8')
data = csv.reader(f)
yp = []
for k in range(2):
area = input("지역명 입력 : ")
for row in data:
    if area in row[0]:
        print("total :", row[1])
        for i in row[3:]:
            yp.append(int(i))

plt.title(area)
plt.style.use('ggplot')
plt.plot(yp)
plt.show()