def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
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


def primes_in_range(start, end):
    """Return a list of all prime numbers between start and end (inclusive)."""
    if start > end:
        start, end = end, start
    return [num for num in range(start, end + 1) if is_prime(num)]


if __name__ == "__main__":
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    print(primes_in_range(start, end))
