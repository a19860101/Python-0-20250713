import pandas as pd

data = pd.read_json('./TransService.json')

# condition = data['shelter_address'].str.contains('臺北|新北')
# print(data[condition])

# condition = data['animal_Variety'].str.contains('混種狗|混種犬')
#
# condition = (data['shelter_address'].str.contains('新竹市') &
#              (data['animal_kind'].str.contains('狗') == False)
#              )

condition = data['animal_kind'].str.contains('狗|貓') == False

my_data = data[condition]

my_data = my_data[['shelter_address','shelter_name','animal_Variety','animal_remark']]

# print(my_data.columns)
my_data.columns = ['收容所','收容所地址','品種','註記']
my_data.to_excel('dog.xlsx')
print(my_data)