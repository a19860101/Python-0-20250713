# 生成式

drinks = ['紅茶','綠茶','奶茶','美式咖啡']
data = ['Banana', 'Zebra', 'Yellow', 'Apple']
n = [21, 16, 7, 28, 15, 12]

# result = [str(i) for i in n ]
# print(result)

even = [i for i in n if i%2 == 0]
odd = [i for i in n if i%2 == 1]
print(even)
print(odd)

tea = [i for i in drinks if i.find('茶')>-1]
print(tea)

# r = []
# for i in n:
#     r.append(str(i))
#
# print(r)

s = '紅茶'
print(s.find('q'))
print(s.index('茶'))