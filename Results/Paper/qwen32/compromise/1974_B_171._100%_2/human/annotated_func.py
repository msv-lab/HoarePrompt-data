#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and encoded is a string of length n consisting of lowercase Latin letters. The sum of all n values across all test cases does not exceed 2 * 10^5.
def func_1(encoded):
    unique_chars = sorted(set(encoded))
    char_map = {}
    len_unique = len(unique_chars)
    for i in range(len_unique):
        char_map[unique_chars[i]] = unique_chars[len_unique - 1 - i]
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an integer such that 1 <= n <= 2 * 10^5; `encoded` is a string of length `n` consisting of lowercase Latin letters; `unique_chars` is a sorted list of unique characters from `encoded`; `char_map` is a dictionary where each unique character in `unique_chars` is mapped to its reverse counterpart in the sorted list; `len_unique` is the number of unique characters in `encoded`.
    decoded = ''.join(char_map[ch] for ch in encoded)
    return decoded
    #The program returns a string `decoded` of length `n` where each character is the reverse counterpart of the corresponding character in `encoded` as per `char_map`.
#Overall this is what the function does:The function takes a string `encoded` consisting of lowercase Latin letters and returns a new string `decoded` of the same length, where each character is replaced by its reverse counterpart based on the sorted order of unique characters in `encoded`.

