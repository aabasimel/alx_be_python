# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    """Calculate and display the future date after adding a specified number of days."""
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    current_date = display_current_datetime()
    
    while True:
        try:
            days_input = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    calculate_future_date(current_date, days_input)

if __name__ == "__main__":
    main()
