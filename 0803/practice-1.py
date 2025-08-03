def currency_converter(dollar ,mode, rate=0.201):
    if mode == '0':
        result = dollar / rate
        print(f'{dollar}台幣大約為{result:.0f}日幣')
    else:
        result = dollar * rate
        print(f'{dollar}日幣大約為{result}台幣')

m = input('台幣換算日幣請按0，日幣換算台幣請按1:')
d = float(input('請輸入金額'))
r = float(input('請輸入匯率'))
currency_converter(d ,m)

def currency_converter_2():
    mode = input('台幣換算日幣請按0，日幣換算台幣請按1:')

    dollar = float(input('請輸入金額'))

    rate = 0.201

    if mode == '0':
        result = dollar / rate
        print(f'{dollar}台幣大約為{result:.0f}日幣')
    else:
        result = dollar * rate
        print(f'{dollar}日幣大約為{result}台幣')

# currency_converter_2()