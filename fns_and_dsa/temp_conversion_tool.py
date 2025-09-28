# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius
    Uses global FAHRENHEIT_TO_CELSIUS_FACTOR
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit
    Uses global CELSIUS_TO_FAHRENHEIT_FACTOR
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        
        try:
            temperature = float(temp_input)
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()