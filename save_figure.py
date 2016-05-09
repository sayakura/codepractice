import matplotlib.pylab as plt
import numpy as np
x = np.arange(-15, 15)
y = np.cos(x)
pic = plt.figure()
plt.scatter(x, y)
plt.show()