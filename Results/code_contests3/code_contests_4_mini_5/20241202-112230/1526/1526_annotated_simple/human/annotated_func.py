#State of the program right berfore the function call: w is a string consisting of lowercase letters with a length between 1 and 100, inclusive.
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters with a length between 1 and 100, `s` is a non-empty string, `memo` contains keys for each unique character in `s` with their values representing the count of occurrences of those characters.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters with a length between 1 and 100, `s` is a non-empty string, `memo` contains keys for each unique character in `s`, `result` is False if at least one value in `memo.values()` is odd, otherwise `result` is True.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase letters with a length between 1 and 100 and checks if all characters in `s` occur an even number of times. If they do, it prints 'Yes'; if any character occurs an odd number of times, it prints 'No'.

