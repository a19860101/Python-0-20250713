s1 = {'apple', 'Banana', 'Cat'}

# 新增
# add
# s1.add('Dog')
# print(s1)

# 移除（找不到報錯）
# remove() 抱錯
# s1.remove('qqq')
# print(s1)

# 移除（找不到不報錯，顯示原來集合）
# discard()
# s1.discard('qqq')
# print(s1)

# 清空
# clear()
# s1.clear()
# print(s1)

a = {'apple', 'Banana', 'Cat'}
b = {'Dog', 'Eagle', 'Cat'}

# 聯集
print(a.union(b))
print(a | b)

# 交集
print(a.intersection(b))
print(a & b)

# 差集
print(a.difference(b))
print(a - b)
print(b.difference(a))
print(b - a)

# 對稱差集
print(a.symmetric_difference(b))
print(a ^ b)

x = {1,2,3,0}
y = {3,4,5,0}
z = {4,5,6,0}

print(x|y|z)
print(x.union(y).union(z))
print(x & y & z)