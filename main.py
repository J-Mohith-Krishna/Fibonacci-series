def generate_fibonacci(n):
    fib_sequence = [0, 1]

    while fib_sequence[-1] + fib_sequence[-2] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

def main():
    limit = int(input("Enter the limit for Fibonacci sequence: "))
    fibonacci_sequence = generate_fibonacci(limit)

    print("Fibonacci Sequence up to", limit, ":", fibonacci_sequence)

if __name__ == "__main__":
    main()
