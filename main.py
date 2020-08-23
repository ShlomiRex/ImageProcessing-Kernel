#https://stackoverflow.com/questions/57534808/generate-an-image-of-a-sloped-sinewave

import numpy as np
import matplotlib.pyplot as plt

N = 256
x = np.linspace(-np.pi,np.pi, N)
sine1D = 128.0 + (127.0 * np.sin(x * 8.0))
sine1D = np.uint8(sine1D)
sine2D = np.ndarray((N,N), dtype=np.uint8)
for i in range(N):
    sine2D[i]= np.roll(sine1D,-i)  # shift the 1D sin data by -i, -i increases with rows
plt.imshow(sine2D, cmap='gray')
plt.show()