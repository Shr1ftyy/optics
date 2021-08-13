import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

d = (1/600)*(10**(-3))

def error(y, L):
  r_1 = math.sqrt((y-(d/2))**2+L**2)
  r_2 = math.sqrt((y+(d/2))**2+L**2)
  phi = r_2 - r_1
  return abs( phi - (d*y/L) / (phi)) * 100

L_s = np.linspace(0.1, 2, 100)
delta_y_s = np.linspace(0.1, 2, 100)


def generate(x_s, alphas, func):
  ret = np.empty((x_s.shape[0], alphas.shape[0]))
  for i in range(len(x_s)):
    for j in range(len(alphas)):
      ret[i, j] = (func(x_s[i], alphas[j]))

  return ret


Y, X = np.meshgrid(delta_y_s, L_s)

errors = generate(delta_y_s, L_s, error)


fig = plt.figure()

ax = fig.add_subplot(111, projection='3d') 
# ax.set_zlim3d(-1,100)
# plt.rcParams['axes.titlepad'] = 40
ax.set_title('Wavelength Value Error Due to Angle Approximation – Double Slit')
ax.set_xlabel('Δy (m)')
ax.set_ylabel('L (m)')
ax.set_zlabel('Error %')
ax.plot_surface(X, Y, errors, color='y', rstride=4, cstride=4, linewidth=1, alpha=0.75, edgecolors='blue')



plt.draw()
plt.show()
