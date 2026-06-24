#Audio signal lab

This repository is a personal DSP learning laboratory focused on audio signal processing, signal generation, visualization, and algorithm validation. 

##Current progress

###01 - Sin Wave Generation 

In this firt experiment, a 5 Hz sin wave was generated using Python, Numpy and Matplotlib

The signal is defined as:

```text
x(t) = A · sin(2πft + φ)
=======
# DSP
A simple lab for learning and experimenting with digital signal processing (DSP).

### 02 - Basic Signal Generation

In this experiment, different basic digital signals were generated and visualized using Python, NumPy, SciPy, and Matplotlib.

The generated signals were:

- Square wave
- Triangle wave
- White noise
- Composite signal

## Square wave

A square wave alternates abruptly between high and low amplitude levels.

![5 Hz Square Wave](results/images/02_square_wave.png)

## Triangle wave

A triangle wave increases and decreases linearly over time.

![5 Hz Triangle Wave](results/images/03_triangle_wave.png)

## White noise

White noise is a random signal with no clear periodic pattern in the time domain.

![White Noise](results/images/04_white_noise.png)

## Composite signal

The composite signal was created by adding two sine waves:

```text
composite_signal = sine_5hz + sine_20hz