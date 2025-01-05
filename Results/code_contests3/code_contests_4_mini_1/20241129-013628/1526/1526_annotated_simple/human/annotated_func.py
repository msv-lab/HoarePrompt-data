#State of the program right berfore the function call: w is a string consisting of lowercase letters with a length between 1 and 100 inclusive.
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a string consisting of lowercase letters, `memo` is a dictionary containing each unique character from `s` as keys and their corresponding counts as values.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` and `s` are strings consisting of lowercase letters, `memo` is a dictionary containing unique characters from `s` and their counts, `result` is either True (if all counts are even) or False (if at least one count is odd).
    print('Yes' if result else 'No')
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase letters, counts the occurrences of each character, and checks whether all character counts are even. It prints 'Yes' if all counts are even and 'No' if at least one count is odd. However, the function does not accept any parameters directly; instead, it reads the input from the user with `raw_input()`, which may not align with the annotation stating it accepts a parameter `w`. Additionally, the function does not return any value; it only prints the result.

