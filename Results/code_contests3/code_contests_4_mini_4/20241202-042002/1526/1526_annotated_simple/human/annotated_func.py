#State of the program right berfore the function call: w is a string consisting of lowercase letters with a length between 1 and 100.
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters with a length between 1 and 100; `s` is a string with at least 1 character; `memo` contains keys for each unique character in `s` with their corresponding values representing the count of occurrences of each character in `s`.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters, `s` is a string with at least 1 character, `memo` is a non-empty dictionary containing keys for each unique character in `s`, and `result` is True if all counts are even, or False if at least one count is odd.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase letters and checks if every character in the string occurs an even number of times. It prints 'Yes' if all characters have even occurrences and 'No' if at least one character has an odd occurrence. The function does not return any value.

