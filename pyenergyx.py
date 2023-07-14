class ConversionError(Exception):
    """
    Exception raised for errors in the conversion process.
    """
    pass


class EnergyConverter:
    """
    A class for converting between different units of energy.
    """

    btu_IT = 1055.05585262

    base_units = {
        'J': (1, 'J'),
        'kJ': (1e3, 'kJ'),
        'MJ': (1e6, 'MJ'),
        'GJ': (1e9, 'GJ'),
        'TJ': (1e12, 'TJ'),
        'cal': (4.184, 'cal'),
        'Btu': (btu_IT, 'Btu'),
        'therm': (btu_IT * 1e5, 'Therm'),
        'MMBtu': (btu_IT * 1e6, 'MMBtu'),
        'quad': (btu_IT * 1e15, 'quad'),
        'eV': (1.60218e-19, 'eV'),
        'tonneTNT': (4.184e9, 'tTNT'),
        'TWyr': (31.54e18, 'TWyr'),
        'kWh': (60 * 60 * 1e3, 'kWh'),
        'short_ton_coal': (18.82e6 * btu_IT, 'st Coal'),
        'long_ton_coal': (18.82e6 * (2240/2000) * btu_IT, 'lt Coal'),
        'cord_wood': (20e6 * btu_IT, 'cord Wood'),
        'cubic_foot_ng': (1036 * btu_IT, 'ft3 NG'),
        'oil_bbl': (5684000 * btu_IT, 'bbl Oil'),
        'bbl_av_gasoline': (5.326e9, 'bbl Aviation Gasoline'),
        'gal_gasoline': (120214.286 * btu_IT, 'gal Gasoline'),
        'gal_diesel': (137380.952 * btu_IT, 'gal Diesel'),
        'gal_heating_oil': (138500 * btu_IT, 'gal Heating Oil'),
        'bbl_residual_oil': (6.287e6 * btu_IT, 'bbl Residual Oil'),
        'gal_propane': (91452 * btu_IT, 'gal Propane'),
        'food_calorie': (1000 * 4.184, 'Food Calorie'),
        'toe': (4.187e10, 'toe'),
        'tce': (2.93e10, 'tce'),
        'boe': (6.118e9, 'boe'),
        'horsepower_h': (2684519.5368856, 'hph'),
    }


    def __init__(self):
        """
        Initialize a new instance of the EnergyConverter class.
        """
        self.conversion_factors, self.friendly_names = self.create_conversion_factors()

    def create_conversion_factors(self):
        """
        Create a dictionary of conversion factors and friendly names for all units.
        """
        conversion_factors = {}
        friendly_names = {}

        for base_unit, (base_value, friendly_name) in self.base_units.items():
            conversion_factors[base_unit] = base_value
            friendly_names[base_unit] = friendly_name

        return conversion_factors, friendly_names


        return conversion_factors, friendly_names

    def get_units(self):
        """
        Get a list of the available units of energy.

        Returns:
        list: A list of dictionaries, each containing the 'abbreviation' and 'name' of a unit of energy.
        """
        return [{'abbreviation': unit, 'name': self.friendly_names[unit]} for unit in self.conversion_factors.keys()]

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
