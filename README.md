# Audio signal lab

This repository is a personal DSP learning laboratory focused on audio signal processing, signal generation, visualization, and algorithm validation. 

## Current progress

### 01 - Sin Wave Generation 

In this firt experiment, a 5 Hz sin wave was generated using Python, Numpy and Matplotlib

The signal is defined as:

```text
x(t) = A · sin(2πft + φ)
```

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
```

### 03 - Reusable Signal Generation Functions

In this experiment, the signal generation code was reorganized into reusable Python functions.

Instead of writing the mathematical formulas directly inside each example script, the main signal generation logic was moved into:

```text
src/signals.py
```

This improves the project structure and makes the code easier to reuse, test, maintain, and extend.

## Implemented functions

The following functions were created:

```text
generate_time_vector()
generate_sine_wave()
generate_square_wave()
generate_triangle_wave()
generate_white_noise()
```

## Why this matters

In digital signal processing projects, it is important to separate the algorithm implementation from the example or application code.

This allows the same DSP functions to be reused in different experiments without duplicating code.

## Generated signals using functions

### Sine wave

A sine wave was generated using the reusable `generate_sine_wave()` function.

![Sine Wave from Function](results/images/06_sine_from_function.png)

### Square wave

A square wave was generated using the reusable `generate_square_wave()` function.

![Square Wave from Function](results/images/07_square_from_function.png)

### Triangle wave

A triangle wave was generated using the reusable `generate_triangle_wave()` function.

![Triangle Wave from Function](results/images/08_triangle_from_function.png)

### White noise

White noise was generated using the reusable `generate_white_noise()` function.

![White Noise from Function](results/images/09_white_noise_from_function.png)

### Composite signal

A composite signal was created by adding two sine waves generated from the reusable function:

```text
composite_wave = sine_5hz + sine_20hz
```

Where:

* `sine_5hz` has amplitude 1.0.
* `sine_20hz` has amplitude 0.5.

![Composite Signal from Functions](results/images/10_composite_from_function.png)

## What I learned

* Reusable functions make DSP code cleaner and easier to maintain.
* Signal generation formulas should be separated from plotting and example scripts.
* A signal processing project should have a clear structure.
* Functions allow the same algorithm to be reused with different parameters.
* Modular code is closer to how real engineering projects are organized.

### 04 - Time Domain Analysis

In this experiment, sine waves were analyzed in the time domain.

The goal was to understand how frequency, period, amplitude, sampling rate, samples per cycle, and phase affect a digital signal.

## Period and Frequency

The period is the duration of one complete cycle of a periodic signal.

```text
T = 1 / f
```

For a 5 Hz sine wave:

```text
T = 1 / 5 = 0.2 seconds
```

This means that each cycle lasts 0.2 seconds.

## Samples per Cycle

The number of samples per cycle depends on the sampling rate and the signal frequency.

```text
samples_per_cycle = sample_rate / frequency
```

For a 5 Hz signal sampled at 1000 Hz:

```text
samples_per_cycle = 1000 / 5 = 200 samples
```

This means that each cycle is represented by 200 samples.

## Amplitude Comparison

Changing the amplitude modifies the height of the signal, but it does not change the frequency or the number of cycles.

* Amplitude 1.0
* Amplitude 2.0

## Frequency Comparison

Changing the frequency modifies how many cycles occur in one second.

* Frequency 5 Hz
* Frequency 10 Hz

A 5 Hz sine wave has a period of 0.2 seconds, while a 10 Hz sine wave has a period of 0.1 seconds.

## Phase Comparison

Changing the phase shifts the signal horizontally in time.

* Phase 0
* Phase π/2

A sine wave with phase π/2 looks like a cosine wave because:

```text
sin(x + π/2) = cos(x)
```

## What I Learned

* The period is the time duration of one complete cycle.
* Frequency and period are inversely related.
* The sampling rate defines how many samples are taken per second.
* Samples per cycle depend on both sampling rate and signal frequency.
* Increasing amplitude changes the signal height, not the number of cycles.
* Increasing frequency increases the number of cycles in the same time interval.
* Changing phase shifts the signal horizontally.
* Time-domain analysis helps describe how a digital signal behaves before moving to frequency-domain analysis.

### 05 - Sampling Analysis

In this experiment, a 5 Hz sine wave was sampled using different sampling rates.

The goal was to understand how the sampling rate affects the digital representation of a signal.

## Sampling Period

The sampling period is the time between two consecutive samples.

```text
Ts = 1 / sample_rate
```

For a sampling rate of 1000 Hz:

```text
Ts = 1 / 1000 = 0.001 seconds
```

This means that one sample is taken every 1 millisecond.

## Samples per Cycle

The number of samples per cycle depends on the signal frequency and the sampling rate.

```text
samples_per_cycle = sample_rate / frequency
```

For a 5 Hz signal:

| Sampling Rate | Samples per Cycle |
| ------------- | ----------------: |
| 1000 Hz       |               200 |
| 100 Hz        |                20 |
| 50 Hz         |                10 |
| 20 Hz         |                 4 |
| 8 Hz          |               1.6 |

## Sampling Comparison

As the sampling rate decreases, the signal is represented with fewer samples.

* 1000 Hz sampling rate
* 100 Hz sampling rate
* 50 Hz sampling rate
* 20 Hz sampling rate
* 8 Hz sampling rate

## Aliasing

Aliasing occurs when the sampling rate is too low to correctly represent the original signal.

According to the Nyquist criterion:

```text
sample_rate > 2 × signal_frequency
```

For a 5 Hz signal:

```text
sample_rate > 2 × 5 = 10 Hz
```

When the signal was sampled at 8 Hz, the sampling rate was below the Nyquist limit. As a result, the sampled signal appeared distorted and looked like a lower-frequency signal.

In this case, the apparent alias frequency is approximately:

```text
alias ≈ |8 Hz - 5 Hz| = 3 Hz
```

## What I Learned

* The sampling rate defines how many samples are taken per second.
* The sampling period defines the time between consecutive samples.
* Lower sampling rates produce fewer samples per cycle.
* A signal can look less smooth when it is represented with fewer samples.
* The plotted line is only a visual connection between discrete samples.
* Aliasing occurs when the sampling rate is below the Nyquist limit.
* Aliasing can make a signal appear as a false lower frequency.
* Anti-aliasing filters are important before real ADC sampling.

### 06 - Quantization Analysis

In this experiment, a 5 Hz sine wave was quantized using different bit depths.

The goal was to understand how bit resolution affects the amplitude representation of a digital signal.

## Quantization

Quantization is the process of mapping continuous amplitude values into a finite number of discrete levels.

The number of quantization levels depends on the number of bits:

```text
levels = 2^bits
```

Examples:

| Bits    | Quantization Levels |
| ------- | ------------------: |
| 3 bits  |                   8 |
| 8 bits  |                 256 |
| 16 bits |               65536 |

## 3-bit Quantization

With 3 bits, the signal can only be represented using 8 amplitude levels.

This produces visible stair-step behavior.

## 8-bit Quantization

With 8 bits, the signal has 256 possible amplitude levels, so it looks much closer to the original signal.

## 16-bit Quantization

With 16 bits, the signal has 65536 possible amplitude levels, making the quantized signal almost identical to the original signal visually.

## Quantization Error

The quantization error is the difference between the original signal and the quantized signal.

```text
quantization_error = original_signal - quantized_signal
```

* Quantization error - 3 bits
* Quantization error - 8 bits
* Quantization error - 16 bits

## Mean Absolute Error

The mean absolute error was calculated to numerically compare the quantization error.

```text
mean_absolute_error = mean(abs(original_signal - quantized_signal))
```

Results:

| Bits    | Mean Absolute Error |
| ------- | ------------------: |
| 3 bits  |          0.06381867 |
| 8 bits  |          0.00203790 |
| 16 bits |          0.00000758 |

## What I Learned

* Quantization converts continuous amplitude values into discrete levels.
* The number of available levels depends on the bit depth.
* Low bit depth produces visible stair-step distortion.
* Higher bit depth reduces the quantization error.
* Quantization error can be measured numerically.
* Increasing bit depth improves amplitude precision.
* In audio systems, quantization error can appear as noise or low-level distortion.
