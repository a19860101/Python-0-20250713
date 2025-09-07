a = int(input())
b = int(input())
c = input()

if c == '+':print(a + b)
elif c == '-': print(a - b)
elif c == '*':print(a * b)
elif c == '/':print(a / b)
elif c == '//':print(a // b)
elif c == '%':print(a % b)


#

a=int(input());b=int(input());c=input().strip()
print(eval(f"{a}{c}{b}") if c in {'+','-','*','/','//','%'} else 'error')

# a=int(input());b=int(input());c=input().strip()
# print(eval(f"{a}{c}{b}"))

a=int(input());b=int(input());c=input().strip();print({'+':lambda x,y:x+y,'-':lambda x,y:x-y,'*':lambda x,y:x*y,'/':lambda x,y:x/y,'//':lambda x,y:x//y,'%':lambda x,y:x%y}.get(c,lambda x,y:'error')(a,b))