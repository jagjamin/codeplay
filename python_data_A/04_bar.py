# https://www.mois.go.kr/
import matplotlib.pyplot as plt
import csv
# plt.bar([0, 1, 2, 4, 6, 10], [1, 2, 3, 5, 6, 7,])
plt.barh(range(6), [1, 2, 3, 5, 6, 7])

plt.show()


# f = open('', 'r', encoding='utf8')
# data = csv.reader(f)
# result = []
# for row in data:
#     if '양평읍' in row[0]:
#         for i in row[3:]:
#             result.append(int(i))

# plt.bar(range(101), result)
# plt.bar(range(101), result)
# plt.show()