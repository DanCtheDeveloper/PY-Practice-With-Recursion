# Write code for algorithm 3 below
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."

    elif n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        # Initialize the first two numbers in the sequence
        first = 0
        second = 1

        # Iterate to calculate the nth Fibonacci number
        for _ in range(2, n):
            next_fib = first + second
            first, second = second, next_fib

        return second

# Example usage
print(fibonacci(4))  # Output: 2
print(fibonacci(2))  # Output: 1
