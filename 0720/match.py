import datetime

# print(datetime.date.today())
# print(datetime.datetime.today())
# print(datetime.date.today().weekday())
# print(datetime.date.today().isoweekday())
s = datetime.date.today().isoweekday()

match s:
    case 7:
        print('日')
    case 1:
        print('月')
    case 2:
        print('火')
    case 3:
        print('水')
    case 4:
        print('木')
    case 5:
        print('金')
    case 6:
        print('土')
    case _:
        print('ERROR')