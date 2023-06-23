from matplotlib import pyplot as plt
#plt.style.use('fivethirtyeight')
plt.style.use('ggplot')
dev_x = [25,26,27,28,29,30,31,32,33,34]
dev_y = [3897,4430,2332,345,2345,2345,1346,3457,3456,6780]
dev_z = [234,213,345,356,346,789,545,675,456,678]
plt.plot(dev_x,dev_y,'k--',label='all devs')
plt.plot(dev_x,dev_z,'b--',label='python')
plt.bar(dev_x,dev_y)

plt.xlabel('Ages')
plt.ylabel('Salary per year')
plt.title('Median salary USD')
plt.legend()
plt.grid(True)
plt.savefig('plot.png')
plt.show()

