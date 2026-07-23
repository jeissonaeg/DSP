#importamos librerias necesarias
import numpy as np
import matplotlib.pyplot as plt

from src.signals import generate_time_vector, generate_sine_wave

#definimos los parametros de la señal
duration = [1.0, 0.5, 2.0]
A = 1.0
sample_rate = 1000
f = 5

k = 35 #para tener continuidad en las graficas
for d in duration:
    #generamos el vector tiempo
    t = generate_time_vector(d, sample_rate)

    #generamos la señal seno
    signal = generate_sine_wave(A, f, t, p=0.0)

    #calculamos el numero de muestras
    N = len(signal)

    #calculamos la resolucion espectral
    frequency_resolution = sample_rate/N

    #imprimimos los parametros calculados
    print(f"Duration: {d} s")
    print(f"Number of samples: {N}")
    print(f"Frequency_resolution: {frequency_resolution} Hz")

    #pasamos al dominio de la frecuencia
    fft_result = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(len(signal), d=1/sample_rate)

    magnitude = np.abs(fft_result)
    positive_frequencies = frequencies[:len(frequencies)//2]
    positive_magnitude = magnitude[:len(magnitude)//2]
    normalized_magnitude = (2 / len(signal)) * positive_magnitude

    #graficamos la señal
    plt.figure(figsize=(10, 4))
    plt.plot(positive_frequencies, positive_magnitude)
    plt.title(f"Frequency Spectrum - Duration {d} s")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.xlim(0, 50)
    plt.savefig(f"results/images/{k}_frequency_bins_{d}s.png", dpi=300)
    plt.show()

    k += 1

