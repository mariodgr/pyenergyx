class ConversionError(Exception):
    """
    Exception raised for errors in the conversion process.
    """
    pass


class EnergyConverter:
    """
    A class for converting between different units of energy.
    """

    unit_prefixes = {
        'y': 1e-24,
        'z': 1e-21,
        'a': 1e-18,
        'f': 1e-15,
        'p': 1e-12,
        'n': 1e-9,
        'μ': 1e-6,
        'm': 1e-3,
        'c': 1e-2,
        'd': 1e-1,
        'da': 1e1,
        'h': 1e2,
        'k': 1e3,
        'M': 1e6,
        'G': 1e9,
        'T': 1e12,
        'P': 1e15,
        'E': 1e18,
        'Z': 1e21,
        'Y': 1e24,
    }
    btu_IT=1055.05585262
    base_units = {
        'J': 1,
        'cal': 4.184,
        'Btu': btu_IT,
        'therm': 1055.06 * 1e5,  
        'MMBtu': 1055.06 * 1e6,  
        'quad': 1055.06 * 1e15,
        'eV': 1.60218e-19,
        'tonneTNT': 4.184e9,  
        'TWyr': 31.54e18,  
        'kWh': 60 * 60 * 1e3,
        'short_ton_coal': 18.82e6 * btu_IT ,
        'long_ton_coal': 18.82e6 * (2240/2000) * btu_IT,
        'cord_wood': 20e6 * btu_IT, 
        'cubic_foot_ng': 1036 * btu_IT,  
        'oil_bbl': 5684000 * btu_IT,
        'bbl_av_gasoline': 5.326e9,
        'gal_gasoline': 120214.286 * btu_IT,
        'gal_diesel': 137380.952 * btu_IT,
        'gal_heating_oil': 138500 * btu_IT,
        'bbl_residual_oil': 6.287e6 * btu_IT,
        'gal_propane': 91452 * btu_IT,
        'food_calorie': 1000 * 4.184,
        'toe': 4.187e10,
        'tce': 2.93e10,
        'boe': 6.118e9,
        'horsepower_h': 2684519.5368856,
    }


    def __init__(self):
        """
        Initialize a new instance of the EnergyConverter class.
        """
        self.conversion_factors = self.create_conversion_factors()

    def create_conversion_factors(self):
        """
        Create a dictionary of conversion factors for all units.
        """
        conversion_factors = {}

        for base_unit, base_value in self.base_units.items():
            conversion_factors[base_unit] = base_value
            for prefix, multiple in self.unit_prefixes.items():
                conversion_factors[prefix + base_unit] = base_value * multiple

        return conversion_factors

    def get_units(self):
        """
        Get a list of the available units of energy.

        Returns:
        list: A list of strings, each string being a unit of energy.
        """
        return list(self.conversion_factors.keys())

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
        if from_unit not in self.conversion_factors:
            raise ConversionError(f"Unknown energy unit: {from_unit}")
        if to_unit not in self.conversion_factors:
            raise ConversionError(f"Unknown energy unit: {to_unit}")

        try:
            # Convert from the source unit to Joules
            joules = value * self.conversion_factors[from_unit]

            # Then convert from Joules to the destination unit
            result = joules / self.conversion_factors[to_unit]

            return result

        except Exception as e:
            raise ConversionError(f"Error performing conversion: {str(e)}")
            
converter = EnergyConverter()  # create an object of the class
value_in_Joules = converter.convert(1, 'short_ton_coal', 'Btu')  # convert 100 calories to Joules
print(value_in_Joules)
