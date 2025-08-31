import matplotlib.pyplot as plt
import pandas as pd

datas = pd.read_csv('./FMSRFK_2330_2025.csv',encoding='big5',header=1)
# print(datas.iloc[0])
print(datas.columns)
# print(datas['最高價'])
# print(datas)

# datamax = list(datas['最高價'])[:8]
# datamax = datas['最高價'].tolist()[:8]
datamax = datas['最高價'].dropna().tolist()
datamin = datas['最低價'].dropna().tolist()

datax = [1,2,3,4,5,6,7,8]
datamax_number = [float(i.replace(',','')) for i in datamax]
datamin_number = [float(i.replace(',','')) for i in datamin]
plt.rc('font',family='Microsoft Jhenghei')

plt.plot(datax,datamax_number,color='red',label='最高價',marker='o')
plt.plot(datax,datamin_number,color='blue',label='最低價',marker='o')

plt.title('114年1-8月份台積電月成交資訊')
plt.xlabel('月份')
plt.ylabel('股價')

plt.ylim(700,1300)

plt.yticks(range(700,1300,50))

plt.grid(axis='y', color="#ccc", linewidth=1, linestyle='-.')

plt.legend()

plt.show()