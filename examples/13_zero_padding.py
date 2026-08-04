#importamos librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
from src.signals import generate_time_vector, generate_sine_wave

#definimos los parametros
sample_rate = 1000
duration = 1.0
A = 1.0
frequency = 5.5

#generamos el vector de tiempo
t = generate_time_vector(duration, sample_rate)

#generamos la señal seno de 5.5 Hz
signal = generate_sine_wave(A, frequency, t)

#calculamos el numero de muestras y la resolucion frecuencial
N = len(signal)
n_fft_without_padding = N
n_fft_with_padding = 4096
true_frequency_resolution = 1 / duration
bin_spacing_without_padding = sample_rate / n_fft_without_padding
bin_spacing_with_padding = sample_rate / n_fft_with_padding

#imprimimos los parametros estimados
print(f"Number of real samples: {N}")
print(f"FFT size without padding: {n_fft_without_padding}")
print(f"FFT size with padding: {n_fft_with_padding}")
print(f"True frequency resolution: {true_frequency_resolution}")
print(f"Bin spacing without padding: {bin_spacing_without_padding}")
print(f"Bin spacing with padding: {bin_spacing_with_padding}")

#ahora aplicamos la fft
fft_signal_without_padding = np.fft.fft (signal, n_fft_without_padding)
fft_with_padding = np.fft.fft(signal, n_fft_with_padding)

frequencies_without_padding = np.fft.fftfreq(N, d=1/sample_rate)
positive_frequencies_without_padding = frequencies_without_padding[:len(frequencies_without_padding)//2]

frequencies_with_padding = np.fft.fftfreq(n_fft_with_padding, d=1/sample_rate)
positive_frequencies_with_padding = frequencies_with_padding[:len(frequencies_with_padding)//2]

magnitude_signal_without_padding = np.abs(fft_signal_without_padding)
magnitude_signal_with_padding = np.abs(fft_with_padding)

positive_magnitude_signal_without_padding = magnitude_signal_without_padding[:len(magnitude_signal_without_padding)//2]
positive_magnitude_signal_with_padding = magnitude_signal_with_padding[:len(magnitude_signal_with_padding)//2]

normalized_magnitude_signal_without_padding = (2/N) * positive_magnitude_signal_without_padding
normalized_magnitude_signal_with_padding = (2/N) * positive_magnitude_signal_with_padding

#imprimimos los picos maximos de cada espectro
print(f"Peak without padding: {np.argmax(normalized_magnitude_signal_without_padding)} Hz")
print(f"Peak with padding: {positive_frequencies_with_padding[np.argmax(normalized_magnitude_signal_with_padding)]} Hz")

#ahora graficamos los espectros
plt.figure(figsize=(10,4))
plt.plot(positive_frequencies_without_padding, normalized_magnitude_signal_without_padding)
plt.title("Spectrum Without Zero Padding")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized Magnitude")
plt.xlim(0,20)
plt.grid()
plt.savefig(f"results/images/54_spectrum_without_zero_padding.png")
plt.show()

plt.figure(figsize=(10,4))
plt.plot(positive_frequencies_with_padding, normalized_magnitude_signal_with_padding)
plt.title("Spectrum With Zero Padding")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized Magnitude")
plt.xlim(0,20)
plt.grid()
plt.savefig(f"results/images/55_spectrum_with_zero_padding.png")
plt.show()

plt.figure(figsize=(10,4))
plt.plot(positive_frequencies_without_padding, normalized_magnitude_signal_without_padding, label = "original signal")
plt.plot(positive_frequencies_with_padding, normalized_magnitude_signal_with_padding, label = "signal with padding")
plt.title("Zero Padding Spectrum Comparison")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized Magnitude")
plt.xlim(0,20)
plt.legend()
plt.grid()
plt.savefig(f"results/images/56_zero_padding_comparison.png")
plt.show()