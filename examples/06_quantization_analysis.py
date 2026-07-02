#importamos librerias necesarias
import numpy as np
import matplotlib.pyplot as plt

from src.signals import generate_time_vector, generate_sine_wave

#definimos los parametros de la señal
duration = 1
f = 5
A = 1.0
sample_rate = 1000

#generamos la señal y el vector tiempo 
t = generate_time_vector(duration, sample_rate)
original_signal = generate_sine_wave(A,f,t)

#creamos la funcion para cuantizar la señal
def quantize_signal (signal, bits):
    levels = 2**bits
    quantized = np.round((signal + 1) / 2 * (levels - 1))
    quantized = (quantized / (levels - 1)) * 2 - 1
    return quantized

#llamamos la función y realizamos las graficas
k = 23 #para guardar con numeración en orden
l = 26
quantized_bits=[3,8,16]
for i in quantized_bits:
    quantized_bit = quantize_signal(original_signal, bits=i)
    plt.figure(figsize = (10,4))
    plt.plot(t, original_signal, label="Original signal")
    plt.plot(t, quantized_bit, label="Quantized signal")
    plt.legend()
    plt.title(f"{i}-bit Quantization of a 5 Hz Sine Wave")
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.savefig(f"results/images/{k}_quantization_{i}bit.png", dpi = 300)
    k += 1
    plt.show()
    
    error = original_signal - quantized_bit
    plt.figure(figsize = (10,4))
    plt.plot(t, error, label="Quantization_error")
    plt.legend()
    plt.title(f"Quantization Error - {i} bits")
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.savefig(f"results/images/{l}_quantization_error_{i}bit.png", dpi = 300)
    l += 1
    plt.show()

    mae = np.mean(np.abs(error))
    print(f"Mean absolute error for {i} bits:{mae}")