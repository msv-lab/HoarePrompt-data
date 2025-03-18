#State of the program right berfore the function call: n, pos, l, and r are integers such that 1 <= n <= 100, 1 <= pos <= n, 1 <= l <= r <= n.
def func():
    n, pos, l, r = map(int, input().split())
    ans = 0
    if (pos < l) :
        ans += l - pos
    #State of the program after the if block has been executed: `n` equals the first input integer, `l` equals the third input integer, `r` equals the fourth input integer, if `pos` is less than `l`, then `ans` equals `l - pos` and `pos` is less than `l`. If `pos` is not less than `l`, then the state of `ans` and `pos` remains unchanged.
    if (pos > r) :
        ans += pos - r
    #State of the program after the if block has been executed: `n` equals the first input integer, `l` equals the third input integer, `r` equals the fourth input integer. If `pos` is less than `l`, then `ans` equals `l - pos`. If `pos` is not less than `l` and not greater than `r`, then the state of `ans` and `pos` remains unchanged. If `pos` is greater than `r`, then `ans` has been increased by `pos - r`; if `pos` was initially less than `l`, then the new `ans` equals `l - r`; if `pos` was not less than `l`, then `ans` equals its previous value (if any) plus `pos - r`.
    ans += min(pos - 1, n - r) + max(0, l - 1)
    print(ans)
#Overall this is what the function does:The function accepts four integer parameters `n`, `pos`, `l`, and `r` as input from the user, calculates a value `ans` based on their relationship, and prints the calculated value, where `ans` is incremented by the distance from `pos` to `l` if `pos` is less than `l`, by the distance from `pos` to `r` if `pos` is greater than `r`, and by the minimum of `pos - 1` and `n - r` plus the maximum of `0` and `l - 1`.

