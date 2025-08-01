#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, pos is an integer such that 1 ≤ pos ≤ n, and l and r are integers such that 1 ≤ l ≤ r ≤ n.
def func():
    n, pos, l, r = map(int, input().split())
    ans = 0
    if (pos < l) :
        ans += l - pos
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ n ≤ 100, `pos` is an integer such that 1 ≤ pos < l ≤ n, `l` is an integer such that 1 ≤ l ≤ r ≤ n, `r` is an integer such that 1 ≤ l ≤ r ≤ n; `ans` is equal to `l - pos` whenever `pos` is less than `l`.
    if (pos > r) :
        ans += pos - r
    #State of the program after the if block has been executed: *`n`, `pos`, `l`, and `r` are integers such that 1 ≤ n ≤ 100, 1 ≤ pos < l ≤ n, 1 ≤ l ≤ r ≤ n. If `pos` is greater than `r`, then `ans` is equal to the initial value of `ans` plus `(pos - r)`.
    ans += min(pos - 1, n - r) + max(0, l - 1)
    print(ans)
#Overall this is what the function does:The function calculates an integer result based on the parameters `n`, `pos`, `l`, and `r`, representing boundaries and a current position within a range of numbers from 1 to `n`. It determines how far `pos` is from the defined boundaries, incrementing the result (`ans`) accordingly based on whether `pos` lies outside the range defined by `l` and `r`. Specifically, if `pos` is less than `l`, it adds the difference to `ans`. If `pos` is greater than `r`, it also adds the difference to `ans`. Then, it adds the smaller of `pos - 1` or `n - r`, which accounts for the distance to the start or the end of the range, as well as the maximum of `0` or `l - 1`, which ensures the result accounts for positions before `l`. The function ultimately prints out the computed value of `ans`, which summarizes how far the position is from optimal boundaries, including edge cases where the `pos` is at extreme ends or exactly on the boundaries.

