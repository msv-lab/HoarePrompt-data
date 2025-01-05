#State of the program right berfore the function call: w is a string consisting of lowercase letters with a length between 1 and 100 inclusive.
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string of lowercase letters, `s` is a non-empty string, `memo` is a dictionary containing the frequency of each character in `s`.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string of lowercase letters, `s` is a non-empty string, `memo` is a dictionary containing the frequency of each character in `s`, and `result` is False if any value in `memo` is odd; True if all values in `memo` are even.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase letters and checks if every character in the string appears an even number of times. It prints 'Yes' if all characters have even frequencies and 'No' if any character has an odd frequency. The function does not return a value.

