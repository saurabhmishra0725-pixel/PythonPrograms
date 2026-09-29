def is_palindrome_string(text):
    """Return True if text is a palindrome.

    Case and non-alphanumeric characters are ignored.
    """
    cleaned = ""
    for char in text:
        if char.isalnum():
            cleaned += char.lower()
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    sample = input("Enter a string: ")
    print("Palindrome" if is_palindrome_string(sample) else "Not a Palindrome")
