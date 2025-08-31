import matplotlib.pyplot as plt
import pandas as pd

datas = pd.read_json('./TransService.json')

# print(datas['animal_kind'])
# print(datas['animal_kind'].value_counts())
# print(datas['animal_Variety'].value_counts(ascending=True))

animal_kind = datas['animal_kind'].value_counts()

# print(datas['shelter_name'].nunique())
# print(datas['animal_kind'].nunique())


# plt.pie(animal_kind, autopct='%.1f%%')

# plt.show()

mydata = datas[datas['shelter_address'].str.contains('臺北|新北')]
print(mydata['shelter_address'].nunique())
print(mydata['shelter_address'].value_counts())

