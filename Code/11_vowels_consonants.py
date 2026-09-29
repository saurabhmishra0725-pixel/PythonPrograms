VOWELS = "aeiouAEIOU"


def count_vowels_consonants(text):
    """Return a dict with the number of vowels and consonants in text.

    Only alphabetic characters are counted; everything else is ignored.
    """
    vowels = 0
    consonants = 0
    for char in text:
        if not char.isalpha():
            continue
        if char in VOWELS:
            vowels += 1
        else:
            consonants += 1
    return {"vowels": vowels, "consonants": consonants}


if __name__ == "__main__":
    sample = input("Enter a string: ")
    print(count_vowels_consonants(sample))
