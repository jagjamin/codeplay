import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

axes[0, 0].plot(x, y1, label='sin(x)', color='blue')
axes[0, 0].set_title('Line Plot 1')
axes[0, 0].legend()

axes[0, 1].plot(x, y2, label='cos(x)', color='orange')
axes[0, 1].set_title('Line Plot 2')
axes[0, 1].legend()

axes[1, 0].plot(x, y3, label='tan(x)', color='green')
axes[1, 0].set_title('Line Plot 3')
axes[1, 0].legend()

axes[1, 1].plot(x, y4, label='exp(-x)', color='red')
axes[1, 1].set_title('Line Plot 4')
axes[1, 1].legend()

plt.tight_layout()

plt.show()

'''
우리 고장의  인구분포 분석하기

1.인구데이터를 1세 남녀따로, 1세 남녀 합, 10세 남녀 따로, 10세 남녀 합을 만든다
2.전체 인구분포(bar), 남녀구분 인구분포(항아라) 그래프를 그려본다
3.세대별(10세기준) 인구비율을 남녀 합과 남녀  별도 두개의 파이차트로 그려본다
4.5개의 그래프를 한 장으로 그려본다
6.데이터 분석결과를 문서로 제출 한다