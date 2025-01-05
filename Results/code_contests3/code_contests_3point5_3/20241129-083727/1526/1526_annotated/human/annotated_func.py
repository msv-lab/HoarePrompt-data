#State of the program right berfore the function call: w is a string consisting of lowercase letters.
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is an input string, `memo` is a dictionary where each character `c` in `s` is a key, and the value is the count of how many times `c` appears in `s`.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is an input string, `memo` is a dictionary where each character `c` in `s` is a key, and the value is the count of how many times `c` appears in `s`. If any value in `memo` has an odd count, `result` is False, otherwise `result` is True.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function `func_1` reads an input string `s`, creates a dictionary `memo` where each character in `s` is a key storing the count of occurrences, checks if any character count is odd, and prints 'Yes' if all character counts are even, otherwise 'No'. The function operates on a string variable `w` consisting of lowercase letters but does not explicitly return any value.

