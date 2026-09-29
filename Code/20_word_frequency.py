def word_frequency(sentence):
    """Return a dict mapping each lower-cased word to the number of occurrences."""
    frequency = {}
    for word in sentence.split():
        key = word.lower()
        frequency[key] = frequency.get(key, 0) + 1
    return frequency


if __name__ == "__main__":
    sample = input("Enter a sentence: ")
    print(word_frequency(sample))
