def check_even_odd(num):
    """Return 'Even' if num is even, otherwise 'Odd'."""
    if num % 2 == 0:
        return "Even"
    return "Odd"


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(check_even_odd(number))
