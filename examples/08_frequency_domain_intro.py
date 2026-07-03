#importamos las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt

from src.signals import generate_time_vector, generate_sine_wave

#parametros
duration = 1
sample_rate = 1000
A = 1.0

#frecuencias
frequency_1 = 5
frequency_2 = 20

#vector de tiempo
t = generate_time_vector(duration, sample_rate)

#generamos las señales
sine_5hz = generate_sine_wave(A, frequency_1, t)
sine_20hz = generate_sine_wave(A, frequency_2, t)

#generamos la señal compuesta
composite_signal = sine_5hz + 0.5 * sine_20hz

#graficamos la señal
plt.figure(figsize=(10, 4))
plt.plot(t, composite_signal)
plt.title("Composite Signal in Time Domain")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("results/images/32_composite_signal_time_domain.png", dpi=300)
plt.show()

#pasamos al dominio de la frecuencia 
fft_result = np.fft.fft(composite_signal)
frequencies = np.fft.fftfreq(len(composite_signal), d=1/sample_rate)

magnitude = np.abs(fft_result)

positive_frequencies = frequencies[:len(frequencies)//2]
positive_magnitude = magnitude[:len(magnitude)//2]
normalized_magnitude = (2 / len(composite_signal)) * positive_magnitude

#graficamos la señal
plt.figure(figsize=(10, 4))
plt.plot(positive_frequencies, positive_magnitude)
plt.title("Composite Signal Frequency Spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid(True)
plt.xlim(0, 50)
plt.savefig("results/images/33_composite_signal_frequency_spectrum.png", dpi=300)
plt.show()

threshold = 1e-6

significant_indices = np.where(positive_magnitude > threshold)[0]

top_indices = significant_indices[np.argsort(positive_magnitude[significant_indices])[-5:]]

top_indices = top_indices[::-1]

print("Top frequency components:")
for index in top_indices:
    freq = positive_frequencies[index]
    mag = positive_magnitude[index]
    print(f"Frequency: {freq:.2f} Hz, Magnitude: {mag:.2f}")

plt.figure(figsize=(10, 4))
plt.plot(positive_frequencies, normalized_magnitude)
plt.title("Normalized Composite Signal Frequency Spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized Magnitude")
plt.grid(True)
plt.xlim(0, 50)
plt.savefig("results/images/34_normalized_composite_signal_frequency_spectrum.png", dpi=300)
plt.show()

threshold = 1e-6

significant_indices = np.where(normalized_magnitude > threshold)[0]

top_indices = significant_indices[np.argsort(normalized_magnitude[significant_indices])[-5:]]

top_indices = top_indices[::-1]

print("Top normalized frequency components:")
for index in top_indices:
    freq = positive_frequencies[index]
    mag = normalized_magnitude[index]
    print(f"Frequency: {freq:.2f} Hz, Normalized Magnitude: {mag:.2f}")