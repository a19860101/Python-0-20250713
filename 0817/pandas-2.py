import pandas as pd

users = [
    {'name': 'Zac', 'age': '32', 'gender': 'M'},
    {'name': 'Max', 'age': '28', 'gender': 'M'},
    {'name': 'Andy', 'age': '30', 'gender': 'M'},
    {'name': 'Amy', 'age': '22', 'gender': 'F'},
    {'name': 'Laura', 'age': '26', 'gender': 'F'}
]

# data = pd.DataFrame(users,index=range(1,len(users)+1))
data = pd.DataFrame(users)

# print(data)
# print(data.index)
# print(data.columns)
# print(data.size)
# print(data.shape)
#
# print(data['name'])
# print(data['age'])

# print(data.loc[0])
# print(data.iloc[1])

# print(data.iloc[3]['gender'])
# print(data['gender'].iloc[3])



age = pd.Series([int(a) for a in data['age']])

print(age)
# print(min(age))
# print(max(age))
print(age.min()) # 最小值
print(age.max()) # 最大值
print(age.mean()) # 算術平均數
print(age.std()) # 標準差
print(age.median()) #中位數
print(age.describe())
