a = [123, 'hello', True, 3.12]
# a = list([123,345,678])

# 取得串列內資料
# list[start:end:step]

# print(a[0])
# print(a[-2])
# print(a[2:3])
# print(a[:4])
# print(a[1:])
# print(a[::2])

# 顯示迴圈所有資料
# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])

# for i in enumerate(a):
#     print(i[0],i[1])

# unpack
for idx,i in enumerate(a):
    print(idx,i)

# str to list
s = 'hello,python'
# print(s.split(','))
# print(list(s))

# list to str

result = '____'.join(str(s) for s in a)
print(result)