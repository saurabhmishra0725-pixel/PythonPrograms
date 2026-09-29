def common_elements(list_a, list_b):
    """Return the distinct elements present in both lists (order of list_a)."""
    result = []
    for item in list_a:
        if item in list_b and item not in result:
            result.append(item)
    return result


if __name__ == "__main__":
    a = input("Enter first list values: ").split()
    b = input("Enter second list values: ").split()
    print(common_elements(a, b))
