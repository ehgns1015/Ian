def count_words(words):
    """
    Given a list of words, count how many times each word appears.
    
    :param words: list of strings
    :return: dict mapping each word to its count
    
    Example:
    >>> count_words(["apple", "banana", "apple", "orange", "banana", "apple"])
    {'apple': 3, 'banana': 2, 'orange': 1}
    """
    counts = {}
    # CODE BELOW
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
