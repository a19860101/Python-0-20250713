d = {
    'name': 'John',
    'mail': 'asdf@gmail.com',
    'gender': 'Male',
    'n': 123
}

# print(d)
# print(d['name'])
# print(d['mail'])
# print(d['gender'])

products = [
    {
        'name': 'iPhone16',
        'price': ['29900','33400','40400'],
        'size': ['128GB','256GB','512GB'],
        'color': ['湛海藍色','湖水綠色','粉紅色','白色','黑色']
    },
    {
        'name': 'iPhone16 Plus',
        'price': ['32900','36400','43400'],
        'size': ['128GB','256GB','512GB'],
        'color': ['湛海藍色','湖水綠色','粉紅色','白色','黑色']
    },
    {
        'name': 'iPhone16 Pro',
        'price': ['36900','40400','47400','54400'],
        'size': ['128GB','256GB','512GB','1TB'],
        'color': ['沙漠色鈦金屬','原色鈦金屬','白色鈦金屬','黑色鈦金屬']
    },{
        'name': 'iPhone16 Pro Max',
        'price': ['44900','51900','58900'],
        'size': ['256GB','512GB','1TB'],
        'color': ['沙漠色鈦金屬','原色鈦金屬','白色鈦金屬','黑色鈦金屬']
    }
]

# print(products[0]['price'])
# print(products[0]['color'][0])

# print(products[0]['name'])
# print(products[1]['name'])
# print(products[2]['name'])
# print(products[3]['name'])

for product in products:
    print(product['name'])
    print(product['color'])
