#State of the program right berfore the function call: s is a string of length at least 1, consisting of characters '(', ')' or '#'.**
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
        
    #State of the program after the  for loop has been executed: If the loop executes, the output state will be dependent on the input string `s` and the operations performed within the loop. The final values of `left`, `right`, `sh`, `ans`, `p`, `j`, and `i` will vary based on the content of `s` and the conditions met during the loop iterations. If the loop does not execute, the initial values of the variables will remain unchanged.
    print(*ans, sep='\n')
#Overall this is what the function does:The function takes an input string `s` containing characters '(', ')', or '#' and performs certain operations based on the counts of these characters. It calculates and adjusts the values of `left`, `right`, `sh`, `ans`, `p`, `j`, and `i` within a loop. If at any point during the loop `right` becomes greater than `left`, it prints -1 and exits. The final values of `ans` are printed. The function does not return any value.

