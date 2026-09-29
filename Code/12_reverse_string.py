def reverse_string(text):
    """Return text reversed without using slicing with [::-1]."""
    result = ""
    for char in text:
        result = char + result
    return result


if __name__ == "__main__":
    sample = input("Enter a string: ")
    print(reverse_string(sample))
