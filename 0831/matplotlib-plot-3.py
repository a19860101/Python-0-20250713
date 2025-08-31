import matplotlib.pyplot as plt

plt.rc('font', family='Microsoft Jhenghei')

dataX = [1,2,3,4,5,6,7]
dataY = [32,30,26,28,16,20,22]

dataY2 = [18,20,35,20,15,2,0]

plt.plot(dataX, dataY, label='8月第四周')
plt.plot(dataX, dataY2, label='8月第三周')

# plt.xlim(1,30)
plt.ylim(0,50)

# plt.xticks(range(1,30,2))
plt.yticks(range(0,50,5))

plt.title('一周天氣')
plt.xlabel('星期')
plt.ylabel('溫度')

plt.legend()

plt.show()
