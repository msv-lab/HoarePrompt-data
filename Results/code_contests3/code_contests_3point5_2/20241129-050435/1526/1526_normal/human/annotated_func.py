#State of the program right berfore the function call: w is a string consisting of lowercase letters.**
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: w is a string consisting of lowercase letters, s is a non-empty string, memo is a dictionary where each key represents a unique character in s, and the corresponding value is the frequency of that character in s.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a non-empty string, `memo` is a dictionary where each key represents a unique character in `s`, and the corresponding value is the frequency of that character in `s`, `result` is False if there is at least one value in `memo` that is odd, otherwise `result` is True.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function `func_1` reads a string `s` from input, creates a dictionary `memo` where keys are unique characters in `s` and values are the frequency of those characters. It then checks if the frequency of any character in `memo` is odd. If there is at least one odd frequency, it prints 'No'; otherwise, it prints 'Yes'. The function does not accept any parameters and operates independently of input values.

