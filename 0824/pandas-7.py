import pandas as pd
import json

with open('./restaurant_C_f.json','r',encoding='utf-8-sig') as f:
    data = json.load(f)
    # result = pd.DataFrame(json.load(f)['XML_Head']['Infos']['Info'])
# print(data['XML_Head']['Infos']['Info'])
result = pd.DataFrame(data['XML_Head']['Infos']['Info'])
print(result)

condition = result['Region'].str.contains('高雄', na=False)

print(result[condition])