def find_duplicates(items):
    """Return values that appear more than once, in order of first appearance."""
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return [item for item in dict.fromkeys(items) if counts[item] > 1]


if __name__ == "__main__":
    values = input("Enter values separated by space: ").split()
    print(find_duplicates(values))
