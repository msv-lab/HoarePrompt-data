#State of the program right berfore the function call: w is a string consisting of lowercase letters (`a`-`z`) with a length between 1 and 100 inclusive.
def func_1():
    s = raw_input()
    memo = {}
    for c in s:
        if c not in memo:
            memo[c] = 0
        
        memo[c] += 1
        
    #State of the program after the  for loop has been executed: `w` is a string of lowercase letters, `s` is a non-empty string from the user, `memo` is a dictionary where each key is a unique character from `s` and its corresponding value is the count of occurrences of that character in `s`.
    result = True
    for x in memo.values():
        if x % 2 > 0:
            result = False
            break
        
    #State of the program after the  for loop has been executed: `w` is a string of lowercase letters, `s` is a non-empty string from the user, `memo` is a dictionary with character counts from `s`, `result` is False if any character in `s` has an odd count, otherwise `result` is True.
    print('Yes' if result else 'No')
#Overall this is what the function does:The function accepts a string `s` consisting of lowercase letters, counts the occurrences of each character, and checks if all characters have even counts. If all characters have even counts, it prints 'Yes'; otherwise, it prints 'No'. If the string is empty or contains only odd counts, the function will still handle it correctly by returning 'No' in such cases.

