import matplotlib.pyplot as plt
import numpy as np

xpoints= np.array([1,2,6,8,15])
ypoints= np.array([3, 8, 1, 10, 25])
y2points= np.array([4,6,9,3,1])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.plot(xpoints, ypoints, linestyle ="solid", color= "r")
plt.plot(xpoints, y2points)
plt.xlabel("x points", fontdict=font2)
plt.ylabel("y points", fontdict=font2)
plt.title("Graph plotting", fontdict=font1)
plt.show()