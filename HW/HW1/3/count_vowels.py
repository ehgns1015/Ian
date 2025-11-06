def count_vowels(s):
    """
    This function counts the number of vowels (a, e, i, o, u) in the given string 's'.
    It treats uppercase and lowercase vowels equally and ignores non-alphabetic characters.
    
    :param s: The input string to be checked
    :return: The total count of vowels in the string

    Example:
    >>> count_vowels("Hello World")
    3
    >>> count_vowels("Python is fun!")
    4
    >>> count_vowels("12345!@#$%")
    0
    >>> count_vowels("")
    0
    """
    vowels = "aeiouAEIOU"  # Define the vowels to look for
    count = 0  # Initialize a counter to zero

    # CODE BELOW
    # Loop through each character in the string
    # Check if the character is a vowel
    # Increment the counter if it's a vowel
    # Return the total count of vowels

    for char in s:
        if char in vowels:
            count += 1

    return count
