#State of the program right berfore the function call: **Precondition**: **n and m are positive integers such that 1 ≤ n ≤ 2·10^5 and 1 ≤ m ≤ n. The list of colors of lightsabers contains n integers in the range {1, 2, ..., m}. The list of desired counts of Jedi Knights with lightsabers of each color contains m integers.**
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
        
    #State of the program after the loop has been executed: At the end of the loop, `n`, `m`, `b`, `s`, `l`, `ans`, and `t` remain the same as their initial values. The list `c` contains the counts of elements in list `a` such that the count of each element matches the corresponding element in list `b`. The index `r` is such that `r + 1` is not less than `n`.
    if (t > 0) :
        print(ans)
        exit()
    #State of the program after the if block has been executed: *At the end of the loop, `n`, `m`, `b`, `s`, `l`, `ans`, and `t` remain the same as their initial values. The list `c` contains the counts of elements in list `a` such that the count of each element matches the corresponding element in list `b`. The index `r` is such that `r + 1` is not less than `n`. Additionally, if `t` is greater than 0, the above conditions hold true.
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
        
    #State of the program after the loop has been executed: At the end of the loop, `n`, `m`, `b`, `s`, and `t` remain the same as their initial values. The list `c` contains the final counts of elements in list `a` such that the count of each element matches the corresponding element in list `b`. The index `r` is such that `r + 1` is not less than `n`. `l` is increased by the total number of loop iterations. If `c[a[l]]` is less than `b[a[l]]`, the loop breaks, and `ans` is updated to the minimum value between the current `ans` and `r - l + 1 - s`.
    print(ans)
#Overall this is what the function does:The function accepts input for the number of lightsabers and the desired counts of Jedi Knights with lightsabers of each color. It then checks if the list of colors of lightsabers can satisfy the desired counts. If it can, the function calculates and prints the minimum number of lightsabers that need to be bought to satisfy all counts. If the conditions are not met, it prints the last valid solution before breaking the loop.

