#State of the program right berfore the function call: encoded is a string consisting of lowercase Latin letters. The function will be called multiple times (up to 10^4 times) with different strings, each having a length between 1 and 2 \cdot 10^5, and the total length of all strings across all test cases does not exceed 2 \cdot 10^5.
def func_1(encoded):
    mapping = {}
    decoded = []
    for char in encoded:
        if char in mapping:
            decoded.append(mapping[char])
        else:
            for c in range(ord('a'), ord('z') + 1):
                if chr(c) not in mapping.values():
                    mapping[chr(c)] = char
                    break
            decoded.append(chr(c))
        
    #State: `decoded` is a list of characters where each unique character in `encoded` is replaced by a unique character from 'a' to 'z' in the order of their first appearance, and `mapping` is a dictionary that maps each unique character in `decoded` back to its corresponding character in `encoded`.
    return ''.join(decoded)
    #The program returns a string formed by joining the characters in the list `decoded`. Each unique character in the original `encoded` string is replaced by a unique character from 'a' to 'z' in the order of their first appearance.
#Overall this is what the function does:The function takes a string `encoded` consisting of lowercase Latin letters and returns a new string where each unique character in `encoded` is replaced by a unique character from 'a' to 'z' in the order of their first appearance.

