#State of the program right berfore the function call: # Precondition

**w is a string consisting of lowercase letters.**
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a non-empty string, `memo` is a dictionary with keys as each unique character in `s` and their corresponding values are the number of occurrences of that character in `s`
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a non-empty string, `memo` is a dictionary with key-value pairs where the values are all even, and `result` is either True or False based on the conditions met during the loop execution.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function func_1 reads a string `s` as input, creates a dictionary `memo` to store the count of each unique character in `s`, and then checks if the count of all characters in `s` is even. If all counts are even, it prints 'Yes'; otherwise, it prints 'No'. The function operates on a string `w` consisting of lowercase letters.

