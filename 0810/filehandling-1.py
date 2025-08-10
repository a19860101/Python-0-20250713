# file = open('hello.txt','r',encoding='utf-8')
# # big5
#
# print(file.read())
#
# print(file.closed)
# file.close()
# print(file.closed)


with open('hello.txt','r',encoding='utf-8') as file:
    print(file.read())

print(file.closed)