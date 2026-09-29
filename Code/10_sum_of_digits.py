def sum_of_digits(n):
    """Return the sum of the digits of n (sign is ignored)."""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(sum_of_digits(number))
