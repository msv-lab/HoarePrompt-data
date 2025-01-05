#State of the program right berfore the function call: s is a string of length between 1 and 100,000 inclusive, consisting of characters '(', ')' and '#', and it is guaranteed that s contains at least one '#' character.
def func():
    rstr = lambda : stdin.readline().strip()
    s = rstr()
    left, right, sh = s.count('('), s.count(')'), s.count('#')
    ans, p = [1] * (sh - 1) + [abs(right - sh - 1)], 0
    for (j, i) in enumerate(s):
        if i == '(':
            left -= 1
        elif i == ')':
            right -= 1
        else:
            right -= ans[p]
            p += 1
        
        if right > left:
            print(-1)
            exit()
        
    #State of the program after the  for loop has been executed: `s` is a string of length between 1 and 100,000; `left` is the count of unmatched '(', `right` is the count of unmatched ')', `sh` is the count of '#' after processing all characters in `s`, `ans` is either [0] or a list of 1's followed by a computed value based on `abs(right - sh - 1)`, `p` is the count of '#' processed.
    print(*ans, sep='\n')
#Overall this is what the function does:The function accepts a string `s` consisting of characters '(', ')', and '#' and processes it to determine how many '#' can be replaced to ensure that the string can represent a valid parentheses configuration. If it finds that the number of unmatched ')' exceeds the number of unmatched '(', it prints -1 and exits. Finally, it prints a list of integers representing valid replacements for each '#' character or computes a single value based on the unmatched counts. The function does not return a boolean value but instead outputs the results directly.

