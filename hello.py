#displaying subplots
import matplotlib.pyplot as plt
import numpy as np
x = np.array([0,1,2,3])
y = np.array([3, 8, 1, 10])

plt.subplot(3,1,1)
plt.plot(x, y,'r') #red line

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(3,1,2)#second plot in a row and first column
plt.plot(x,y,"b")

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(3,1,3)#second plot in a row and first column
plt.plot(x,y,"b")

plt.show()