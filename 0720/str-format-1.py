# 格式化字串 %

name = 'John'
# print('hello %s' % name)
# print('您是第%i位訪客' % 123)
# print('您是第%f位訪客' % 123)
# print('您是第%s位訪客' % 123)

# print('%10s' % 'hello')
# print('%10s' % '哈囉')
# print('%-10s' % '哈囉')
# print('%+10s' % '哈囉')

print('%10d' % 123)
print('%-10i' % 123)
print('%10f' % 123)
print('%10.1f' % 123)
print('%10.3f' % 3.1415926)

print('hello %s你好，今天氣溫為%.2f度' % ('John', 39.4865))

# i => int
# d => decimal 10進位

# %x 10 -> 16

print('%x' % 255)

"""
%i,%d 10進位（儘量使用%d）
%f 浮點數
%s 字串
%x 10進位轉16進位
"""