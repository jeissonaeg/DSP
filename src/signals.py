#importamos librerias necesarias
import numpy as np 
from scipy.signal import sawtooth

#definimos la función para generar el vector de tiempo
def generate_time_vector(duration, sample_rate):
    """
    Genera un vector de tiempo para una señal.

    Args:
        duration (float): Duración de la señal en segundos.
        sample_rate (int): Frecuencia de muestreo en Hz.

    Returns:
        np.ndarray: Vector de tiempo.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return t

#definimos la función para generar una señal senoidal
def generate_sine_wave(A, f, t, p=0.0):
    """
    Genera una señal senoidal.

    Args:
        A (float): Amplitud de la señal.
        f (float): Frecuencia de la señal en Hz.
        t (np.ndarray): Vector de tiempo.
        p (float, optional): Fase de la señal en radianes. Por defecto es 0.

    Returns:
        np.ndarray: Señal senoidal.
    """
    signal = A * np.sin(2 * np.pi * f * t + p)
    return signal

#definimos la función para generar una señal cuadrada
def generate_square_wave(f, t, A=1.0):
    """
    Genera una señal cuadrada.

    Args:
        A (float): Amplitud de la señal.
        f (float): Frecuencia de la señal en Hz.
        t (np.ndarray): Vector de tiempo.

    Returns:
        np.ndarray: Señal cuadrada.
    """
    signal = A * np.sign(np.sin(2 * np.pi * f * t))
    return signal

def generate_triangle_wave(f, t, A=1.0):
    """
    Genera una señal triangular.

    Args:
        A (float): Amplitud de la señal.
        f (float): Frecuencia de la señal en Hz.
        t (np.ndarray): Vector de tiempo.

    Returns:
        np.ndarray: Señal triangular.
    """
    signal = A * sawtooth(2 * np.pi * f * t, 0.5)
    return signal

def generate_white_noise(A, t):
    """
    Genera una señal de ruido blanco.

    Args:
        A (float): Amplitud máxima del ruido.
        t (np.ndarray): Vector de tiempo.

    Returns:
        np.ndarray: Señal de ruido blanco.
    """
    signal = np.random.uniform(-A, A, t)
    return signal