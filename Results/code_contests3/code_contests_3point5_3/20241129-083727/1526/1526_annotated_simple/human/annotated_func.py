#State of the program right berfore the function call: w is a string consisting of lowercase letters.**
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a string input, `memo` is a dictionary with each unique character in `s` as keys and their respective frequencies as values.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a non-empty string consisting of lowercase letters, `s` is a non-empty string input, `memo` is a dictionary with key-value pairs representing the frequencies of unique characters in `s`, `result` is False if there exists at least one odd frequency in `memo.values()`, otherwise `result` remains True.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function `func_1` reads a string input `s`, creates a dictionary `memo` to store the frequencies of unique characters in `s`, and then checks if all character frequencies are even. If there exists at least one odd frequency, it prints 'No'; otherwise, it prints 'Yes'. The function does not return any value explicitly.

