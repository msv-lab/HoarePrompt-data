#State of the program right berfore the function call: n is an integer between 1 and 100, pos, l, and r are integers such that 1 ≤ n ≥ pos ≥ 1, 1 ≤ l ≤ r ≤ n.
def func():
    n, pos, l, r = map(int, input().split())
    ans = 0
    if (pos < l) :
        ans += l - pos
    #State of the program after the if block has been executed: *`n` is an integer between 1 and 100, `pos` is an integer between 1 and `n`, `l` is an integer between 1 and `n`, `r` is an integer between `l` and `n`, `ans` is `l - pos` if `pos` is less than `l`. Otherwise, `ans` remains 0.
    if (pos > r) :
        ans += pos - r
    #State of the program after the if block has been executed: *`n` is an integer between 1 and 100, `pos` is an integer between 1 and `n`, `l` is an integer between 1 and `n`, `r` is an integer between `l` and `n`. If `pos` is greater than `r`, `ans` is `pos - r`. Otherwise, `ans` remains `l - pos` if `pos` is less than `l`, otherwise `ans` remains 0.
    ans += min(pos - 1, n - r) + max(0, l - 1)
    print(ans)
#Overall this is what the function does:The function accepts four integers `n`, `pos`, `l`, and `r` and calculates a value `ans` based on the positions relative to `l` and `r`. Specifically, it adds the minimum distance from `pos` to `l` and from `pos` to `r`, ensuring these distances do not go beyond the boundaries of 1 and `n`. Finally, it prints the computed value `ans`.

