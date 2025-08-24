import pandas as pd
import json

with open('./restaurant_C_f.json','r',encoding='utf-8-sig') as f:
    data = json.load(f)

result = pd.DataFrame(data['XML_Head']['Infos']['Info'])
print(result)