#State of the program right berfore the function call: w is a string consisting of lowercase letters.**
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a user-input string, `memo` is a dictionary containing each unique character `c` in `s` as a key with its corresponding frequency as the value.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a user-input string, `memo` is a dictionary containing each unique character `c` in `s` as a key with its corresponding frequency as the value, `result` is False if there exists at least one character with an odd frequency in `memo.values()`, otherwise `result` is True.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function `func_1` reads a user-input string `s`, creates a dictionary `memo` to store the frequency of each unique character in `s`, and then checks if there is an odd frequency character in `memo`. If there is at least one character with an odd frequency, it prints 'No'; otherwise, it prints 'Yes'. The function operates on the string `w`, consisting of lowercase letters, but it does not explicitly return any value.

