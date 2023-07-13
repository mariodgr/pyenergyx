# PyEnergyX

PyEnergyX is a robust Python library aimed at professionals in the energy industry. It provides a reliable and accurate method for converting between various energy units.

## Overview

With PyEnergyX, you can conveniently convert between common units as well as less conventional ones like Tonne of Coal Equivalent, Barrel of Aviation Gasoline, BTU, tons of coal, barrels of oil, joules, and many more. 

The main source for the conversion factors used in this library is the Energy Information Administration, which ensures high accuracy and reliability of the conversions.

## Installation

To install PyEnergyX, you can use pip to install directly from the GitHub repository:

```pip install git+https://github.com/mariodgr/pyenergyx.git```

## Usage
Here's how to use PyEnergyX:

First, import the EnergyConverter class and create an instance:

```
from pyenergyx import EnergyConverter

converter = EnergyConverter()

```
You can get a list of all available energy units:

```
units = converter.get_units()
# Returns a list of dictionaries with 'abbreviation' and 'name' of a unit
```

To convert from one energy unit to another, use the convert() method:

```
result = converter.convert(1000, 'J', 'kWh')
# Converts 1000 Joules to Kilowatt Hours
```

## Error Handling
The ConversionError exception will be raised if there are any issues during the conversion process, such as unknown units or invalid values.

## Contributing
Contributions to PyEnergyX are very welcome! Feel free to fork the repository and submit pull requests.

## License
This project is open source, provided under the MIT License. Feel free to use, modify, and distribute PyEnergyX as you see fit.
