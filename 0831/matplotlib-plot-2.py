import matplotlib.pyplot as plt

dataX = [10,20,30,40,50]
dataY = [20,25,60,10,40]

plt.plot(dataX, dataY,
         color='#fa0',
         linewidth=3,
         linestyle='-',
         marker='o',
         markersize='15',
         markerfacecolor='red',
         markeredgecolor='blue',
         markeredgewidth='10'
         )

plt.show()
