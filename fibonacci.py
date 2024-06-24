def generate_fibonacci(n):
    fib_sequence = [0, 1]  # Starting the sequence with the first two numbers
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Append the sum of the last two numbers
    return fib_sequence

# Number of Fibonacci numbers to generate
n = 18

# Generate the Fibonacci sequence
fib_sequence = generate_fibonacci(n)

# Print the Fibonacci sequence
print(f"The first {n} Fibonacci numbers are:")
print(fib_sequence)

