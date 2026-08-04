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

#creamos los diferentes tipos de ventanas
rectangular_window = np.ones(N)
hann_window = np.hanning(N)
hamming_window = np.hamming(N)
blackman_window = np.blackman(N)

#imprimimos los resultados 
print(f"Number of samples: {N} samples")
print(f"Frequency resolution: {frequency_resolution} Hz")
print(f"Rectangular first/center/last: {rectangular_window[0]}, {rectangular_window[int(N/2)]}, {rectangular_window[-1]}")
print(f"Hann first/center/last: {hann_window[0]}, {hann_window[int(N/2)]}, {hann_window[-1]} ")
print(f"Hamming first/center/last: {hamming_window[0]}, {hamming_window[int(N/2)]}, {hamming_window[-1]}")
print(f"Blackman first/center/last: {blackman_window[0]}, {blackman_window[int(N/2)]}, {blackman_window[-1]}")

#graficamos las ventana 
plt.figure(figsize = (10,4))
plt.plot(t, rectangular_window)
plt.plot(t, hann_window)
plt.plot(t, hamming_window)
plt.plot(t,blackman_window)
plt.title("Window Functions Comparison")
plt.xlabel("Time[s]")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig(f"results/images/47_window_functions_comparison.png")
plt.show()

#aplicamos las ventanas a las señales
signal_rectangular = rectangular_window * signal
signal_hann = hann_window * signal
signal_hamming = hamming_window * signal
signal_blackman = blackman_window * signal

#graficamos y comparamos la señal con diferentes ventanas
plt.figure(figsize=(10,4))
plt.plot(t, signal_rectangular)
plt.plot(t, signal_hann)
plt.plot(t, signal_hamming)
plt.plot(t, signal_blackman)
plt.title("5.5 Hz Signal With Different Windows")
plt.xlabel("Time[s]")
plt.ylabel("Amplitude")
plt.grid()
plt.savefig(f"results/images/48_windowed_signals_comparison.png")
plt.show()

#ahora aplicamos la fft
fft_signal_rectangular = np.fft.fft (signal_rectangular)
fft_signal_hann = np.fft.fft (signal_hann)
fft_signal_hamming = np.fft.fft (signal_hamming)
fft_signal_blackman = np.fft.fft (signal_blackman)

frequencies = np.fft.fftfreq(N, d=1/sample_rate)
positive_frequencies = frequencies[:len(frequencies)//2]

magnitude_signal_rectangular = np.abs(fft_signal_rectangular)
magnitude_signal_hann = np.abs(fft_signal_hann)
magnitude_signal_hamming = np.abs(fft_signal_hamming)
magnitude_signal_blackman = np.abs(fft_signal_blackman)

positive_magnitude_signal_rectangular = magnitude_signal_rectangular[:len(magnitude_signal_rectangular)//2]
positive_magnitude_signal_hann = magnitude_signal_hann[:len(magnitude_signal_hann)//2]
positive_magnitude_signal_hamming = magnitude_signal_hamming[:len(magnitude_signal_hamming)//2]
positive_magnitude_signal_blackman = magnitude_signal_blackman[:len(magnitude_signal_blackman)//2]

normalized_magnitude_signal_rectangular = (2/N) * positive_magnitude_signal_rectangular
normalized_magnitude_signal_hann = (2/N) * positive_magnitude_signal_hann
normalized_magnitude_signal_hamming = (2/N) * positive_magnitude_signal_hamming
normalized_magnitude_signal_blackman = (2/N) * positive_magnitude_signal_blackman

#imprimimos los picos maximos
print(f"Peak Rectangular: {np.argmax(normalized_magnitude_signal_rectangular)} Hz")
print(f"Peak Hann:: {np.argmax(normalized_magnitude_signal_hann)} Hz")
print(f"Peak Hamming: {np.argmax(normalized_magnitude_signal_hamming)} Hz")
print(f"Peak Blackman: {np.argmax(normalized_magnitude_signal_blackman)} Hz")

#ahora graficamos los espectros
plt.figure(figsize=(10,4))
plt.plot(positive_frequencies, normalized_magnitude_signal_rectangular)
plt.title("Rectangular spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized Magnitude")
plt.xlim(0,20)
plt.grid()
plt.savefig(f"results/images/49_rectangular_window_spectrum.png")
plt.show()

plt.figure(figsize=(10,4))
plt.plot(positive_frequencies, normalized_magnitude_signal_hann)
plt.title("Hann spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized Magnitude")
plt.xlim(0,20)
plt.grid()
plt.savefig(f"results/images/50_hann_window_spectrum.png")
plt.show()

plt.figure(figsize=(10,4))
plt.plot(positive_frequencies, normalized_magnitude_signal_hamming)
plt.title("Hamming spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized Magnitude")
plt.xlim(0,20)
plt.grid()
plt.savefig(f"results/images/51_hamming_window_spectrum.png")
plt.show()

plt.figure(figsize=(10,4))
plt.plot(positive_frequencies, normalized_magnitude_signal_blackman)
plt.title("Blackman spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized Magnitude")
plt.xlim(0,20)
plt.grid()
plt.savefig(f"results/images/52_blackman_window_spectrum.png")
plt.show()

plt.figure(figsize=(10,4))
plt.plot(positive_frequencies, normalized_magnitude_signal_rectangular, label = "Rectangular")
plt.plot(positive_frequencies, normalized_magnitude_signal_hann, label = "Hann")
plt.plot(positive_frequencies, normalized_magnitude_signal_hamming, label = "Hamming")
plt.plot(positive_frequencies, normalized_magnitude_signal_blackman, label = "Blackman")
plt.title("Window Spectrum Comparison")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Normalized Magnitude")
plt.xlim(0,20)
plt.grid()
plt.legend()
plt.savefig(f"results/images/53_window_spectrum_comparison.png")
plt.show()