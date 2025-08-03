def foo():
    print('Hello Function')

# 引數
def greeting(name):
    print(f'Hello {name}')

def foo2(a,b,c):
    print(a*b*c)

def tw_us(dollar, rate=30):
    # print(dollar / rate)
    return dollar / rate

def hello():
    # print('hello')
    return 'hello'

print(tw_us(10000))
