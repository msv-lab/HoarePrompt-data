#State of the program right berfore the function call: w is a string consisting of lowercase letters.**
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a non-empty string, `memo` is a dictionary where each key represents a unique character in `s`, and the value associated with each key is the frequency of that character in `s`.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a non-empty string, `memo` is a non-empty dictionary representing the frequencies of characters in `s`, `result` is True. The loop will make `result` False if any value in `memo.values()` is odd. If all values in `memo.values()` are even, `result` will remain True.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function `func_1` reads an input string `s`, then creates a dictionary `memo` where keys are unique characters in `s` and values represent the frequency of each character. It then checks if all frequencies in `memo` are even. If all frequencies are even, it prints 'Yes'; otherwise, it prints 'No'. The function does not explicitly return a value and operates on a string `w` consisting of lowercase letters.

