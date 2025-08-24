import pandas as pd

result = pd.read_csv('restaurant_C_f.csv')
# result = pd.read_json('./restaurant_C_f.json')

# print(result)


condition = result['Region'].str.contains('新北')
print(result[condition])

# mydata = result[condition]
# print(mydata)

# mydata = mydata[['Name','Add','Opentime']]
# mydata.columns = ['名稱','地址','營業時間']

# mydata.to_excel('restaurant.xlsx')
# print(mydata)