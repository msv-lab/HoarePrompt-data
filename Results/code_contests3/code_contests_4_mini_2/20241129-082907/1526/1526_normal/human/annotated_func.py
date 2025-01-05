#State of the program right berfore the function call: w is a string consisting of lowercase letters with a length between 1 and 100 inclusive.
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `memo` contains the count of each character in `s`, `w` is a string consisting of lowercase letters.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `memo` contains the count of each character in `s`, `result` is False if any count is odd; otherwise, `result` remains True.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function accepts a string of lowercase letters and prints 'Yes' if all characters appear an even number of times, and 'No' if any character appears an odd number of times.

