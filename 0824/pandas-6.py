import pandas as pd

result = pd.read_csv('restaurant_C_f.csv')
# result = pd.read_json('./restaurant_C_f.json')
# print(result)

# 計算Region欄位空值的數量
# print(result['Region'].isnull().sum())
# 印出Region欄位為空的資料
# print(result[result['Region'].isnull()])

# data_region = result[result['Region'].isnull()]
# print(data_region['Name'])
# print(data_region['Add'])

# result['Region'] = result['Region'].fillna('0')
# result = result.dropna(subset=['Region'])
# condition = result['Region'].str.contains('新北')
# print(result[condition])

print(result.shape)
r = result.dropna(axis=1)
print(r.shape)
r2 = result.dropna(axis=0,subset=['Region'])
print(r2.shape)

# condition = result['Region'].str.contains('新北',na=False)
# print(result[condition])

# mydata = result[condition]
# print(mydata)

# mydata = mydata[['Name','Add','Opentime']]
# mydata.columns = ['名稱','地址','營業時間']

# mydata.to_excel('restaurant.xlsx')
# print(mydata)