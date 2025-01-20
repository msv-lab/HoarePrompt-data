#State of the program right berfore the function call: l, r, and a are non-negative integers such that 0 ≤ l, r, a ≤ 100.
def func():
    l, r, a = map(int, input().split())
    if (l < r) :
        l += min(a, r - l)

a -= min(a, r - l)
    else :
        if (r < l) :
            r += min(a, l - r)

a -= min(a, l - r)
        #State of the program after the if block has been executed: *`l`, `r`, and `a` are integers. If `r` is less than `l`, then `l` is `L`, `r` is `R + M`, and `a` is `A - M`. Since there is no else part, no other changes occur in these variables.
    #State of the program after the if-else block has been executed: *`l`, `r`, and `a` are integers. If `l` is less than `r`, then `l` is increased by the minimum of `a` and `r-l`, and `a` is 0. If `r` is less than `l`, then `l` is `L`, `r` is `R + M`, and `a` is `A - M`.
    max_team_size = l + r + a // 2 * 2
    if (max_team_size % 2 != 0) :
        max_team_size -= 1
    #State of the program after the if block has been executed: *`l`, `r`, and `a` are integers. If `max_team_size` (which is `l + r + a`) is an odd number, the function does not change the values of `l`, `r`, and `a`. Since there is no else part, the postcondition remains the same as the precondition.
    print(max_team_size)
#Overall this is what the function does:The function processes three non-negative integer values `l`, `r`, and `a` (where \(0 \leq l, r, a \leq 100\)) obtained from user input. It first adjusts the values of `l` and `r` based on their relative sizes and the value of `a`. Specifically, if `l < r`, then `l` is increased by the minimum of `a` and `r - l`. If `r < l`, then `r` is adjusted to `r + min(a, l - r)`, and `a` is updated accordingly. In both cases, `a` is reduced by the minimum amount used for adjustment.

After adjusting `l` and `r`, the function calculates the maximum possible team size (`max_team_size`) as `l + r + a // 2 * 2`. If this calculated value is odd, `max_team_size` is decremented by 1 to ensure it is even. Finally, the function prints the computed `max_team_size`.

Potential edge cases include when `a` is zero or when `l` equals `r`. If `a` is zero, the adjustments to `l` and `r` will not occur, and the final `max_team_size` will simply be the sum of `l`, `r`, and any remaining `a` (which will be zero). When `l` equals `r`, the adjustments will be made based on the value of `a`, and the final `max_team_size` will be adjusted accordingly.

