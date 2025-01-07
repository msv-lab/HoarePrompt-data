#State of the program right berfore the function call: n, pos, l, r are integers such that 1 ≤ n ≤ 100, 1 ≤ pos ≤ n, 1 ≤ l ≤ r ≤ n.
def func():
    n, pos, l, r = map(int, input().split())
    ans = 0
    if (pos < l) :
        ans += l - pos
    #State of the program after the if block has been executed: *`n`, `pos`, `l`, `r`, `ans` are specific integers. If `pos` is less than `l`, then `ans` is set to `l - pos`. Otherwise, `ans` remains 0.
    if (pos > r) :
        ans += pos - r
    #State of the program after the if block has been executed: *`n`, `pos`, `l`, `r`, `ans` are specific integers. If `pos` is greater than `r`, then `ans` is set to `pos - r`. Otherwise, `ans` remains 0.
    ans += min(pos - 1, n - r) + max(0, l - 1)
    print(ans)
#Overall this is what the function does:The function accepts four integers `n`, `pos`, `l`, and `r` (where 1 ≤ n ≤ 100, 1 ≤ pos ≤ n, 1 ≤ l ≤ r ≤ n), calculates the minimum number of steps required to move the position `pos` within the range `[l, r]` on a circular list of size `n`, and prints the result. Specifically, it handles the following cases:
- If `pos` is less than `l`, it adds the distance from `pos` to `l` to the answer.
- If `pos` is greater than `r`, it adds the distance from `pos` to `r` to the answer.
- It always adds the minimum of `pos - 1` and `n - r` plus the maximum of `0` and `l - 1` to the answer.
This ensures that the position `pos` is moved within the range `[l, r]` with the minimum possible steps, considering both clockwise and counterclockwise directions. The function does not return any value but prints the calculated answer.

