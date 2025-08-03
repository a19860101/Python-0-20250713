

def foo(n):
    if n==0:
        return 0
    else:
        return n * foo(n-1) + 2

# print(foo(3))

# x = int(input())
x = 10
def q(n):
    if n==0:
        return 1
    else:
        return n * q(n-1)



r = []
for i in range(1,x+1):
    r.append(str(i))
r.reverse()
print(f'{x}!={'x'.join(r)}={q(x)}')
