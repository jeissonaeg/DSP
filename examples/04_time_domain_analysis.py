#importamos las librerias necesarias
import matplotlib.pyplot as plt
import numpy as np
from src.signals import generate_time_vector, generate_sine_wave

#definimos los parametros de la señal
duration = 1
sample_rate = 1000
f = 5
A = 1.0
phase = 0

#calculamos los parámetros de la señal
period = 1 / f
samples_per_cycle = sample_rate / f

#imprimimos los parámetros de la señal
print(f"Period of the signal: {period} seconds")
print(f"Samples per cycle: {samples_per_cycle} samples")

#generamos el vector de tiempo y la señal
t = generate_time_vector(duration, sample_rate)
sine_wave = generate_sine_wave(A, f, t, phase)
sine_wave_amplitude_1 = generate_sine_wave(A, f, t, phase)
sine_wave_amplitude_2 = generate_sine_wave(2, f, t, phase)
sine_frequency_5hz = generate_sine_wave(A, f, t, phase)
sine_frequency_10hz = generate_sine_wave(A, 10, t, phase)
sine_phase_0 = generate_sine_wave(A, f, t, phase)
sine_phase_pi_over_2 = generate_sine_wave(A, f, t, np.pi/2)

#graficamos las señales
plt.figure(figsize=(10,4))
plt.plot(t, sine_wave)
plt.axvline(period)
plt.title("Time Domain Analysis - Period of a 5 Hz Sine Wave")
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/11_time_domain_period_analysis.png", dpi=300)
plt.show()

plt.figure(figsize=(10,4))
plt.plot(t, sine_wave_amplitude_1)
plt.axvline(period)
plt.title("Sine Wave with Amplitude 1.0")
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/12_sine_amplitude_1.png", dpi=300)
plt.show()

plt.figure(figsize=(10,4))
plt.plot(t, sine_wave_amplitude_2)
plt.axvline(period)
plt.title("Sine Wave with Amplitude 2.0")
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/13_sine_amplitude_2.png", dpi=300)
plt.show()

plt.figure(figsize=(10,4))
plt.plot(t, sine_frequency_5hz)
plt.axvline(period)
plt.title("Sine Wave with Frequency 5 Hz")
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/14_sine_frequency_5hz.png", dpi=300)
plt.show()

plt.figure(figsize=(10,4))
plt.plot(t, sine_frequency_10hz)
plt.axvline(period)
plt.title("Sine Wave with Frequency 10 Hz")
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/15_sine_frequency_10hz.png", dpi=300)
plt.show()

plt.figure(figsize=(10,4))
plt.plot(t, sine_phase_0)
plt.axvline(period)
plt.title("Sine Wave with Phase 0")
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/16_sine_phase_0.png", dpi=300)
plt.show()

plt.figure(figsize=(10,4))
plt.plot(t, sine_phase_pi_over_2)
plt.axvline(period)
plt.title("Sine Wave with Phase pi/2")
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("results/images/17_sine_phase_pi_over_2.png", dpi=300)
plt.show()