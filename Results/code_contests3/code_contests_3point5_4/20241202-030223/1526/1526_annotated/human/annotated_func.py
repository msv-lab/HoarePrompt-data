#State of the program right berfore the function call: w is a string consisting of lowercase letters.**
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `memo` is a dictionary where each key represents a unique character in `w` and the corresponding value is the frequency of that character in `w`.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `memo` is a dictionary with values representing the frequency of characters in `w`, `result` is True if all values in `memo` are even, otherwise False.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function `func_1` reads input from the user as a string `s` consisting of lowercase letters. It then constructs a dictionary `memo` where each key represents a unique character in `s` and the corresponding value is the frequency of that character. After that, it checks if all frequencies in `memo` are even, and prints 'Yes' if they are, otherwise 'No'. The function does not accept any parameters and does not return any value.

