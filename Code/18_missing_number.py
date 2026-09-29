def missing_number(numbers):
    """Return the missing number from 1..n given n-1 unique numbers.

    Example: missing_number([1, 2, 4, 5]) -> 3
    """
    if not numbers:
        raise ValueError("numbers must not be empty")
    n = max(max(numbers), len(numbers) + 1)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(numbers)


if __name__ == "__main__":
    values = [int(x) for x in input("Enter numbers separated by space: ").split()]
    print(missing_number(values))
