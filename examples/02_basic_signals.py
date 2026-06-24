#importamos librerias necesarias 
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth

#definimos los parametros de las señales
A = 1.0
f = 5
duration = 1
sample_rate = 1000

#vector de tiempo
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

#definimos las señales
square_signal = A * np.sign(np.sin(2 * np.pi * f * t))
triangle_signal = A * sawtooth(2 * np.pi * f * t, 0.5)
white_noise = np.random.uniform(-A,A,len(t))
sine_5Hz = np.sin(2*np.pi*5*t)
sine_20Hz = 0.5*np.sin(2*np.pi*20*t)
composite_signal = sine_5Hz + sine_20Hz


#graficamos las señales 

plt.figure(figsize=(10, 4))
plt.plot(t, square_signal)
plt.title('5 Hz square signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/02_square_wave.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(t, triangle_signal)
plt.title('5 Hz triangle signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/02_triangle_wave.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(t, white_noise)
plt.title('White noise signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/02_white_noise.png", dpi=300)
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(t, composite_signal)
plt.title('Composite signal (5 Hz + 20 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/02_composite_signal.png", dpi=300)
plt.show()
