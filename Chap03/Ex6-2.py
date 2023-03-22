import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

x=np.linspace(-6,6, num=100)
y=np.linspace(-6,6, num=100)

x, y = np.meshgrid(x, y)

z = np.exp(-0.5*x**2-0.5*y**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z, cmap=cm.jet)
plt.show()