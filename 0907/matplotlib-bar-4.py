import matplotlib.pyplot as plt

plt.rc('font',family='Microsoft Jhenghei')

x = ['taiwan','japan','hongkong','usa']
y1 = [50,20,40,30]
y2 = [40,50,45,15]

plt.bar([1,2,3,4],y1, width=.4, align='edge')
plt.bar([.8,1.8,2.8,3.8],y2,width=.4)

plt.xticks(range(1,5), x)

plt.show()
