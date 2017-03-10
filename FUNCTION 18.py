#Function 18



from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np



fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.arange(-2, 2, 0.01)
Y = np.arange(-2, 2, 0.01)
X, Y = np.meshgrid(X, Y)
hasil1 = []
hasil2 = []
for i in range(1,6):
	hasil1.append(i * np.cos((i + 1) * X + 1))
	hasil2.append(i * np.cos((i + 1) * Y + 1))
Z = (-1) * (sum(hasil1) * sum(hasil2))
surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_stern,
                       linewidth=0, antialiased=False)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()