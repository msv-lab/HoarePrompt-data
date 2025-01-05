#State of the program right berfore the function call: w is a string consisting of lowercase letters.**
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: w` is a string consisting of lowercase letters, `s` is an input string with no characters left, `memo` is a dictionary with each unique character in `s` as a key and the corresponding frequency of that character as the value.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is an input string with no characters left, `memo` is a dictionary with key-value pairs where the values are all even, `result` is True
    print('Yes' if result else 'No')
#Overall this is what the function does:The function func_1 reads an input string `s`, creates a dictionary `memo` with the frequency of each unique character in `s`, and then checks if all the frequencies are even. If all frequencies are even, it prints 'Yes'; otherwise, it prints 'No'. The function does not accept any parameters and does not return any value.

