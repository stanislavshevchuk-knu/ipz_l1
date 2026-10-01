
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

if __name__ == "__main__":
    n_terms = int(input("enter the number of Fibonacci numbers: "))
    print(f"first {n_terms} Fibonacci numbers:")
    print(fibonacci(n_terms))