# 2. 設計說明：
# 請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和。
#
# 提示：J、Q、K以及A分別代表11、12、13以及1。
#
# 3. 輸入輸出：
# 輸入說明
# 5張牌數
#
# 輸出說明
# 5張牌的數值總和

r=0
for i in range(5):
    a=input()
    if a=='J':
        r+=11
    elif a=='Q':
        r+=12
    elif a=='K':
        r+=13
    elif a=='A':
        r+=1
    else:
        r+=int(a)
print(r)


r=[]
for i in range(5):
    a=input()
    if a=='J':
        r.append(11)
    elif a=='Q':
        r.append(12)
    elif a=='K':
        r.append(13)
    elif a=='A':
        r.append(1)
    else:
        r.append(a)
print(sum(r))
