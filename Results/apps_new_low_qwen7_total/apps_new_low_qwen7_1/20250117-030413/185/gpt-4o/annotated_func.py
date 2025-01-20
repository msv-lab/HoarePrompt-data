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
        #State of the program after the if block has been executed: *`l`, `r`, and `a` are integers where `l` and `r` satisfy the condition `l >= r`. If `r < l`, then `r` is updated to `R + \min(A, L - R)` and `a` is updated to `A - \min(A, L - R)`. Otherwise, no change is made to `r` and `a`.
    #State of the program after the if-else block has been executed: *`l`, `r`, and `a` are integers. If `l < r`, then `l` is increased by the minimum value between `a` and `r - l`, `a` remains unchanged (since it is less than or equal to 0), and `r` remains the same as the initial value. Otherwise (`r >= l`), `r` is updated to `r + \min(a, l - r)` and `a` is updated to `a - \min(a, l - r)`.
    max_team_size = l + r + a // 2 * 2
    if (max_team_size % 2 != 0) :
        max_team_size -= 1
    #State of the program after the if block has been executed: *`l`, `r`, `a` are the initial values. `max_team_size` is `l + r + a`. If `max_team_size` is odd, then `max_team_size` is adjusted to be even by subtracting 1 from it. The final value of `max_team_size` will be either the original value minus 1 (if it was odd) or the original value (if it was already even).
    print(max_team_size)
#Overall this is what the function does:The function accepts three parameters `l`, `r`, and `a`, which are non-negative integers. It first adjusts the values of `l` and `r` based on their relative sizes and the value of `a`. Specifically, if `l < r`, it increases `l` by the minimum value between `a` and `r - l`. If `r < l`, it increases `r` by the minimum value between `a` and `l - r`. After adjusting `l` and `r`, it updates `a` to be `a` minus the value used for adjustment. Finally, it calculates `max_team_size` as `l + r + a`, ensuring that `max_team_size` is even by subtracting 1 if necessary. The function then prints the final value of `max_team_size`.

