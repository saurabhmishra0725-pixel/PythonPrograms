def factorial(n):
    """Return n! (n factorial). Raises ValueError for negative numbers."""
    if not isinstance(n, int):
        raise TypeError("factorial() only accepts integers")
    if n < 0:
        raise ValueError("factorial() is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    number = int(input("Enter a non-negative integer: "))
    print(factorial(number))
