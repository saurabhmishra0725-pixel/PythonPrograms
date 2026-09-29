def char_frequency(text):
    """Return a dict mapping every character to the number of times it occurs."""
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


if __name__ == "__main__":
    sample = input("Enter a string: ")
    print(char_frequency(sample))
