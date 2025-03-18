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
    s = ''
    for c in b:
        s += char_map[c]
    return s
num_test_cases = int(input())
for _ in range(num_test_cases):
    num_chars = int(input())
    b = input()
    print(func_1(b))