#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, pos is an integer such that 1 ≤ pos ≤ n, and l and r are integers such that 1 ≤ l ≤ r ≤ n.
def func():
    n, pos, l, r = map(int, input().split())
    ans = 0
    if (pos < l) :
        ans += l - pos
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ n ≤ 100; `pos` is an integer such that 1 ≤ pos ≤ n; `l` is an integer such that 1 ≤ l ≤ n; `r` is an integer such that 1 ≤ l ≤ r ≤ n; `ans` is `l - pos` if `pos < l`, otherwise `ans` remains 0.
    if (pos > r) :
        ans += pos - r
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ n ≤ 100; `pos` is an integer such that 1 ≤ pos ≤ n; `l` is an integer such that 1 ≤ l ≤ n; `r` is an integer such that 1 ≤ l ≤ r ≤ n; `ans` is `pos - r` if `pos` is greater than `r`, otherwise `ans` remains 0.
    ans += min(pos - 1, n - r) + max(0, l - 1)
    print(ans)
#Overall this is what the function does:The function `func` accepts four parameters: `n`, `pos`, `l`, and `r`. It processes these parameters according to specific conditions and calculates a value stored in `ans`. After executing the necessary conditions, it prints the value of `ans`. The state of the program after the function concludes is that `ans` contains a value determined by the following logic:
- If `pos` is less than `l`, `ans` is incremented by `l - pos`.
- If `pos` is greater than `r`, `ans` is incremented by `pos - r`.
- Finally, `ans` is adjusted by adding `min(pos - 1, n - r)` and `max(0, l - 1)`.

The function does not return a boolean value as suggested in the original annotation. Instead, it prints the computed value of `ans`. The function covers all potential edge cases where `pos` is within the range `[l, r]`, exactly at `l` or `r`, or outside this range.

