# 元組 tuple
# 有序=有索引
# 不可改變
t1 = (123,567,'asdf',True)
t2 = ()
t3 = ('123',)
print(t1)
print(t1[1])
print(t1[1:3])
print(t2)
print(type(t3))

# 若tuple中只有一筆資料，需要在後方加上逗號，否則會視為字串或是數字

# t1 = list(t1)
# t1.append('qqq')
# t1 = tuple(t1)
print(t1)

print(t1+t2)

# l1 = ['a','b']
# l2 = [123,456]

# print(l1 + l2)

