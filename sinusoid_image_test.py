# Links:
# https://stackoverflow.com/questions/57534808/generate-an-image-of-a-sloped-sinewave
# https://www.youtube.com/watch?v=xhO8iz2qCOE&t=694s

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

N = 256
freq = 8.0
ampt = 127.0
phase = 0.0
vec = 1

def create_image(N, freq, ampt, phase, vec):
    x = np.linspace(-np.pi, np.pi, N)

    sine1D = N / 2.0 + (ampt * np.sin((x * freq) + phase))
    sine1D = np.uint8(sine1D)

    sine2D = np.ndarray((N, N), dtype=np.uint8)
    for i in range(N):
        sine2D[i] = np.roll(sine1D, -i)  # shift the 1D sin data by -i, -i increases with rows
    return sine2D


sine2D = create_image(N, freq, ampt, phase, vec)
fig, ax = plt.subplots()
im = plt.imshow(sine2D, cmap='gray')

fig.subplots_adjust(bottom=0.2) # or whatever

axamp = plt.axes([0.25, 0.1, 0.50, 0.02])
slider_freq = Slider(axamp, 'Frequency', 0, 30, valinit=freq)
axamp = plt.axes([0.25, 0.07, 0.50, 0.02])
slider_ampt = Slider(axamp, 'Amptitude', 0, ampt, valinit=ampt)
axamp = plt.axes([0.25, 0.04, 0.50, 0.02])
slider_phase = Slider(axamp, 'Phase', 0, 360, valinit=phase)
axamp = plt.axes([0.25, 0.01, 0.50, 0.02])
slider_vector = Slider(axamp, 'Vector', 0, 10, valinit=phase)


def slider_freq_onchange(val):
    freq = val
    sine2D = create_image(N, freq, ampt, phase, vec)
    im.set_array(sine2D)

def slider_ampt_onchange(val):
    ampt = val
    sine2D = create_image(N, freq, ampt, phase, vec)
    im.set_array(sine2D)

def slider_phase_onchange(val):
    phase = val
    sine2D = create_image(N, freq, ampt, phase, vec)
    im.set_array(sine2D)

def slider_vector_onchange(val):
    vec = int(val)
    sine2D = create_image(N, freq, ampt, phase, vec)
    im.set_array(sine2D)

slider_freq.on_changed(slider_freq_onchange)
slider_ampt.on_changed(slider_ampt_onchange)
slider_phase.on_changed(slider_phase_onchange)
slider_vector.on_changed(slider_vector_onchange)

plt.show()




