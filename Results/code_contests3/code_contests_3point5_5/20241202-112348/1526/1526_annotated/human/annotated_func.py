#State of the program right berfore the function call: w is a string consisting of lowercase letters.**
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: w is a string consisting of lowercase letters, s is an empty string, memo is a dictionary where each character in w is a key and its value is the number of occurrences of that character in the input string s.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is an empty string, `memo` is a dictionary with values where all the values are even, `result` is True
    print('Yes' if result else 'No')
#Overall this is what the function does:The function `func_1` reads an input string `w` consisting of lowercase letters. It then creates a dictionary `memo` where each character in `w` is a key, and the value is the number of occurrences of that character in the input string. Subsequently, it checks if all the values in `memo` are even. If all values are even, it prints 'Yes'; otherwise, it prints 'No'. The function does not explicitly return any value. However, it may not handle edge cases where the input string is empty or contains non-lowercase characters.

