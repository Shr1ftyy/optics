import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

d = (1/600)*(10**(-3))

# value of mu is hardcoded for now
def error(delta_y, L):
  # return (mu)*(alpha**2) - 2*(alpha)*(x**2) -2*(mu)*(x**2) + 4*(x**2)
  return 100*(abs(d*math.sin(math.atan(delta_y/L)) - ((d*delta_y)/L)))/abs(d*math.sin(math.atan(delta_y/L)))

L_s = np.linspace(5, 110.0, 100)
# 0<x<(alpha/2)
delta_y_s = np.linspace(5, 110.0, 100)


def generate(x_s, alphas, func):
  ret = np.empty((x_s.shape[0], alphas.shape[0]))
  for i in range(len(x_s)):
    for j in range(len(alphas)):
      ret[i, j] = (func(x_s[i], alphas[j]))

  return ret


Y, X = np.meshgrid(delta_y_s, L_s)
# Values for volume 
errors = generate(delta_y_s, L_s, error)
# Values for derivative of volume 

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d') 
ax.set_zlim3d(-10,110)
# ax.set_title('Error')
ax.set_xlabel('Δy (m)')
ax.set_ylabel('L (m)')
ax.set_zlabel('Error %')
ax.plot_surface(X, Y, errors, color='y', rstride=4, cstride=4, linewidth=1, alpha=0.75, edgecolors='blue')


# ax = fig.add_subplot(121, projection='3d') 
# ax.set_title('Derivative of Volume Function')
# ax.set_xlabel('x')
# ax.set_ylabel('α')
# ax.set_zlabel("error'(x)")
# ax.plot_surface(X, Y, errors, color='b')

plt.draw()
plt.show()
