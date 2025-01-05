#State of the program right berfore the function call: w is a string consisting of lowercase letters (`a`-`z`).
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters `a-z`, `s` is a non-empty input string with all characters processed, `memo` is a dictionary with each unique character in `s` as a key and the frequency of that character as the value.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters `a-z`, `s` is a non-empty input string with all characters processed, `memo` is a dictionary with each unique character in `s` as a key and the frequency of that character as the value, `result` is True. If there is at least one value in `memo` that is an odd number, `result` will be False. Otherwise, it will remain True after the loop executes.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function `func_1` reads an input string `s`, processes each character to calculate its frequency, and checks if all character frequencies are even. It then prints 'Yes' if all frequencies are even, and 'No' otherwise. The function does not accept any parameters and does not return any value.

