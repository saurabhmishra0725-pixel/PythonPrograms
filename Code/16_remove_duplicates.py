def remove_duplicates(items):
    """Return a new list with duplicates removed, keeping first-seen order."""
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen


if __name__ == "__main__":
    values = input("Enter values separated by space: ").split()
    print(remove_duplicates(values))
