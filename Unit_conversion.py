import numpy as np
import time
import sys
def type_effect(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def convert_units(value, from_unit, to_unit, conversion_factors):
    if from_unit == to_unit:
        return value
    elif (from_unit, to_unit) in conversion_factors:
        return value * conversion_factors[(from_unit, to_unit)]
    else:
        return "Invalid unit selection!"
def format_scientific(value):
    if value == 0:
        return "0.00 × 10^0"
    exponent = int(np.floor(np.log10(abs(value))))
    coefficient = value / (10 ** exponent)
    return f"{coefficient:.2f} × 10^{exponent}"
def main():
    logo = r"""
  ____  __  __
 |  _ \|  \/  |   // CODE BY R.M
 | |_) | |\/| |   << rmog.ir >>
 |  _ <| |  | |
 |_| \_\_|  |_|
"""
    type_effect(logo, delay=0.05)
    type_effect("Welcome to the Multi-Unit Converter!")
    categories = {
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
        "Length": ["Meter", "Kilometer", "Millimeter"],
        "Weight": ["Kilogram", "Gram", "Ton"]
    }
    conversion_factors = {
        ("Meter", "Kilometer"): 0.001,
        ("Meter", "Millimeter"): 1000,
        ("Kilometer", "Meter"): 1000,
        ("Kilometer", "Millimeter"): 1_000_000,
        ("Millimeter", "Meter"): 0.001,
        ("Millimeter", "Kilometer"): 0.000001,
        ("Kilogram", "Gram"): 1000,
        ("Kilogram", "Ton"): 0.001,
        ("Gram", "Kilogram"): 0.001,
        ("Gram", "Ton"): 0.000001,
        ("Ton", "Kilogram"): 1000,
        ("Ton", "Gram"): 1_000_000,
    }
    print("\n" + "*" * 30)
    for i, category in enumerate(categories.keys(), 1):
        type_effect(f"{i}. {category}")
    print("*" * 30)
    try:
        type_effect("Select a category (1-3): ", delay=0.1)
        category_choice = int(input())
        if 1 <= category_choice <= len(categories):
            selected_category = list(categories.keys())[category_choice - 1]
            units = categories[selected_category]
            if selected_category == "Temperature":
                def temperature_conversion(value, from_unit, to_unit):
                    conversions = {
                        ("Celsius", "Fahrenheit"): lambda x: (x * 9 / 5) + 32,
                        ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5 / 9,
                        ("Celsius", "Kelvin"): lambda x: x + 273.15,
                        ("Kelvin", "Celsius"): lambda x: x - 273.15,
                        ("Fahrenheit", "Kelvin"): lambda x: (x - 32) * 5 / 9 + 273.15,
                        ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15) * 9 / 5 + 32
                    }
                    return conversions.get((from_unit, to_unit), lambda x: x)(value)
                convert_function = temperature_conversion
            else:
                convert_function = lambda v, f, t: convert_units(v, f, t, conversion_factors)
            type_effect("\nAvailable units:")
            print("*" * 30)
            for i, unit in enumerate(units, 1):
                type_effect(f"{i}. {unit}")
            print("*" * 30)
            type_effect("Select the source unit (1-3): ", delay=0.1)
            from_choice = int(input())
            type_effect("Select the target unit (1-3): ", delay=0.1)
            to_choice = int(input())
            if 1 <= from_choice <= len(units) and 1 <= to_choice <= len(units):
                from_unit = units[from_choice - 1]
                to_unit = units[to_choice - 1]
                type_effect(f"Please enter the value in {from_unit}: ", delay=0.1)
                value = float(input())
                result = convert_function(value, from_unit, to_unit)
                normal_format = np.round(result, 2)
                scientific_format = format_scientific(result)
                time.sleep(1)
                type_effect(f"\nConverted to {to_unit}:", delay=0.1)
                type_effect(f"- Normal mode: {normal_format}", delay=0.1)
                type_effect(f"- Scientific notation mode: {scientific_format}", delay=0.1)
            else:
                type_effect("Invalid unit selection!", delay=0.1)
        else:
            type_effect("Invalid category selection!", delay=0.1)
    except ValueError:
        type_effect("Please enter a valid number!", delay=0.1)
if __name__ == "__main__":
    main()