a = '10'

# if a > 0:
# #     print('ok')
try:
    if a > 0:
        print('ok')
# except Exception as e:
#     print(e)
except NameError as ne:
    print('NameError',ne)
except TypeError as te:
    print('TypeError',te)
