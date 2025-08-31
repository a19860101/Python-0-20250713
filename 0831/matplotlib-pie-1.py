import matplotlib.pyplot as plt

data = [12,32,15,35]

# plt.pie(data)

plt.pie(data,
        radius=1,
        labels=['A','B','C','D'],
        colors=['red','green','blue','pink'],
        labeldistance=1.2,
        startangle=15,
        explode=[.2,0,0,0],
        counterclock=False,
        shadow=True,
        autopct='%.2f%%',
        textprops={
                'color':'white',
                'weight': 'bold'
            },
        wedgeprops={
                'linewidth':5,
                'linestyle':':',
                'edgecolor': 'red'
            }
        )

plt.show()