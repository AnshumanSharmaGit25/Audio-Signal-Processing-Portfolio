# Audio Signal Processing & DSP Portfolio

This repository tracks my hands-on implementation of digital signal processing (DSP) concepts, focusing on electroacoustics, signal analysis, and algorithmic audio filtering in Python.

## Automated Progress Log


### `Ex1.ipynb`

# Exercise 1: Python and sounds

## Summary

This exercise introduces fundamental audio signal processing concepts in Python. You'll learn how to read WAV files, perform basic audio operations, work with NumPy array indexing, and understand the effects of downsampling on audio signals.

The exercise consists of four practical parts:
1. Reading audio files and extracting sample slices
2. Finding minimum and maximum amplitude values
3. Mastering Python array indexing with the hop operation
4. Implementing downsampling and observing its effects on different signals

## Skills Learned

### Core Concepts
- **Audio File I/O**: Reading WAV files using the `wavread()` function from sms-tools
- **Audio Normalization**: Understanding why floating-point values in [-1, 1] are preferred over raw 16-bit integers
- **Sampling Rate**: Grasping the relationship between sampling rate (Hz) and time

### Python Fundamentals
- **Array Slicing**: Using NumPy slicing syntax `x[start:stop]` to extract contiguous subarrays
- **Tuple Unpacking**: Extracting multiple return values using `fs, x = wavread(file)`
- **NumPy Operations**: Using NumPy functions like `min()`, `max()`, and array indexing
- **List Comprehension & Indexing**: Extracting every Mth element efficiently

### Signal Processing
- **Downsampling**: Reducing the sampling rate by a factor M and observing aliasing effects
- **Nyquist Theorem**: Understanding the maximum representable frequency after downsampling
- **Aliasing**: Observing how high-frequency components fold back into lower frequencies when undersampled
- **Anti-aliasing**: Conceptually understanding why filtering before downsampling is necessary

### Practical Skills
- Working with Jupyter notebooks for interactive audio exploration
- Plotting waveforms with time-axis labels
- Playing audio directly from NumPy arrays
- Comparing audio quality degradation across different signal types

## Key Takeaways

By completing this exercise, you understand:
- How digital audio is represented and manipulated in Python
- The critical importance of sampling rate in audio processing
- How improper downsampling introduces artifacts (aliasing)
- The mathematical relationship between sampling rate, Nyquist frequency, and representable harmonics

---

### `Ex2.ipynb`

# Exercise 2: Sinusoids and the DFT

## Summary

This exercise develops an understanding of sinusoidal signals and the Discrete Fourier Transform (DFT). It covers generating real and complex sinusoids, implementing the DFT and inverse DFT from their mathematical definitions, and computing the magnitude spectrum of a discrete-time signal.

The implementations use NumPy and are validated against expected numerical results and NumPy's built-in FFT functions.

## Topics Covered

- Discrete-time real sinusoids
- Complex sinusoids
- Amplitude, frequency, phase, and sampling rate
- Sampling theorem and Nyquist frequency
- Aliasing
- Angular frequency and phase increments
- Euler's complex exponential
- Discrete Fourier Transform
- Inverse Discrete Fourier Transform
- Frequency bins
- DC component
- Magnitude spectrum
- Positive and negative frequency components
- Spectral symmetry
- Spectral leakage
- Floating-point numerical precision
- Signal reconstruction

## Skills Learned

- Generate sampled real sinusoids with NumPy.
- Generate complex exponentials for specific DFT frequency bins.
- Implement the DFT using the definition:

  $$
  X[k] = \sum_{n=0}^{N-1} x[n]e^{-j2\pi kn/N}
  $$

- Implement the IDFT using the definition:

  $$
  x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k]e^{j2\pi kn/N}
  $$

- Compute the magnitude spectrum using the absolute value of a complex spectrum.
- Plot the real and imaginary parts of signals and spectra.
- Identify the DC component in a DFT output.
- Convert DFT bin indices into physical frequencies.
- Compare a custom DFT implementation with `np.fft.fft()`.
- Validate signal reconstruction using `idft(dft(x))`.
- Measure reconstruction accuracy using maximum absolute error.
- Interpret small floating-point residuals in numerical computations.
- Explain why real signals produce symmetric positive- and negative-frequency peaks.
- Recognize spectral leakage when a sinusoid does not align with a DFT bin.
- Understand how changing signal amplitude affects spectral magnitude.

## Implemented Functions

- `gen_sine(A, f, phi, fs, t)`  
  Generates a real-valued sinusoid.

- `gen_complex_sine(k, N)`  
  Generates a complex sinusoid for a selected DFT frequency bin.

- `dft(x)`  
  Computes the discrete Fourier transform of a sequence.

- `idft(X)`  
  Computes the inverse discrete Fourier transform.

- `gen_mag_spec(x)`  
  Computes the magnitude spectrum of a sequence.

## Key Takeaways

- The sampling rate must be greater than twice the signal frequency to avoid aliasing.
- The phase parameter shifts a sinusoid in time.
- A complex sinusoid rotates around the unit circle with a phase increment of $(2\pi k/N)$.
- The DFT measures how strongly each discrete frequency component is present in a signal.
- The zero-frequency bin represents the DC component.
- The IDFT reconstructs the original signal using a $(1/N)$ scaling factor.
- Real-valued signals have conjugate-symmetric DFT spectra.
- A sinusoid aligned with a DFT bin produces concentrated spectral peaks.
- A sinusoid between DFT bins produces spectral leakage across neighboring bins.
- Very small imaginary or real-valued residuals are usually caused by floating-point precision.

## Technologies Used

- Python
- NumPy
- Matplotlib
- IPython Audio

<!-- EXERCISE-2-SUMMARY:END -->

---


## Technical Stack
* **Languages:** Python
* **Libraries:** `NumPy`, `Matplotlib`
* **Focus:** Audio Acoustics, Electroacoustics, Signal Processing

## About the Developer
B.Tech Electronics & Communication Engineering student bridging audio production and embedded DSP systems.
