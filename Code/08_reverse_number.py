def reverse_number(n):
    """Return the number with its digits reversed, keeping the sign."""
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    return sign * reversed_n


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(reverse_number(number))
