#importamos las librerias necesarias
import matplotlib.pyplot as plt
from src.signals import generate_time_vector, generate_sine_wave

#parametros de la señal
duration = 1
f = 5
A = 1.0
sample_rates = [1000, 100, 50, 20, 8]

#definimos las señales con un ciclo for 
k = 18 #para guardar con numeración en orden
for i in sample_rates:
    t = generate_time_vector(duration, i)
    signal = generate_sine_wave(A, f, t)
    samples_per_cycle = i / f
    plt.figure(figsize = (10,4))
    plt.plot(t, signal, marker="o")
    plt.title(f"5 Hz Sine Wave Sampled at {i} Hz")
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.savefig(f"results/images/{k}_sampling_{i}hz.png", dpi = 300)
    k += 1
    plt.show()