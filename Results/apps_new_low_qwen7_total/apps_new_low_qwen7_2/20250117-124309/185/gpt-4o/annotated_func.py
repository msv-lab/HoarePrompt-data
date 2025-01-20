#State of the program right berfore the function call: l, r, and a are non-negative integers such that 0 <= l, r, a <= 100.
def func():
    l, r, a = map(int, input().split())
    if (l < r) :
        l += min(a, r - l)

a -= min(a, r - l)
    else :
        if (r < l) :
            r += min(a, l - r)

a -= min(a, l - r)
        #State of the program after the if block has been executed: *`l` is `l_input`, `r` is `r_input`, `a` is `a_input`. If `r < l` is true, then `r` is updated to `r_input + a_input` and `a` is set to 0. Since there is no else part, these changes only occur when `r < l` is true.
    #State of the program after the if-else block has been executed: `l` is `l_input + min(a_input, r_input - l_input)` and `a` is `a_input - min(a_input, r_input - l_input)`, and `r` is `r_input` if `l < r`. If `r < l`, then `r` is updated to `r_input + a_input` and `a` is set to 0.
    max_team_size = l + r + a // 2 * 2
    if (max_team_size % 2 != 0) :
        max_team_size -= 1
    #State of the program after the if block has been executed: *`l` is `l_input + min(a_input, r_input - l_input)`, `a` is `a_input - min(a_input, r_input - l_input)`, `r` is `r_input` if `l < r` and 0 otherwise, and `max_team_size` is `l + r + a`. If `max_team_size` is an odd number, then `max_team_size` is adjusted to the nearest even number. Otherwise, `max_team_size` remains unchanged.
    print(max_team_size)
#Overall this is what the function does:The function accepts three parameters `l`, `r`, and `a`, which are non-negative integers such that \(0 \leq l, r, a \leq 100\). It adjusts the values of `l` and `r` based on the value of `a` and then calculates the maximum team size. Specifically, it ensures that `l` and `r` are updated to their closest reachable values given the constraint that `a` can be used to increase either `l` or `r` by at most `a`. If `r < l`, `r` is updated to `r + a` and `a` is set to 0. Otherwise, `l` is increased by the minimum of `a` and the difference between `r` and `l`. After updating `l` and `r`, the function calculates `max_team_size` as the sum of `l`, `r`, and half of `a` rounded down to the nearest integer, adjusting `max_team_size` to be even if necessary. Finally, it prints the calculated `max_team_size`. Potential edge cases include scenarios where `a` is exactly equal to the difference between `l` and `r`, and the case where `r < l`, in which case `r` is updated to `r + a` and `a` is reset to 0.

