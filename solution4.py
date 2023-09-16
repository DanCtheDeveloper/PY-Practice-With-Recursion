# Write code for algorithm 4 below

def power(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

# Example usage
print(power(2, 4))  # Output: 16
