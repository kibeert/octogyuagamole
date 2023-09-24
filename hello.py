import matplotlib.pyplot as plt
import numpy as np

y = np.array([0, 50, 100, 150,200])
mylabels = ["Apples", "Bananas", "Cherries", "Dates", "Oranges"]
myexplode = [0.2, 0, 0, 0,0]
plt.pie(y,labels= mylabels,  explode=myexplode)
plt.show()