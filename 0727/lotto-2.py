import random

result = random.sample(range(1,50),6)

# list to str

result_txt = ','.join(str(i) for i in result)

print(f'您的大樂投選號結果為{result_txt}，特別號為{result[-1]}')