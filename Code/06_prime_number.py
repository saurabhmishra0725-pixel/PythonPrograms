def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    if not isinstance(n, int):
        raise TypeError("is_prime() only accepts integers")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("Prime" if is_prime(number) else "Not Prime")
