def safe_divide(numerator, denominator):
    """
    Perform division with robust error handling for:
    - Division by zero
    - Non-numeric inputs
    
    Returns:
        float: Result of division if successful
        str: Error message if division fails
    """
    try:
        num = float(numerator)
        den = float(denominator)
        
        result = num / den
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
    
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"