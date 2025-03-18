#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, each test case consists of an integer n such that 1 <= n <= 2 * 10^5, and a string b of length n consisting of lowercase Latin letters. The sum of all n values across all test cases does not exceed 2 * 10^5.
def func_1(b):
    """
    Decode the given string b by restoring the original string s.

    Args:
        b (str): The encoded string.

    Returns:
        str: The decoded string s.
    """
    char_map = {}
    for (i, c) in enumerate(sorted(set(b))):
        char_map[c] = chr(ord('a') + (len(b) - i - 1))
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an integer such that 1 <= n <= 2 * 10^5, `b` is a non-empty string of length `n` consisting of lowercase Latin letters, `char_map` is a dictionary with each unique character in `b` mapped to a unique character from 'a' to the `n`-th letter of the alphabet in descending order based on the sorted unique characters of `b`.
    s = ''
    for c in b:
        s += char_map[c]
        
    #State: - `t` remains unchanged as an integer such that 1 <= t <= 10^4.
    #- `n` remains unchanged as an integer such that 1 <= n <= 2 * 10^5.
    #- `b` remains unchanged as a non-empty string of length `n` consisting of lowercase Latin letters.
    #- `char_map` remains unchanged as a dictionary with each unique character in `b` mapped to a unique character from 'a' to the `n`-th letter of the alphabet in descending order based on the sorted unique characters of `b`.
    #- `s` is now a string of length `n` where each character is the mapped character from `char_map` corresponding to the characters in `b`.
    #
    #Output State:
    return s
    #The program returns a string `s` of length `n` where each character in `s` is the mapped character from `char_map` corresponding to the characters in `b`.
#Overall this is what the function does:The function accepts a string `b` of length `n` consisting of lowercase Latin letters. It returns a string `s` of the same length `n` where each character in `s` is a uniquely mapped character from the original characters in `b`, with the mapping determined by the sorted order of unique characters in `b` reversed and mapped to the alphabet in descending order.

