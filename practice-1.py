# nt = float(input('請輸入台幣金額:'))
# print(nt / 0.1998)

nt = input('請輸入台幣金額:')

result = float(nt) / 0.1998
# result = int(result)
# 四捨五入 round()
result = round(result, 2)

print(result)

# input得到的資料型別為字串str()

print(int(2.4)) # 2
print(int(2.5)) # 2