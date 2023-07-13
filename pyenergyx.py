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
        'J': (1, 'Joule'),
        'kJ': (1e3, 'Kilojoule'),
        'MJ': (1e6, 'Megajoule'),
        'GJ': (1e9, 'Gigajoule'),
        'TJ': (1e12, 'Terajoule'),
        'cal': (4.184, 'Calorie'),
        'Btu': (btu_IT, 'British Thermal Unit'),
        'therm': (btu_IT * 1e5, 'Therm'),
        'MMBtu': (btu_IT * 1e6, 'Million British Thermal Units'),
        'quad': (btu_IT * 1e15, 'Quadrillion British Thermal Units'),
        'eV': (1.60218e-19, 'Electron Volt'),
        'tonneTNT': (4.184e9, 'Tonne of TNT'),
        'TWyr': (31.54e18, 'Terawatt Year'),
        'kWh': (60 * 60 * 1e3, 'Kilowatt Hour'),
        'short_ton_coal': (18.82e6 * btu_IT, 'Short Ton of Coal'),
        'long_ton_coal': (18.82e6 * (2240/2000) * btu_IT, 'Long Ton of Coal'),
        'cord_wood': (20e6 * btu_IT, 'Cord of Wood'),
        'cubic_foot_ng': (1036 * btu_IT, 'Cubic Foot of Natural Gas'),
        'oil_bbl': (5684000 * btu_IT, 'Oil Barrel'),
        'bbl_av_gasoline': (5.326e9, 'Barrel of Aviation Gasoline'),
        'gal_gasoline': (120214.286 * btu_IT, 'Gallon of Gasoline'),
        'gal_diesel': (137380.952 * btu_IT, 'Gallon of Diesel'),
        'gal_heating_oil': (138500 * btu_IT, 'Gallon of Heating Oil'),
        'bbl_residual_oil': (6.287e6 * btu_IT, 'Barrel of Residual Oil'),
        'gal_propane': (91452 * btu_IT, 'Gallon of Propane'),
        'food_calorie': (1000 * 4.184, 'Food Calorie'),
        'toe': (4.187e10, 'Tonne of Oil Equivalent'),
        'tce': (2.93e10, 'Tonne of Coal Equivalent'),
        'boe': (6.118e9, 'Barrel of Oil Equivalent'),
        'horsepower_h': (2684519.5368856, 'Horsepower Hour'),
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
