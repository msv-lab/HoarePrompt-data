#State of the program right berfore the function call: s is a string of length between 1 and 100,000, consisting only of the characters '(', ')' and '#', and contains at least one '#' character.
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
        
    #State of the program after the  for loop has been executed: `left` is the count of '(', `right` is the count of ')', `sh` is the count of '#', `ans` is a list of size `sh` with `sh - 1` ones followed by `abs(right - sh - 1)`, and `p` is the count of processed '#' characters. If `right` is ever greater than `left`, -1 will be printed and the program will terminate.
    print(*ans, sep='\n')
#Overall this is what the function does:The function processes a string `s` consisting of the characters '(', ')' and '#' to determine the balance of parentheses. It counts the instances of each character and constructs an answer list based on the counts of '#' characters and the imbalance between '(' and ')'. If at any point the number of ')' exceeds the number of '(', the function prints -1 and exits. Finally, it prints the constructed answer list, which contains values based on the counts of '#' and the difference between the counts of ')' and '#' characters. The function does not return a value; it outputs results directly.

