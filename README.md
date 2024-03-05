# Sine Wave Generator
### (Continuous Sine Wave Generator)

## Introduction

The Sine Wave Generator is a versatile tool designed to produce continuous sine waves with customizable parameters. This README provides an overview of its features, usage, and configuration options.

## Features

   - Continuous Generation: The generator produces sine wave values continuously, allowing for real-time data generation.
   - Configurability: Users can specify parameters such as frequency, sample rate, and amplitude range to customize the generated sine wave.
   - Flexible Output: The generator outputs sine wave values to standard output (stdout), making it compatible with various data processing pipelines and applications.

## Usage

To use the Sine Wave Generator, follow these steps:

   - Clone or download the repository to your local machine.
   - Ensure you have Python installed (version `3.6` or higher).
   - Ensure depends are installed (`NumPy`, `PyYaml`)
   - Run the `generator.py` script with the desired parameters set in `config.yml`.

## Example usage:

```bash
python generator.py
```

## Configuration

The generator can be configured using a YAML file named config.yml. This file allows users to specify parameters such as:

   - Frequency: The frequency of the sine wave in Hertz (Hz).
   - Sample Rate: The sample rate in samples per second (Hz).
   - Amplitude Range: The minimum and maximum values for the sine wave amplitude.

## Example config.yml file:

```yaml
frequency: 20.0  # Frequency of the sine wave in Hz
sample_rate: 100  # Sample rate in samples per second
min_value: -1.0  # Minimum value for the sine wave amplitude
max_value: 1.0   # Maximum value for the sine wave amplitude
```

## Dependencies

The Sine Wave Generator has the following dependencies:

   - Python (version 3.6 or higher)
   - numpy
   - yaml

## License

This project is licensed under the GPLv2 License - see the [LICENSE](LICENSE) file for details.
Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Authors

   - Connor Crawford (VetheonGames)