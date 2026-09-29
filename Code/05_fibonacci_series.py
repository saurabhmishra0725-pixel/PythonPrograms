def fibonacci(n):
    """Return a list containing the first n terms of the Fibonacci series."""
    if not isinstance(n, int):
        raise TypeError("fibonacci() only accepts integers")
    if n < 0:
        raise ValueError("fibonacci() is not defined for negative numbers")
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


if __name__ == "__main__":
    number = int(input("How many Fibonacci terms? "))
    print(fibonacci(number))
