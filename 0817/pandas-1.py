import pandas as pd

# data = pd.Series(['A','B','C','D','E'])
# print(data)

# data = pd.DataFrame(
#     [
#         ['85','68','46'],
#         ['85','68','46'],
#         ['85','68','46'],
#         ['85','68','46'],
#         ['85','68','46'],
#         ['85','68','46'],
#     ],
#     columns=['John','Mary', 'Ken']
# )


data = pd.DataFrame(
    [
        {
            'name':'John',
            'score': [98,80]
        },{
            'name': 'Mary',
            'score': [100,75]
        }
    ]
)
print(data)