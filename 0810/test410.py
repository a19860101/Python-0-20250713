n = int(input())
# for i in range(n):
    # print('*'* (2*i+1))
    # print('-' * (n-i-1))
    # print(' ' * (n-i-1)+'*'* (2*i+1))


for i in range(n,0,-1):
    print(' '*(i-1) + '*'*(2*(n-i)+1))