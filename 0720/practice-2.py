
rate = 0.21
while True:
    mode = input('台幣換算日幣請按0，日幣換算台幣請按1，結束請按9:')

    if mode.isdigit():
        mode = int(mode)
    else:
        print('請輸入正確文字:')
        continue

    if mode == 9:
        print('掰')
        break

    if mode > 1:
        print('請輸入正確文字:')
        continue

    dollar = float(input('請輸入金額'))

    # if mode == '0':
    #     result = dollar / rate
    #     print(f'{dollar}台幣大約為{result:.0f}日幣')
    # else:
    #     result = dollar * rate
    #     print(f'{dollar}日幣大約為{result}台幣')
    match mode:
        case 0:
            result = dollar / rate
            print(f'{dollar}台幣大約為{result:.0f}日幣')
        case 1:
            result = dollar * rate
            print(f'{dollar}日幣大約為{result}台幣')
        case _:
            print('ERROR')

    print('---------------------------------------------------')
    print('---------------------------------------------------')
    print('---------------------------------------------------')
    print('---------------------------------------------------')
