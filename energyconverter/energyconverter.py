import logging

class EnergyConverter:
    def __init__(self):
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

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
            # ... add other units similarly ...
        }

    def convert(self, value, from_unit, to_unit):
        # Error checking: make sure the units are known
        if from_unit not in self.conversion_factors_to_joule:
            self.logger.error(f"Unknown energy unit: {from_unit}")
            return None
        if to_unit not in self.conversion_factors_to_joule:
            self.logger.error(f"Unknown energy unit: {to_unit}")
            return None

        # Convert from the source unit to Joules
        joules = value * self.conversion_factors_to_joule[from_unit]

        # Then convert from Joules to the destination unit
        result = joules / self.conversion_factors_to_joule[to_unit]

        # Log the conversion
        self.logger.info(f"Converted {value} {from_unit} to {result} {to_unit}")
        return result


# usage example:
converter = EnergyConverter()
value_in_joules = converter.convert(10, 'horsepower-hour', 'J')  # Converts 10 horsepower-hour to J

if value_in_joules is not None:
    print(value_in_joules)
