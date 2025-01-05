#State of the program right berfore the function call: s is a string of length at least 1 containing only characters '(', ')' and '#'.**
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
        
    #State of the program after the  for loop has been executed: If the loop executes until the end, the final output state will be that `s` is a string of length at least 3 containing only characters '(', ')' and '#', `left` and `right` are integers where `right` is greater than `left`, `sh` is the count of '#', `ans` is a list with elements calculated based on the previous counts, `p` is at least 2, `j` is the index of the last character in the string. If `right` is greater than `left` at any point during the loop, the program will print -1 and exit.
    print(*ans, sep='\n')
#Overall this is what the function does:The function `func` reads a string `s` from input, processes it by counting the occurrences of '(', ')', and '#'. It then iterates through the characters in `s`, updating the counts accordingly. If at any point during the iteration `right` becomes greater than `left`, the function prints -1 and exits. Finally, the function prints the elements of the list `ans` separated by newlines. The function does not return any specific output based on the input string `s`.

