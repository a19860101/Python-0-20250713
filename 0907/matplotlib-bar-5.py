import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font',family='Microsoft Jhenghei')

data = pd.read_csv('./travel.csv')

print(data)
label = data.columns.tolist()[2:-1]
label.append('其他國家')

data_109 = [int(i) for i in data.iloc[1][2:-1]]
data_110 = [int(i) for i in data.iloc[2][2:-1]]
data_111 = [int(i) for i in data.iloc[3][2:-1]]

other_109 = int(data.iloc[1]['亞洲地區']) - int(data.iloc[1]['小計'])
other_110 = int(data.iloc[2]['亞洲地區']) - int(data.iloc[2]['小計'])
other_111 = int(data.iloc[3]['亞洲地區']) - int(data.iloc[3]['小計'])

data_109.append(other_109)
data_110.append(other_110)
data_111.append(other_111)

# plt.bar([.8,1.8,2.8,3.8,4.8,5.8,6.8],data_109, width=.2)
# plt.bar([1,2,3,4,5,6,7],data_110, width=.2)
# plt.bar([1.1,2.1,3.1,4.1,5.1,6.1,7.1],data_111, width=.2, align='edge')

w = .3
plt.bar([i-w for i in range(1, len(label) + 1)],data_109, width=w, color='red', label='109年')
plt.bar([i for i in range(1, len(label) + 1)],data_110, width=w, color='blue', label='110年')
plt.bar([i+w/2 for i in range(1, len(label) + 1)],data_111, width=w, align='edge', color='green', label='111年')

plt.xticks(range(1,len(label) + 1),label)

plt.title('109,110,110亞洲地區出國人數統計')
plt.xlabel('國家')
plt.ylabel('人數')

plt.legend()

plt.grid(axis='y')

plt.show()