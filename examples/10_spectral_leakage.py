#importamos librerias necesarias
import numpy as np
import matplotlib.pyplot as plt

from src.signals import generate_time_vector, generate_sine_wave

#definimos las variables necesarias
sample_rate = 1000
duration = 1.0
A = 1
frequency_exact = 5
frequency_non_exact = 5.5

#generamos el vector de tiempo
t = generate_time_vector(duration, sample_rate)

#generamos las señales
signal_exact = generate_sine_wave(A, frequency_exact, t)
signal_non_exact = generate_sine_wave(A,frequency_non_exact, t)

#calculamos los parametros necesarios
N = len(signal_exact)
frequency_resolution = sample_rate / N
cycles_exact = frequency_exact * duration
cycles_non_exact = frequency_non_exact * duration

#imprimimos los parametros encontrados
print(f"Number of samples: {N}")
print(f"Frequency resolution: {frequency_resolution}")
print(f"Cycles for 5 Hz: {cycles_exact}")
print(f"Cycles for 5.5 Hz: {cycles_non_exact}")

#calculamos la magnitud de las señales 
fft_signal_exact = np.fft.fft(signal_exact)
fft_signal_non_exact = np.fft.fft(signal_non_exact)

frequencies = np.fft.fftfreq(N, d=1/sample_rate)

magnitude_signal_exact = np.abs(fft_signal_exact)
magnitude_signal_non_exact = np.abs(fft_signal_non_exact)
positive_frequencies_signal_exact = frequencies[:len(frequencies)//2]
positive_frequencies_signal_non_exact = frequencies[:len(frequencies)//2]
positive_signal_exact = magnitude_signal_exact[:len(magnitude_signal_exact)//2] 
positive_magnitude_signal_non_exact = magnitude_signal_non_exact[:len(magnitude_signal_non_exact)//2] 
normalized_signal_exact = (2 / N) * positive_signal_exact
normalized_magnitude_signal_non_exact = (2 / N) * positive_magnitude_signal_non_exact

print (f"Peak frequency for 5 Hz signal: {np.argmax(normalized_signal_exact)}")
print (f"Peak frequency for 5.5 Hz signal: {np.argmax(normalized_magnitude_signal_non_exact)}")

#graficamos las señales
plt.figure(figsize=(10,4))
plt.plot(positive_frequencies_signal_exact,normalized_signal_exact)
plt.title("Spectral Leakage - 5 Hz Exact Bin")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized Magnitude")
plt.grid(True)
plt.xlim(0,20)
plt.savefig(f"results/images/38_spectral_leakage_5hz.png", dpi=300)
plt.show()

plt.figure(figsize=(10,4))
plt.plot(positive_frequencies_signal_non_exact,normalized_magnitude_signal_non_exact)
plt.title("Spectral Leakage - 5.5 Hz Non-Exact Bin")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized Magnitude")
plt.grid(True)
plt.xlim(0,20)
plt.savefig(f"results/images/39_spectral_leakage_5_5hz.png", dpi=300)
plt.show()

plt.figure(figsize=(10,4))
plt.plot(positive_frequencies_signal_exact,normalized_signal_exact, label="signal_exact")
plt.plot(positive_frequencies_signal_non_exact,normalized_magnitude_signal_non_exact, label="signal_non_exact")
plt.title("Spectral Leakage Comparison")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized Magnitude")
plt.grid(True)
plt.xlim(0,20)
plt.savefig(f"results/images/40_spectral_leakage_comparison.png", dpi=300)
plt.show()