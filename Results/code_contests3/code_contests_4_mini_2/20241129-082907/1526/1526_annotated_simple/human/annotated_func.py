#State of the program right berfore the function call: w is a string consisting of lowercase letters with a length between 1 and 100, inclusive.
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters with a length between 1 and 100; `s` is a non-empty string; `memo` is a dictionary where each key is a character from `s` and each value is the count of occurrences of that character in `s`.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string of lowercase letters, `s` is a non-empty string, `memo` is a dictionary where each key is a character from `s`, `result` is True if all character counts in `s` are even, otherwise `result` is False, and `x` is the count of the current character being evaluated in `s`.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function accepts a string input consisting of lowercase letters and checks if all characters in the string appear an even number of times. It prints 'Yes' if all characters have even counts and 'No' if any character has an odd count. There are no return values from the function.

