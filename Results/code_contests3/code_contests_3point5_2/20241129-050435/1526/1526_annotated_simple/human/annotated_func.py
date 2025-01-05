#State of the program right berfore the function call: w is a string consisting of lowercase letters.**
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a non-empty string, `memo` is a dictionary with each unique character in `s` as a key and the value corresponding to the number of occurrences of that character in `s`.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a non-empty string, `memo` is a dictionary with each unique character in `s` as a key and the value corresponding to the number of occurrences of that character in `s`, `result` is True if all values in `memo` are even, and False otherwise.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function `func_1` reads a string input `s`, creates a dictionary `memo` where each unique character in `s` is a key with the corresponding count of occurrences, and then checks if all counts of characters in `memo` are even. It prints 'Yes' if all counts are even, otherwise 'No'. The function does not explicitly return any value.

