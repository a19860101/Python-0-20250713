# 格式化字串 format

# print('hello {}'.format('John'))
# print('hello {}你好，今天氣溫為{}度'.format(30,'John'))
# print('hello {1}你好，今天氣溫為{0}度'.format(30,'John'))
#
print('hello {name:^10s}你好，今天氣溫為{temp:.1f}度'.format(name='John',temp=32))

# print('hello {:s}你好，今天氣溫為{:d}度'.format('john',32))
# print('{:10s}'.format('hello'))
# print('{:>10s}'.format('hello'))
# print('{:->10s}'.format('hello'))
# print('{:<10s}'.format('hello'))
# print('{:*<10s}'.format('hello'))
# print('{:^10s}'.format('hello'))
# print('{:0^10s}'.format('hello'))
# print('{:/^10d}'.format(12345))
# print('{:_<10.2f}'.format(12))
# print('{:*^10s}'.format('12'))

print('{:*<3.1s}'.format('王大明'))
print('{:010d}'.format(2))

r = 3
g = 255
b = 3
print('#{:02x}{:02x}{:02x}'.format(r,g,b))