def classify_number(num):
    """Return 'Positive', 'Negative' or 'Zero' for the given number."""
    if num > 0:
        return "Positive"
    if num < 0:
        return "Negative"
    return "Zero"


if __name__ == "__main__":
    number = float(input("Enter a number: "))
    print(classify_number(number))
