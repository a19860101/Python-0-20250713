n = int(input())

def foo(n):
    if n==0 :
        return 0
    elif n==1:
        return 1
    else:
        return foo(n-1)+foo(n-2)


for i in range(n):
    print(foo(i),end=' ')