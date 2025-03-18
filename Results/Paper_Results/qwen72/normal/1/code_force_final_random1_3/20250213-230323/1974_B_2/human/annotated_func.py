#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters, and the length of s is between 1 and 2 \cdot 10^5.
def func_1(s):
    unique_chars = sorted(list({char for char in s}))
    i, j = 0, len(unique_chars) - 1
    for char in s:
        if char in unique_chars:
            s = s.replace(char, unique_chars[j])
            j -= 1
        else:
            unique_chars.insert(i, char)
            i += 1
            j += 1
        
    #State: After all iterations of the loop, `s` will consist of the last unique character in `unique_chars` repeated for each character in the original `s` that was in `unique_chars`. Characters in `s` that were not originally in `unique_chars` will remain unchanged. The `unique_chars` list will contain all characters from the original `s` in the order they first appeared, and `i` will be equal to the number of unique characters added to `unique_chars` during the loop. `j` will be 0, as it is decremented for each unique character processed in `s`.
    return ''.join(unique_chars)
    #The program returns a string consisting of all unique characters from the original `s` in the order they first appeared.
#Overall this is what the function does:The function `func_1` takes a string `s` as input and returns a new string containing all unique characters from `s` in the order they first appeared. The input string `s` is modified during the function's execution, but the final state of `s` is not relevant to the function's output. The function ensures that the returned string contains each unique character from `s` exactly once, preserving their first occurrence order.

