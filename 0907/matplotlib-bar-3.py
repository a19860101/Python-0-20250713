import matplotlib.pyplot as plt

plt.rc('font',family='Microsoft Jhenghei')

x = ['taiwan','japan','hongkong','usa']
y = [50,20,40,30]

label = ['台灣','日本','香港','美國']

# plt.bar(x,y,tick_label=label)
plt.bar(x,y)

# plt.xticks(x, label)
plt.xticks(range(4), label)

plt.show()