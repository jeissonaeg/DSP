#importamos las librerías necesarias
import matplotlib.pyplot as plt
from src.signals import generate_time_vector, generate_sine_wave, generate_square_wave, generate_triangle_wave, generate_white_noise

#definimos los parametros 
A = 1.0
f = 5
duration = 1
sample_rate = 1000

#generamos el vector de tiempo y las señales utilizando las funciones definidas en src/signals.py
t = generate_time_vector(duration, sample_rate)
sine_signal = generate_sine_wave(A, f, t)
square_signal = generate_square_wave(f, t, A)
triangle_signal = generate_triangle_wave(f, t, A)
white_noise_signal = generate_white_noise(A, len(t))
composite_signal = generate_sine_wave(1, 5, t) + generate_sine_wave(0.5, 20, t)

#graficamos la señal senoidal
plt.figure(figsize=(10,4))
plt.plot(t, sine_signal)
plt.title('5 Hz Sine Wave Generated from Function')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/06_sine_wave_function.png", dpi=300)
plt.show()

#graficamos la señal cuadrada
plt.figure(figsize=(10,4))
plt.plot(t, square_signal)
plt.title('5 Hz Square Wave Generated from Function')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/07_square_wave_function.png", dpi=300)
plt.show()

#graficamos la señal triangular
plt.figure(figsize=(10,4))  
plt.plot(t, triangle_signal)
plt.title('5 Hz Triangle Wave Generated from Function')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/08_triangle_wave_function.png", dpi=300)
plt.show()

#graficamos la señal de ruido blanco
plt.figure(figsize=(10,4))
plt.plot(t, white_noise_signal)
plt.title('White Noise Signal Generated from Function')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/09_white_noise_function.png", dpi=300)
plt.show()

#graficamos la señal compuesta
plt.figure(figsize=(10,4))  
plt.plot(t, composite_signal)
plt.title('Composite Signal (5 Hz + 20 Hz) Generated from Function')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/10_composite_signal_function.png", dpi=300)
plt.show()