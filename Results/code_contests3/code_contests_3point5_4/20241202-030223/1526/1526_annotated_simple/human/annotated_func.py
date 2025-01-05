#State of the program right berfore the function call: **
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `s` is a string, `memo` is a dictionary containing the count of each character in `s`
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `s` is a string, `memo` is a dictionary containing the count of each character in `s` with at least 1 value. If any value in `memo` is odd, `result` is False; otherwise, `result` is True.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function `func_1` reads a string input `s`, counts the occurrences of each character in the string, and checks if the count of any character is odd. If any character count is odd, it prints 'No'; otherwise, it prints 'Yes'. The function does not accept any parameters and does not return any value.

