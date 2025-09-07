import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font',family='Microsoft Jhenghei')

data = pd.read_csv('./travel.csv')
print(data)
data111 = data.iloc[3][2:-1]

dataX = data111.index.tolist()
dataY = data111.values.tolist()

dataY = [int(i) for i in dataY]

print(dataX,dataY)

plt.bar(dataX,dataY)

plt.show()
