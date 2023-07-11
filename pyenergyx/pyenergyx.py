class ConversionError(Exception):
    """
    Exception raised for errors in the conversion process.
    """
    pass


class EnergyConverter:
    """
    A class for converting between different units of energy.
    """
    def __init__(self):
        """
        Initialize a new instance of the EnergyConverter class.
        """
               # Conversion factors to convert from each unit to Joules.
        # These are calculated as follows:

        self.conversion_factors_to_joule = {
            'GJ': 1e9,  # 1 gigajoule = 1e9 joules
            'MJ': 1e6,  # 1 megajoule = 1e6 joules
            'kJ': 1e3,  # 1 kilojoule = 1e3 joules
            'J': 1,     # 1 joule = 1 joule
            'kcal': 1000 * 4.184,  # 1 kilocalorie = 1000 calories, 1 calorie = 4.184 joules
            'cal': 4.184,  # 1 calorie = 4.184 joules
            'kWh': 1000 * 60 * 60,  # 1 kilowatt-hour = 1000 watts-hour = 3600 seconds * 1 watt
            'MWh': 1e6 * 60 * 60,  # 1 megawatt-hour = 1e6 watts-hour = 3600 seconds * 1 megawatt
            'Wh': 60 * 60,  # 1 watt-hour = 3600 seconds * 1 watt
            'Ws': 1,  # 1 watt-second = 1 joule
            'horsepower-hour': 745.7 * 60 * 60,  # 1 horsepower-hour = 745.7 watts * 3600 seconds
            'koe': 1e3 * 4.1868e7,  # 1 kg of oil equivalent = 1e3 * 4.1868e7 joules
            'toe': 1e3 * 1e3 * 4.1868e7,  # 1 tonne of oil equivalent = 1e3 kg of oil equivalent = 1e3 * 1e3 * 4.1868e7 joules
            'ktoe': 1e3 * 1e3 * 1e3 * 4.1868e7,  # 1 thousand tonnes of oil equivalent = 1e3 tonnes of oil equivalent = 1e3 * 1e3 * 1e3 * 4.1868e7 joules
            'Mtoe': 1e3 * 1e3 * 1e3 * 1e3 * 4.1868e7,  # 1 million tonnes of oil equivalent = 1e3 thousand tonnes of oil equivalent = 1e3 * 1e3 * 1e3 * 1e3 * 4.1868e7 joules
            'boe': 5.8e6,  # 1 barrel of oil equivalent = 5.8e6 joules
            'kboe': 1e3 * 5.8e6,  # 1 thousand barrels of oil equivalent = 1e3 barrels of oil equivalent = 1e3 * 5.8e6 joules
            'Mboe': 1e3 * 1e3 * 5.8e6,  # 1 million barrels of oil equivalent = 1e3 thousand barrels of oil equivalent = 1e3 * 1e3 * 5.8e6 joules
            'Gm3 NG': 1e9 * 1e3,  # 1 billion m3 natural gas = 1e9 m3 natural gas = 1e9 * 1e3 joules
            'Gft3 NG': 1e9 * 1.055056e3,  # 1 billion ft3 natural gas = 1e9 ft3 natural gas = 1e9 * 1.055056e3 joules
            'Mt LNG': 1e6 * 1e3 * 1e3,  # 1 million tonnes liquefied natural gas = 1e6 tonnes liquefied natural gas = 1e6 * 1e3 * 1e3 joules
            'Gt LNG': 1e9 * 1e3 * 1e3,  # 1 billion tonnes liquefied natural gas = 1e9 tonnes liquefied natural gas = 1e9 * 1e3 * 1e3 joules
            'kg SKE': 1e3 * 2.93e7,  # 1 kg hard coal = 1e3 g hard coal = 1e3 * 2.93e7 joules
            't SKE': 1e3 * 1e3 * 2.93e7,  # 1 tonne hard coal = 1e3 kg hard coal = 1e3 * 1e3 * 2.93e7 joules
            'GeV': 1e9 * 1.60218e-19,  # 1 gigaelectronvolt = 1e9 electronvolts = 1e9 * 1.60218e-19 joules
            'TeV': 1e12 * 1.60218e-19,  # 1 tera-electronvolt = 1e12 electronvolts = 1e12 * 1.60218e-19 joules
            'MeV': 1e6 * 1.60218e-19,  # 1 mega-electronvolt = 1e6 electronvolts = 1e6 * 1.60218e-19 joules
            'keV': 1e3 * 1.60218e-19,  # 1 kilo-electronvolt = 1e3 electronvolts = 1e3 * 1.60218e-19 joules
            'eV': 1.60218e-19,  # 1 electronvolt = 1.60218e-19 joules
            'Btu': 1055.06,  # 1 british thermal unit = 1055.06 joules
            'MMBtu': 1e6 * 1055.06,  # 1 million british thermal units = 1e6 british thermal units = 1e6 * 1055.06 joules
            'thm': 1e5 * 1055.06,  # 1 therm = 1e5 british thermal units = 1e5 * 1055.06 joules
            'quad': 1e15 * 1055.06,  # 1 quad = 1e15 british thermal units = 1e15 * 1055.06 joules
            'erg': 1e-7,  # 1 erg = 1e-7 joules
            'Mt': 1e6 * 1e3 * 1e3 * 1e3,  # 1 megatonne TNT = 1e6 tonnes TNT = 1e6 * 1e3 * 1e3 * 1e3 joules
            'kT': 1e3 * 1e3 * 1e3 * 1e3,  # 1 kilotonne TNT = 1e3 tonnes TNT = 1e3 * 1e3 * 1e3 * 1e3 joules
            'ft-lb': 1.35581794833,  # 1 foot-pound = 1.35581794833 joules
        }


    def get_units(self):
        """
        Get a list of the available units of energy.
        
        Returns:
        list: A list of strings, each string being a unit of energy.
        """
        return list(self.conversion_factors_to_joule.keys())
        
    def convert(self, value, from_unit, to_unit):
        """
        Convert a given value from one unit of energy to another.

        Args:
        value (float): The value to convert.
        from_unit (str): The unit to convert from.
        to_unit (str): The unit to convert to.

        Returns:
        float: The converted value.

        Raises:
        ConversionError: If there is a problem with the conversion, such as unknown units or invalid values.
        """

        # Error checking: make sure the units are known
        if from_unit not in self.conversion_factors_to_joule:
            raise ConversionError(f"Unknown energy unit: {from_unit}")
        if to_unit not in self.conversion_factors_to_joule:
            raise ConversionError(f"Unknown energy unit: {to_unit}")

        try:
            # Convert from the source unit to Joules
            joules = value * self.conversion_factors_to_joule[from_unit]

            # Then convert from Joules to the destination unit
            result = joules / self.conversion_factors_to_joule[to_unit]

            return result

        except Exception as e:
            raise ConversionError(f"Error performing conversion: {str(e)}")

converter = EnergyConverter()

# Get available units for dropdown menus
units = converter.get_units()

# Perform conversion
try:
    result = converter.convert(value, from_unit, to_unit)
    print(f"{value} {from_unit} = {result} {to_unit}")
except ConversionError as e:
    print(f"Error performing conversion: {str(e)}")
