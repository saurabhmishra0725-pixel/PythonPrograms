def largest_of_three(a, b, c):
    """Return the largest of three numbers."""
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest


if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print(largest_of_three(a, b, c))
