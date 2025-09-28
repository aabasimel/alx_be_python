# temp_conversion_tool.py

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def main():
    while True:
        user_input = input("\nEnter the temperature to convert (or 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            temp_input = float(user_input)
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
            continue

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            converted = convert_to_celsius(temp_input)
            print(f"{temp_input}°F is {converted}°C")
        elif unit == 'C':
            converted = convert_to_fahrenheit(temp_input)
            print(f"{temp_input}°C is {converted}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
