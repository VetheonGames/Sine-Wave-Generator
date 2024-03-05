import numpy as np
import time
import yaml

def generate_continuous_sine_wave(freq, sample_rate):
    """
    Continuously generates sine wave values and outputs them to the terminal.

    :param freq: Frequency of the sine wave in Hertz.
    :param sample_rate: Sample rate in samples per second.
    """
    t = 0
    dt = 1 / sample_rate
    while True:
        y = np.sin(2 * np.pi * freq * t)
        print(y)
        t += dt
        time.sleep(dt)

if __name__ == "__main__":
    # Load parameters from config.yml
    with open("config.yml", "r") as config_file:
        config = yaml.safe_load(config_file)

    # Extract parameters or use default values
    FREQUENCY = config.get("frequency", 1)  # Hz
    SAMPLE_RATE = config.get("sample_rate", 100)  # Samples per second

    generate_continuous_sine_wave(FREQUENCY, SAMPLE_RATE)
