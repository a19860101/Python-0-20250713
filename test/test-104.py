# 請撰寫一程式，輸入一圓的半徑，並加以計算此圓之面積和周長，
# 最後請印出此圓的半徑（Radius）、周長（Perimeter）和面積（Area）。
#
# 提示1：需import math模組，並使用math.pi。
# 提示2：輸出浮點數到小數點後第二位。

# ans

import math
r = float(input())

p = 2*math.pi*r

a = math.pi*r**2

print(f'Radius = {r:.2f}')
print(f'Perimeter = {p:.2f}')
print(f'Area = {a:.2f}')
