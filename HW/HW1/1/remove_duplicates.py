def remove_duplicates(items):
    # CODE BELOW
    """
    This function takes a list and removes any duplicate values from it.
    It keeps the order of the items the same as the original list.

    For example:
    If the input is [1, 2, 2, 3], the output will be [1, 2, 3].

    :param items: list - A list of items (numbers, strings, etc.). 
                          Some items may appear more than once.
    :return: list - A new list that has the same items,
                    but with duplicates removed.
                    The order of the first appearance of each item is kept.

    Hint: What is Set?
    """
    # [1,1,1,1,2,3,4,5,5,6]
    seen = set()
    result = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result
