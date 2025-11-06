def nested_sum(nested_list):
    """
    This function finds all numbers in a nested list and returns their sum.
    It can handle lists nested at any depth and will find all numbers to calculate the total.

    Examples:
    - nested_sum([1, 2, 3]) = 6 (flat list)
    - nested_sum([1, [2, 3], 4]) = 10
    - nested_sum([1, [2, [3, 4]], 5]) = 15
    - nested_sum([[1, 2], [3, 4]]) = 10
    - nested_sum([]) = 0 (empty list)

    :param nested_list: list - A list containing numbers or other lists
    :return: int - The sum of all numbers found
    """
    # CODE BELOW

    total = 0
    for item in nested_list:
        if type(item) == list:
             total += nested_sum(item)
        else:
            total += item
    return total
