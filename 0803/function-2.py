# 任意參數
def foo(*args):
    print(args)


def foo2(*qqq):
    # print(qqq)
    for i in qqq:
        print(i)


# foo2('hello',123, True)

def fullname(first, last):
    print(f'{first} {last}')
# 關鍵字參數
# fullname( last='Parker',first='Peter')

# 任意關鍵字參數
def test(**kwargs):
    print(kwargs)


def test2(**asdf):
    print(asdf)

test2(first='John', last='Wick')
