#State of the program right berfore the function call: w is a string consisting of lowercase letters with a length between 1 and 100.
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string of lowercase letters with a length between 1 and 100; `memo` is a dictionary mapping each character in `s` to its frequency.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string of lowercase letters with a length between 1 and 100, `memo` is a dictionary mapping each character to its frequency, and `result` is True if all frequencies are even, otherwise False if at least one frequency is odd.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function accepts a string of lowercase letters and prints 'Yes' if all characters in the string appear an even number of times; otherwise, it prints 'No'.

