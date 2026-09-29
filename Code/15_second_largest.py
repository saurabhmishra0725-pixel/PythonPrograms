def second_largest(numbers):
    """Return the second largest distinct value in numbers.

    Raises ValueError when fewer than two distinct values are available.
    """
    if len(numbers) < 2:
        raise ValueError("list must contain at least two distinct numbers")
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    if len(unique) < 2:
        raise ValueError("list must contain at least two distinct numbers")
    unique.sort()
    return unique[-2]


if __name__ == "__main__":
    values = [int(x) for x in input("Enter numbers separated by space: ").split()]
    print(second_largest(values))
