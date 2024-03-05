import numpy as np
import time

def generate_continuous_sine_wave(freq, sample_rate):
    """
    Continuously generates sine wave values and outputs them to the terminal.

    :param freq: Frequency of the sine wave in Hertz.
    :param sample_rate: Sample rate in samples per second.
    """
    t = 0
    dt = 20.0 / sample_rate
    while True:
        y = np.sin(2 * np.pi * freq * t)
        print(y)
        t += dt
        time.sleep(dt)

if __name__ == "__main__":
    FREQUENCY = 1  # Hz
    SAMPLE_RATE = 100  # Samples per second
    generate_continuous_sine_wave(FREQUENCY, SAMPLE_RATE)
