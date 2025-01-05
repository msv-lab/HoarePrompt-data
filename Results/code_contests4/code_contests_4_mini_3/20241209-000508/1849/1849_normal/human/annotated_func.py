#State of the program right berfore the function call: s is a string consisting of characters '(', ')', and '#' with length between 1 and 100,000, and contains at least one '#' character.
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
        
    #State of the program after the  for loop has been executed: `left` is the count of '(', `right` is the count of ')', `sh` is the count of '#' in `s`, `ans` is a list of size `sh` where the first `sh - 1` elements are `1` and the last element is `abs(right - sh - 1)`, `p` is the count of '#' processed. If at any point `right` is greater than `left`, the program exits without further execution.
    print(*ans, sep='\n')
#Overall this is what the function does:The function accepts a string `s` consisting of characters '(', ')', and '#' with a length between 1 and 100,000, and at least one '#' character. It counts the number of each character type, processes them in order, and checks if the number of ')' exceeds the number of '('. If at any point this condition is met, it prints -1 and exits. If the loop completes without exiting, it prints a list of integers derived from the counts of '#' processed, where the first `sh - 1` elements are `1` and the last element is `abs(right - sh - 1)`. The exact output depends on the arrangement of characters in the input string.

