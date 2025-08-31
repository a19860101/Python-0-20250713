import matplotlib.pyplot as plt
import pandas as pd

datas = pd.read_csv('./travel.csv',header=1)

print(datas)
# print(datas['亞洲地區'])
# print(datas.iloc[2]['蒙古'])
# print(datas['Asia'])
# print(datas.iloc[1]['Mongolia'])
print(datas.columns)
# travel_data = datas.iloc[2][2:-1].tolist()
labels = ['日本','韓國','北韓','中國(含香港澳門)','蒙古','其他國家']
other = datas.iloc[2]['Asia'] - datas.iloc[2]['Total']
china = datas.iloc[2]['Hong Kong'] + datas.iloc[2]['China'] + datas.iloc[2]['Macao']
travel_data = [
    datas.iloc[2]['Japan'],
    datas.iloc[2]['Korea'],
    datas.iloc[2]['DPRK'],
    datas.iloc[2]['Hong Kong'] + datas.iloc[2]['China'] + datas.iloc[2]['Macao'],
    datas.iloc[2]['Mongolia'],
    datas.iloc[2]['Asia'] - datas.iloc[2]['Total']
]

print(travel_data)
#
# travel_data.append(other)
#
print(travel_data)
plt.rc('font',family='Microsoft Jhenghei')
plt.pie(travel_data,autopct='%.2f%%',labels=labels,explode=[0.1,0,0,0,0,0])
plt.title('111年亞洲區出國比例')
plt.show()
