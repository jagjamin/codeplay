# https://www.mois.go.kr/
import csv
import matplotlib.pyplot as plt

f = open('python_data_A/csv_data/yp_mf.csv', 'r', encoding='utf8')
data = csv.reader(f)
m =[] # 남성 연령대 
f =[] # 여성 연령대

result = []
for row in data :
    if'양서' in row[0]:
        # print(row)
        for i in row[3:104]: # 남성리스트 시작과 끝
            m. append (-(int(i)))
        for j in row[106:]: # 여성리스트 시작과 끝
            f. append (int(j))

#         for i in range(0, 101) :
#             m. append(-int (row[ (1*3)]))
#             f.append(int(row[- (1+1)]))
# f. reverse()
plt. style.use('ggplot')
plt. figure(figsize=(10,5), dpi=150)
plt.rc('font', family = 'Malgun Gothic') # 한글을 쓰기위해
plt.rcParams['axes.unicode_minus'] = False # 특수기호를 utf-8로 쓰기위해
plt.title("양평군 양평읍 성별분포")
plt.barh(range(101), m, label = "남성")
plt.barh(range(101), f, label = "여성") 
plt.legend()
plt.show()
