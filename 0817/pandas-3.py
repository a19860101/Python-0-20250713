import pandas as pd

users = [
    {'name': 'Zac', 'age': 32, 'gender': 'M'},
    {'name': 'Max', 'age': 28, 'gender': 'M'},
    {'name': 'Andy', 'age': 30, 'gender': 'M'},
    {'name': 'Amy', 'age': 22, 'gender': 'F'},
    {'name': 'Laura', 'age': 26, 'gender': 'F'}
]
data = pd.DataFrame(users)

# condition = data['age'] > 25
# print(data[condition])
# print(data[data['age'] > 25])
# print(data[data['gender'] == 'M'])
# print(data[data['name'] == 'Laura'])
# print(data[data['age'] > 50])

# print(data[data['name'].str.contains('A|a')])

condition = (data['name'].str.contains('An'))
print(data[condition])
