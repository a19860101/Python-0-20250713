drinks = ['紅茶','綠茶','奶茶','美式咖啡']
foods = ['滷肉飯','鹹酥雞']

# len()
# print(len(drinks))

# append() 加入資料
# drinks.append('拿鐵')
# drinks.append(foods)
# print(drinks)

# extend() 擴充資料
# drinks.extend(foods)
# print(drinks)

# insert() 插入資料
# drinks.insert(2,'拿鐵')
# print(drinks)

# remove() 移除資料
# drinks.remove('美式咖啡')
# print(drinks)

# pop() 移除最後一筆資料
# drinks.pop()
# drinks.pop()
# print(drinks)

# del 移除資料
# del drinks[1]
# del drinks[1:]
# del drinks[:4]
# del drinks[1:3]
# print(drinks)

# clear() 清空資料
# drinks.clear()
# print(drinks)

# sort() 排序
data = ['Banana', 'Zebra', 'Yellow', 'Apple']
# print(data)
# data.sort()
# print(data)
# data.sort(reverse=True)
# print(data)

# reverse() 反轉
data.reverse()
print(data)

n = [21, 16, 7, 28, 15, 12]
even = []
odd = []
for i in n:
    if i % 2 == 0:
        even.append(i)
print(even)

for i in n:
    if i % 2 == 1:
        odd.append(i)

print(odd)