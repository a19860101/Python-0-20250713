# 請撰寫一程式，將使用者輸入的三個整數
# （代表一元二次方程式  的三個係數a、b、c）
# 作為參數傳遞給一個名為compute()的函式，
# 該函式回傳方程式的解，如無解則輸出【Your equation has no root.】
#
# 提示：
# 輸出有順序性，請先輸出包含正平方根的解，再輸出包含負平方根的解
# 回傳方程式的解，無須考慮小數點位數
#
# 3. 輸入輸出：
# 輸入說明
# 三個整數，分別為a、b、c
#
# 輸出說明
# 代入一元二次方程式，回傳方程式解；如無解則輸出【Your equation has no root.】



























a = int(input())
b = int(input())
c = int(input())

def compute(a, b, c):
    q = b ** 2 - 4 * a * c

    if q < 0:
        print('Your equation has no root.')
    elif q == 0:
        print(-b / 2 * a)
    else:
        a1 = (-b + (q ** 0.5))/(2*a)
        a2 = (-b - (q ** 0.5))/(2*a)

        print(f'{a1}, {a2}')

compute(a, b, c)