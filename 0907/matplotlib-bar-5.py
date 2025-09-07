import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font',family='Microsoft Jhenghei')

data = pd.read_csv('./travel.csv')

print(data)
label = data.columns.tolist()[2:-1]

data_109 = [int(i) for i in data.iloc[1][2:-1]]
data_110 = [int(i) for i in data.iloc[2][2:-1]]
data_111 = [int(i) for i in data.iloc[3][2:-1]]

print(len(data_109))

# plt.bar([.8,1.8,2.8,3.8,4.8,5.8,6.8],data_109, width=.2)
# plt.bar([1,2,3,4,5,6,7],data_110, width=.2)
# plt.bar([1.1,2.1,3.1,4.1,5.1,6.1,7.1],data_111, width=.2, align='edge')

w = .3
plt.bar([i-w for i in range(1, len(label) + 1)],data_109, width=w)
plt.bar([i for i in range(1, len(label) + 1)],data_110, width=w)
plt.bar([i+w/2 for i in range(1, len(label) + 1)],data_111, width=w, align='edge')

plt.xticks(range(1,len(label) + 1),label)

plt.show()