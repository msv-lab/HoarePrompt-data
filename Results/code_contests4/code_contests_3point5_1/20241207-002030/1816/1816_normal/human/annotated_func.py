#State of the program right berfore the function call: n and m are integers such that 1 ≤ n ≤ 2·10^5, 1 ≤ m ≤ n. The input sequence of colors of lightsabers of Jedi Knights is represented by a list of n integers in the range {1, 2, ..., m}. The desired counts of Jedi Knights with lightsabers of each color are represented by a list of m integers.**
def func():
    n, m = map(int, raw_input().split())
    a = map(lambda x: int(x) - 1, raw_input().split())
    b = map(int, raw_input().split())
    s = sum(b)
    c = [0] * m
    l, r = 0, -1
    ans = -1
    t = m
    while t > 0 and r + 1 < n:
        r += 1
        
        c[a[r]] += 1
        
        if c[a[r]] == b[a[r]]:
            t -= 1
        
    #State of the program after the loop has been executed: `t` is 0, `r` is equal to `n - 1`, `c` has been updated based on the values in list `a`, the loop has finished execution.
    if (t > 0) :
        print(ans)
        exit()
    #State of the program after the if block has been executed: *`t` is 0, `r` is equal to `n - 1`, `c` has been updated based on the values in list `a`, the loop has finished execution, and `t` is greater than 0.
    ans = r - l + 1 - s
    while l <= r:
        c[a[l]] -= 1
        
        while r + 1 < n and c[a[l]] < b[a[l]]:
            r += 1
            c[a[r]] += 1
        
        if c[a[l]] < b[a[l]]:
            break
        
        l += 1
        
        ans = min(ans, r - l + 1 - s)
        
    #State of the program after the loop has been executed: `t` is 0, `r` is equal to `n`, `c` has been updated based on the final values in list `a`, `t` is greater than 0, `ans` is calculated, `l` is greater than `r`, `c[a[l]]` has been decremented by 1, If `c[a[l]]` is less than `b[a[l]]`, then we break out of the most internal loop or if statement, `l` is incremented by 1
    print(ans)
#Overall this is what the function does:The function `func` reads input data about the colors of lightsabers of Jedi Knights and the desired counts of Jedi Knights with lightsabers of each color. It then processes this data to determine the optimal distribution of lightsabers among the Jedi Knights based on the desired counts. The function calculates and prints the final answer.

