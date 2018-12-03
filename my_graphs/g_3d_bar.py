from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x, y, z = axes3d.get_test_data()

ax1.plot_wireframe(x, y, z, rstride=5, cstride=5)

ax1.set_xlabel('X')
ax1.set_xlabel('Y')
ax1.set_xlabel('Z')

plt.show()

