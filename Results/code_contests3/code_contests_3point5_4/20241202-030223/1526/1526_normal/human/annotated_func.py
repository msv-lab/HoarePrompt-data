#State of the program right berfore the function call: w is a string consisting of lowercase letters.**
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a non-empty user input string, `memo` is a dictionary with key-value pairs where each unique character in string `s` is a key in `memo` with its corresponding value being the frequency of that character in the string `s`.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a non-empty user input string, `memo` is a dictionary with key-value pairs where each unique character in string `s` is a key in `memo` with its corresponding value being the frequency of that character in the string `s`, `result` is False if any of the values in `memo` are odd, otherwise `result` remains True.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function `func_1` reads a non-empty user input string `s`, calculates the frequency of each unique character in the string, and then checks if all character frequencies are even. It then prints 'Yes' if all frequencies are even, otherwise 'No'. The function does not accept any parameters and operates on the global variable `w`, which is a string consisting of lowercase letters.

