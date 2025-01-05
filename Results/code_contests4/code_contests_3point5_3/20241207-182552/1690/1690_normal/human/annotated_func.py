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
        
    #State of the program after the  for loop has been executed: `ans` holds the minimum value between the previous `ans` and the sum of all `a[j]` where `s[j]` is equal to `word[4]`, `be` is equal to `n`, `en` is decremented by the number of times the condition in the loop is met, `tem` is the sum of all `a[j]` where `s[j]` is equal to `word[4]`, `cur` is 3, and `s[j]` is equal to `word[i]` for the loop to execute.
    print(ans)
#Overall this is what the function does:Functionality: The function does not accept any parameters. It reads an integer `n`, a string `s`, a list of integers `a`, initializes variables, and then iterates through a series of loops to perform comparisons and calculations. It calculates the minimum sum of elements in `a` under certain conditions. Finally, it prints the calculated minimum sum. The function does not return any value.

