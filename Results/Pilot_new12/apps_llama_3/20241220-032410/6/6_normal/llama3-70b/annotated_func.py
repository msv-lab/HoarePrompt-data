#State of the program right berfore the function call: n, pos, l, and r are integers such that 1 <= n <= 100, 1 <= pos <= n, 1 <= l <= r <= n.
def func():
    n, pos, l, r = map(int, input().split())
    ans = 0
    if (pos < l) :
        ans += l - pos
    #State of the program after the if block has been executed: `n`, `pos`, `l`, and `r` are integers, and `ans` is 0 if `pos` is not less than `l`. If `pos` is less than `l`, then `ans` is `l - pos`.
    if (pos > r) :
        ans += pos - r
    #State of the program after the if block has been executed: `n`, `pos`, `l`, and `r` are integers. If `pos` is not less than `l`, `ans` is 0. If `pos` is less than `l`, then `ans` is `l - pos`. Additionally, if `pos` is greater than `r`, `ans` is updated to `pos - r`. Otherwise, `ans` remains as previously determined by the relationship between `pos` and `l`.
    ans += min(pos - 1, n - r) + max(0, l - 1)
    print(ans)
#Overall this is what the function does:The function calculates and returns the minimum number of moves required to reach a target position within a given range, considering the constraints of the input parameters `n`, `pos`, `l`, and `r`. The function accepts these parameters as integers, where `1 <= n <= 100`, `1 <= pos <= n`, and `1 <= l <= r <= n`. It then determines the minimum distance to move the position `pos` within the range `[l, r]` and to the closest boundary of the range `[1, n]`, accounting for the minimum number of moves required to adjust `pos` to be within the range `[l, r]` and to move towards the closest end of the range `[1, n]`. The function returns the total number of moves required, considering all potential edge cases, including when `pos` is less than `l`, greater than `r`, or within the range `[l, r]`.

