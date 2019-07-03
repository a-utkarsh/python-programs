import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-11,11,0.1)
y = np.sin(x)


plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y)

plt.show()