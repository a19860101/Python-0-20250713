import random

# print(random.randrange(0,10))
# print(random.randint(0,10))

# 電腦選號 1 - 49  6

result = []
# result.append(random.randint(1, 49))
# while len(result) < 6:
#     n = random.randint(1, 49)
#     if n != result[-1]:
#         result.append(n)
# print(result)

while len(result) < 6:
    n = random.randint(1, 49)
    if n not in result:
        result.append(n)
print(result)