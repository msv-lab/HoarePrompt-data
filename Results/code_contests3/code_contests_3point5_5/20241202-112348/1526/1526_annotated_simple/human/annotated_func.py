#State of the program right berfore the function call: w is a string consisting of lowercase letters.
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: Output State: `w` is a string consisting of lowercase letters, `s` is a string consisting of lowercase letters, `memo` is a dictionary with keys as unique characters from `s` and values as the frequency of those characters in `s`.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a string consisting of lowercase letters, `memo` is a dictionary with keys as unique characters from `s` and values as the frequency of those characters in `s`, `result` is True. `result` is False if there exists at least one value in `memo` that is odd. Otherwise, `result` remains True.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function func_1 reads a string `s` from user input, creates a dictionary `memo` with the frequency of each unique character in the string, and then checks if all character frequencies in `memo` are even. If all frequencies are even, it prints 'Yes', otherwise it prints 'No'. The function does not accept any parameters and does not have a specific return value.

