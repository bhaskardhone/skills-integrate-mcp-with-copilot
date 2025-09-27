def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

if __name__ == "__main__":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(f"Sum: {add_numbers(x, y)}")
