"""
設計說明：
請撰寫一程式，輸入並建立兩組數組，各以-9999為結束點（數組中不包含-9999）
。將此兩數組合併並從小到大排序之，顯示排序前的數組和排序後的串列。

輸入輸出：
輸入說明
兩個數組，直至-9999結束輸入

輸出說明
排序前的數組
"""
# t1 = ()
# t2 = ()
# print('Create tuple1:')
#
# while True:
#     v = int(input())
#     if v == -9999:
#         break
#     t1+=(v,)
# print('Create tuple2:')
# while True:
#     v = int(input())
#     if v == -9999:
#         break
#     t2+=(v,)
#
# result = t1 + t2
# print(f'Combined tuple before sorting: {result}')
# result = list(result)
# result.sort()
# print(f'Combined list after sorting: {result}')


# t1=()
# t2=()
# print('Create tuple1:')
# while True:
#     n=int(input())
#     if n==-9999:
#         break
#     t1 += (n,)
# print('Create tuple2:')
# while True:
#     n=int(input())
#     if n==-9999:
#         break
#     t2 += (n,)
#
# print(f'Combined tuple before sorting: {t1+t2}')
# print(f'Combined list after sorting: {sorted(t1+t2)}')

t1=[]
t2=[]
print('Create tuple1:')
while True:
    n=int(input())
    if n==-9999:
        break
    t1.append(n)
print('Create tuple2:')
while True:
    n=int(input())
    if n==-9999:
        break
    t2.append(n)

r = tuple(t1+t2)

print(f'Combined tuple before sorting: {r}')

print(f'Combined list after sorting: {sorted(r)}')