def double_factorial(n):
    """
    This function calculates the double factorial of a number.
    Double factorial is n!! = n × (n-2) × (n-4) × ... decreasing by 2 each time.

    Examples:
    - double_factorial(5) = 5 × 3 × 1 = 15
    - double_factorial(6) = 6 × 4 × 2 = 48
    - double_factorial(0) = 1 (by definition)
    - double_factorial(1) = 1

    :param n: int - A non-negative integer
    :return: int - The double factorial value of n

    Hints: 
    - Base case is when n is 0 or 1.
    - Recursive case is n * double_factorial(n-2).
    """
    # CODE BELOW
    if n == 0 or n == 1:
        return 1
    return n * double_factorial(n - 2)