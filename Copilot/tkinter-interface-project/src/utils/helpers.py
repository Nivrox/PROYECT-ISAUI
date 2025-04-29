def validate_input(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def format_output(value):
    return f"{value:.2f}"

def calculate_area(a, b, n):
    delta_x = (b - a) / n
    return delta_x * (a + b) / 2  # Example of a simple area calculation (trapezoidal rule)