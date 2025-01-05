#State of the program right berfore the function call: **
def func():
    rstr = lambda : stdin.readline().strip()
    rints = lambda : [int(x) for x in stdin.readline().split()]
    n, s, a, ans, word = int(input()), rstr(), rints(), float('inf'), 'hard'
    for i in range(4):
        be, en, tem = 0, n, 0
        
        cur = 0
        
        for j in range(n):
            if cur == i:
                break
            elif s[j] == word[cur]:
                cur += 1
            be += 1
        
        cur = 3
        
        for j in range(n - 1, -1, -1):
            if cur == i:
                break
            elif s[j] == word[cur]:
                cur -= 1
            en -= 1
        
        for j in range(be, en):
            if s[j] == word[i]:
                tem += a[j]
        
        ans = min(ans, tem)
        
    #State of the program after the  for loop has been executed: Output State: `j`, `be`, `en`, `cur`, `tem`, `i` are integers, `s` is a list, `word` is a string, `a` is a list of integers, `ans` is updated to the minimum value of `tem` calculated in each iteration of the loop.
    print(ans)
#Overall this is what the function does:The function defines lambda functions for reading input, initializes variables, and then iterates through a nested loop to manipulate and calculate values. It updates the `ans` variable to the minimum of `tem` in each iteration. Finally, it prints the minimum calculated value of `tem`. The function does not accept any parameters and does not return anything.

