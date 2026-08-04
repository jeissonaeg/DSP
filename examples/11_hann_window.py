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
frequency_resolution = sample_rate/N

#creamos la ventana Hann
hann_window = np.hanning(N)

#aplicamos la ventana a la señal
windowed_signal = signal*hann_window

#imprimimos los resultados 
print(f"Number of samples: {N} samples")
print(f"Frequency resolution: {frequency_resolution} Hz")
print(f"Hann window first value: {hann_window[0]}")
print(f"Hann window center value: {hann_window[int(N/2)]}")
print(f"Hann window last value: {hann_window[-1]}")

#graficamos la ventana 
plt.figure(figsize = (10,4))
plt.plot(t, hann_window)
plt.title("Hann Window Shape")
plt.xlabel("Time[s]")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig(f"results/images/41_hann_window_shape.png")
plt.show()

#graficamos la señal sin ventanad
plt.figure(figsize=(10,4))
plt.plot(t, signal)
plt.title("5.5 Hz Signal Without Window")
plt.xlabel("Time[s]")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig(f"results/images/42_signal_5_5hz_without_window.png")
plt.show()

#graficamos la señal con ventanad
plt.figure(figsize=(10,4))
plt.plot(t, windowed_signal)
plt.title("5.5 Hz Signal With Window")
plt.xlabel("Time[s]")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig(f"results/images/43_signal_5_5hz_with_window.png")
plt.show()

#ahora aplicamos la fft

fft_without_window = np.fft.fft (signal)
fft_with_window = np.fft.fft (windowed_signal)

frequencies = np.fft.fftfreq(N, d=1/sample_rate)
positive_frequencies = frequencies[:len(frequencies)//2]

magnitude_without_window = np.abs(fft_without_window)
magnitude_with_window = np.abs(fft_with_window)
positive_magnitude_without_window = magnitude_without_window[:len(magnitude_without_window)//2]
positive_magnitude_with_window = magnitude_with_window[:len(magnitude_with_window)//2]
normalized_magnitude_without_window = (2/N) * positive_magnitude_without_window
normalized_magnitude_with_window = (2/N) * positive_magnitude_with_window

#imprimimos los picos maximos
print(f"Peak without window: {np.argmax(normalized_magnitude_without_window)} Hz")
print(f"Peak with window: {np.argmax(normalized_magnitude_with_window)} Hz")

#ahora graficamos los espectros
plt.figure(figsize=(10,4))
plt.plot(positive_frequencies, normalized_magnitude_without_window)
plt.title("Spectral Leakage Without Window")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized Magnitude")
plt.xlim(0,20)
plt.grid()
plt.savefig(f"results/images/44_spectral_leakage_without_window.png")
plt.show()

plt.figure(figsize=(10,4))
plt.plot(positive_frequencies, normalized_magnitude_with_window)
plt.title("Spectral Leakage With Hann Window")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized Magnitude")
plt.xlim(0,20)
plt.grid()
plt.savefig(f"results/images/45_spectral_leakage_with_hann_window.png")
plt.show()

#comparamos ambas graficas
plt.figure(figsize=(10,4))
plt.plot(positive_frequencies, normalized_magnitude_without_window)
plt.plot(positive_frequencies, normalized_magnitude_with_window)
plt.title("Windowing Effect on Spectral Leakage")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized Magnitude")
plt.xlim(0,20)
plt.grid()
plt.legend()
plt.savefig(f"results/images/46_windowing_comparison.png")
plt.show()