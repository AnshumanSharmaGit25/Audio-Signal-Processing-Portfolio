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
- **Tuple Unpacking**: Extracting multiple return values using `x, fs = wavread(file)`
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


## Technical Stack
* **Languages:** Python
* **Libraries:** `NumPy`, `Matplotlib`
* **Focus:** Audio Acoustics, Electroacoustics, Signal Processing

## About the Developer
B.Tech Electronics & Communication Engineering student bridging audio production and embedded DSP systems.
