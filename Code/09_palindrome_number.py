def is_palindrome_number(n):
    """Return True if n reads the same forwards and backwards, else False."""
    if not isinstance(n, int):
        raise TypeError("is_palindrome_number() only accepts integers")
    original = n
    if n < 0:
        return False
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    return original == reversed_n


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("Palindrome" if is_palindrome_number(number) else "Not a Palindrome")
