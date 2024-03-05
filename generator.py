import numpy as np
import time
import yaml
from decimal import Decimal, getcontext
import math

def generate_continuous_sine_wave(freq, sample_rate, sleep_time, min_value=None, max_value=None):
    """
    Continuously generates sine wave values and outputs them to stdout.

    :param freq: Frequency of the sine wave in Hertz.
    :param sample_rate: Sample rate in samples per second.
    :param sleep_time: Time to wait between taking samples in seconds.
    :param min_value: Minimum value for the sine wave (optional).
    :param max_value: Maximum value for the sine wave (optional).
    """
    getcontext().prec = 28
    t = Decimal(0)
    dt = Decimal(1) / Decimal(sample_rate)
    while True:
        y = Decimal(math.sin(float(2 * math.pi * freq * float(t))))
        if min_value is not None:
            y = max(min_value, y)
        if max_value is not None:
            y = min(max_value, y)
        print(y)
        t += dt
        time.sleep(float(sleep_time))

if __name__ == "__main__":
    with open("config.yml", "r") as config_file:
        config = yaml.safe_load(config_file)

    FREQUENCY = config.get("frequency", 20.0)
    SAMPLE_RATE = config.get("sample_rate", 100)
    SLEEP_TIME = config.get("sleep_time", 0.1)
    MIN_VALUE = config.get("min_value")
    MAX_VALUE = config.get("max_value")

    generate_continuous_sine_wave(FREQUENCY, SAMPLE_RATE, SLEEP_TIME, MIN_VALUE, MAX_VALUE)
