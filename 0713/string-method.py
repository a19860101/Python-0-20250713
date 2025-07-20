s = 'Hello python!! hello moto hello hello ha ha ah'

# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.capitalize())

# 尋找字串內文字，找到回傳索引值，找不到回傳-1
# print(s.find('z'))
# 從右側尋找字串內文字，找到回傳索引值，找不到回傳-1
# print(s.rfind('o'))

# 尋找字串內文字，找到回傳索引值，找不到報錯
# print(s.index('z'))
# 從右側尋找字串內文字，找到回傳索引值，找不到報錯
# print(s.rindex('o'))

# 計算次數
# print(s.count('H'))
# 計算字串長度
# print(len(s))

# 取代文字
# print(s.replace('python', '哈哈'))

# 去除頭尾空白
print(' hello ')
print(' hello '.strip())
print(' hello '.lstrip())
print(' hello '.rstrip())

# split 文字轉串列
# print(s.split())
# print(s.split('h'))

# isalpha()
# print('哈囉'.isalpha())
# isdecimal()
# print('0.1010101'.isdecimal())
# isdigit()
print('12.3'.isdigit())
# isnumeric()

print('１'.isnumeric())
