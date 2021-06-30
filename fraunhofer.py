import numpy as np
import math
import matplotlib.pyplot as plt

b = 0.025e-3 # slit width
S = 0.05e-3 # distance between slits
w = 4.5e-7 # Wavelength of incident light
i = 1
L = 1.32

alpha = lambda x: (math.pi * S * math.sin(x))/w
beta = lambda x: (math.pi * b * math.sin(x))/w

I_s = lambda theta: i * (((math.sin(beta(theta)))**2/(beta(theta)**2)))
I_d = lambda theta: i * (((math.cos(alpha(theta)))**2) * ((math.sin(beta(theta)))**2)/(beta(theta))**2 )

fig, axs = plt.subplots(3, 1)

xs = np.linspace(-0.1,0.1,1000)
h = 150 # height of diffraction pattern output image
single_slit = np.array([I_s(x) for x in xs])
double_slit = np.array([I_d(x) for x in xs])

s_pattern = np.concatenate(h*(np.expand_dims(np.array([I_s(x) for x in xs]), 0), ), axis=0)
print(np.shape(s_pattern))
d_pattern = np.concatenate(h*(np.expand_dims(np.array([I_d(x) for x in xs]), 0), ), axis=0)

axs[0].plot(xs, single_slit, color = 'red', label = f'Intensity')
axs[0].plot(xs, double_slit, color = 'blue', label = f'Intensity')
axs[1].imshow(s_pattern, cmap=plt.cm.get_cmap('Greys').reversed() , label='Single Slit')
axs[2].imshow(d_pattern, cmap=plt.cm.get_cmap('Greys').reversed(), label='Double Slit')
plt.show()
