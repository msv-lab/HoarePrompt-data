#State of the program right berfore the function call: w is a string consisting of lowercase letters.
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `memo` is a dictionary where keys are the characters in `w` and values are the frequency of each character in `w`.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `memo` is a non-empty dictionary, `result` is False if there exists an odd frequency of a character in `w` according to `memo`, otherwise `result` remains True
    print('Yes' if result else 'No')
#Overall this is what the function does:The function `func_1` reads an input string `w` consisting of lowercase letters. It then creates a dictionary `memo` where keys are the characters in `w` and values represent the frequency of each character. The function checks if there exists an odd frequency of any character in `w` and prints 'Yes' if all frequencies are even, otherwise it prints 'No'. The function does not accept any parameters and does not explicitly return any value.

