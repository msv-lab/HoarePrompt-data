#State of the program right berfore the function call: w is a string consisting of lowercase letters with a length between 1 and 100 inclusive.
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters with a length between 1 and 100; `s` is a string consisting of lowercase letters; `memo` is a dictionary where each key is a character from `s` and its value is the count of occurrences of that character in `s`.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string consisting of lowercase letters with a length between 1 and 100, `s` is a string consisting of lowercase letters, `memo` is a dictionary where each key is a character from `s` and its value is the count of occurrences of that character in `s`, and `result` is True if all counts in `memo` are even; otherwise, `result` is False.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase letters (with a length between 1 and 100), counts the occurrences of each character, and checks if all characters appear an even number of times. It prints 'Yes' if all counts are even and 'No' if any count is odd. The function does not return a value; it only prints the result.

