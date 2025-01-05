#State of the program right berfore the function call: w is a string consisting of lowercase letters with a length between 1 and 100, inclusive.
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string of lowercase letters with a length between 1 and 100; `s` is a non-empty string; `memo` is a dictionary where each key is a character from `s` and each value is the count of occurrences of that character in `s`.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string of lowercase letters with a length between 1 and 100, `s` is a non-empty string, `memo` is a dictionary with at least one entry, and `result` is False if any character count was odd, otherwise True.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function accepts a string input from the user consisting of lowercase letters. It counts the occurrences of each character in the string and checks if all characters have even occurrences. The function prints 'Yes' if all characters occur an even number of times, and 'No' if at least one character occurs an odd number of times. There are no parameters for the function, and it directly interacts with the user for input.

