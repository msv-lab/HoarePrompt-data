#State of the program right berfore the function call: s is a string of length between 1 and 10^5, containing only the characters '(', ')', and '#'.**
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
        
    #State of the program after the  for loop has been executed: At the end of the loop, `s` is a string of length at least 1, `left`, `right`, `sh`, `ans`, `p`, and `j` are integers. If `right` is greater than `left`, the loop exits immediately. Otherwise, the loop continues with the updated values of the variables as described in the loop code.
    print(*ans, sep='\n')
#Overall this is what the function does:Functionality: The function `func` reads a string `s` from the input and performs operations based on the counts of '(', ')', and '#' characters in the string. It calculates certain values and updates variables accordingly within a loop. If at any point during the loop, the count of ')' exceeds the count of '(', the function prints -1 and exits the loop. Finally, the function prints the calculated values as output. The function does not return any value.

