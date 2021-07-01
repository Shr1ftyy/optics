import numpy as np
import math
import matplotlib.pyplot as plt

b = 0.025e-3 # slit width
S = 0.05e-3 # distance between slits
w = 6.5e-7 # Wavelength of incident light
i = 1
L = 1.32

alpha = lambda x: (math.pi * S * math.sin(x))/w
beta = lambda x: (math.pi * b * math.sin(x))/w

I_s = lambda theta: i * (((math.sin(beta(theta)))**2/(beta(theta)**2)))
I_d = lambda theta: i * (((math.cos(alpha(theta)))**2) * ((math.sin(beta(theta)))**2)/(beta(theta))**2 )

fig, axs = plt.subplots(3, 1)

angles = np.linspace(-0.1, 0.1, 1000) # Angles (in radians)
xs = [L*math.atan(x) for x in angles] # Displacement of rays on screen from origin - takes the Length between the slit and screen into account
h = 150 # height of diffraction pattern output image
single_slit = np.array([I_s(x) for x in xs])
double_slit = np.array([I_d(x) for x in xs])

s_pattern = np.concatenate(h*(np.expand_dims(np.array([I_s(angle) for angle in angles]), 0), ), axis=0)
print(np.shape(s_pattern))
d_pattern = np.concatenate(h*(np.expand_dims(np.array([I_d(angle) for angle in angles]), 0), ), axis=0)

axs[0].plot(xs, single_slit, color = 'red', label = f'Intensity')
axs[0].plot(xs, double_slit, color = 'blue', label = f'Intensity')
plt.setp(axs[0], ylabel='Intensity')
plt.setp(axs[0], xlabel='Displacement from Origin')
axs[1].imshow(s_pattern, cmap=plt.cm.get_cmap('Greys').reversed() , label='Single Slit')
axs[2].imshow(d_pattern, cmap=plt.cm.get_cmap('Greys').reversed(), label='Double Slit')
plt.show()
