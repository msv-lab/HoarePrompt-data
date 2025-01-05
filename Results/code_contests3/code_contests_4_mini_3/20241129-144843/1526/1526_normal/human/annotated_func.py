#State of the program right berfore the function call: w is a string consisting of lowercase letters ('a' to 'z') with a length between 1 and 100.
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a non-empty string; `memo` contains each unique character from `s` as keys with their corresponding counts as values.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a non-empty string, `memo` contains each unique character from `s` with their corresponding counts as values, and `result` is False if any value in `memo` is odd; otherwise, `result` is True.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase letters and checks if all characters in the string have even counts. It prints 'Yes' if all characters appear an even number of times, and 'No' if any character appears an odd number of times.

