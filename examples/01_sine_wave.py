#importamos las librerias necesarias para el ejemplo
import numpy as np 
import matplotlib.pyplot as plt 

#definimos la señal
A = 1
f = 5
t_signal = 1
sample_rate = 1000
p = 0

#vector de tiempo
t = np.linspace(0, t_signal, int(sample_rate*t_signal), endpoint=False)

#la señal
signal = A*np.sin(2*np.pi*f*t + p)

#graficamos la señal

plt.figure(figsize=(10, 4))
plt.plot(t, signal)
plt.title("5 Hz Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("results/images/01_sine_wave.png", dpi=300)
plt.show()