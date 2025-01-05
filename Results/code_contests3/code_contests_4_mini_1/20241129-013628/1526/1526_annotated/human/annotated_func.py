#State of the program right berfore the function call: w is a string consisting of lowercase letters with a length between 1 and 100, inclusive.
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a non-empty string, `memo` contains the count of each unique character in `s`.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a non-empty string, `memo` contains the count of each unique character in `s`, and `result` is False if there is at least one odd count in `memo`, otherwise `result` is True.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase letters with a length between 1 and 100. It counts the occurrences of each character in `s` and checks if all characters have even counts. If all characters have even counts, it prints 'Yes'; otherwise, it prints 'No'. The function does not explicitly return any value.

