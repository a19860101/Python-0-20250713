import pandas as pd

result = pd.read_json('./youbike_immediate.json')

# sarea 行政區
# available_rent_bikes 可借數量
# ar 地址
# sna 站點名稱
print(result.shape)

condition = (result['sarea'] == '中正區') & (result['available_rent_bikes'] >= 10)

print(result[condition])

mydata = result[condition]

mydata = mydata[['sna','ar','available_rent_bikes']]
mydata.columns = ['站點名稱', '地址' , '可借數量']

mydata.to_excel('ubike.xlsx')