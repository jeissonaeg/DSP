#importamos librerias necesarias
import numpy as np
import matplotlib.pyplot as plt

from src.signals import generate_time_vector, generate_sine_wave

#definimos los parametros de las señales
duration = 1
A = 1.0
sample_rate = 1000

#generamos las señales
t = generate_time_vector(duration, sample_rate)
sine_5hz = generate_sine_wave(A,5,t)
sine_20hz = generate_sine_wave(0.5,20,t)
composite_signal = sine_5hz + sine_20hz

#graficamos la señal
plt.figure(figsize=(10,4))  
plt.plot(t, composite_signal)
plt.title('Week 01 Review - Composite Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/29_week_01_composite_signal.png", dpi=300)
plt.show()

#generamos la señal con un sample_rate inferior
sample_rate_low = 30

#generamos las señales
t_low = generate_time_vector(duration, sample_rate_low)
sine_5hz = generate_sine_wave(A,5,t_low)
sine_20hz = generate_sine_wave(0.5,20,t_low)
composite_signal_low = sine_5hz + sine_20hz

#graficamos la señal
plt.figure(figsize=(10,4))  
plt.plot(t_low, composite_signal_low)
plt.title('Week 01 Review - Low Sampling Rate')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/30_week_01_low_sampling_rate.png", dpi=300)
plt.show()

def quantize_signal (signal, bits):
    levels = 2**bits
    quantized = np.round((signal + 1) / 2 * (levels - 1))
    quantized = (quantized / (levels - 1)) * 2 - 1
    return quantized

quantized_bit = quantize_signal(composite_signal, bits=4)
plt.figure(figsize = (10,4))
plt.plot(t, quantized_bit)
plt.title("Week 01 Review - 4-bit Quantization")
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/31_week_01_4bit_quantization.png", dpi = 300)
plt.show()