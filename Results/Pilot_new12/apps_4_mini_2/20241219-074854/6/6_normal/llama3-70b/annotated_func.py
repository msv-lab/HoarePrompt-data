#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100), pos is an integer (1 ≤ pos ≤ n), l and r are integers such that 1 ≤ l ≤ r ≤ n, representing the segment of tabs that need to remain opened.
def func():
    n, pos, l, r = map(int, input().split())
    ans = 0
    if (pos < l) :
        ans += l - pos
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 100), `pos` is an integer (1 ≤ pos ≤ n), `l` is an integer (1 ≤ l ≤ r), `r` is an integer (l ≤ r ≤ n), and `ans` is a positive integer equal to `l - pos` when `pos` is less than `l`. There is no else part, so no other changes are made to `ans` when `pos` is greater than or equal to `l`.
    if (pos > r) :
        ans += pos - r
    #State of the program after the if block has been executed: *`n`, `pos`, `l`, `r` are integers such that 1 ≤ n ≤ 100, 1 ≤ pos ≤ n, 1 ≤ l ≤ r, and l ≤ r ≤ n. If `pos` is greater than `r`, then `ans` is updated to its original value plus `(pos - r)`. If `pos` is less than or equal to `r`, the value of `ans` remains unchanged.
    ans += min(pos - 1, n - r) + max(0, l - 1)
    print(ans)
#Overall this is what the function does:The function computes the number of tab closures required based on the current position `pos` relative to the boundaries defined by `l` and `r`. It does not take parameters explicitly but reads values for `n`, `pos`, `l`, and `r` from input. The function calculates the value of `ans`, which represents the total number of tabs that need to be closed, considering three conditions: if `pos` is less than `l`, if `pos` is greater than `r`, and the number of tabs that must be closed to the left and right of the open segment defined by `l` and `r`. The function finally prints the calculated `ans`. Note that while the function has checks for `pos` being less than `l` and greater than `r`, it does not handle cases where `pos` is equal to `l` or `r`, which means that no adjustments need to be made when `pos` lies exactly on these boundaries. Additionally, the function does not validate inputs beyond the assumptions made in the comments, which could lead to unexpected behavior if inputs fall outside the specified constraints.

