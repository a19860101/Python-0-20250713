# 2. 設計說明：
# 請使用迴圈敘述撰寫一程式，讓使用者輸入兩個正整數a、b（a < b）
# ，利用迴圈計算從a開始的偶數連加到b的總和。
# 例如：輸入a=1、b=100，則輸出結果為2550（2 + 4 + … + 100 = 2550）。
#
# 3. 輸入輸出：
# 輸入說明
# 兩個正整數（a、b，且a < b）
#
# 輸出說明
# 計算從a開始的偶數連加到b的總和



# 解法一
# a=int(input())
# b=int(input())
# r=0
# for i in range(a,b+1):
#     if i%2==0:
#         r += i
# print(r)

# 解法二
# a=int(input())
# b=int(input())
# r = []
# for i in range(a,b+1):
#     if i%2==0:
#         r.append(i)
# print(sum(r))

# 解法三
# print(sum([i for i in range(int(input()),int(input())+1) if i%2==0]))
