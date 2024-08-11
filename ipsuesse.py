class RangedInt:
    def __init__(self, value, max_value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")
        if not isinstance(max_value, int):
            raise ValueError("Max value must be an integer")
        if value < 0 or value > max_value:
            raise ValueError(f"Value {value} is out of the allowed range 0-{max_value}")
        self.value = value
        self.max_value = max_value

# Example usage:
try:
    x2 = RangedInt(10, 12)  # This should work fine
    print(x2.value)         # Outputs: 10
except ValueError as e:
    print(e)
