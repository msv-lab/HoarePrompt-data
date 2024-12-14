#State of the program right berfore the function call: n is an integer between 1 and 100, pos is an integer such that 1 <= pos <= n, l and r are integers such that 1 <= l <= r <= n.
def func():
    n, pos, l, r = map(int, input().split())
    ans = 0
    if (pos < l) :
        ans += l - pos
    #State of the program after the if block has been executed: *`n` is an integer between 1 and 100. If `pos` is less than `l`, then `ans` is equal to `l - pos`. If `pos` is greater than or equal to `l`, `ans` remains 0.
    if (pos > r) :
        ans += pos - r
    #State of the program after the if block has been executed: *`n` is an integer between 1 and 100. If `pos` is greater than `r` and less than `l`, then `ans` is equal to `l - pos + (pos - r)`; if `pos` is greater than or equal to `l`, then `ans` remains 0.
    ans += min(pos - 1, n - r) + max(0, l - 1)
    print(ans)
#Overall this is what the function does:The function accepts four integers `n`, `pos`, `l`, and `r` via user input, where `n` is between 1 and 100, `pos` is between 1 and `n`, and `l` and `r` are such that `1 <= l <= r <= n`. It calculates a value `ans` based on the position of `pos` relative to `l` and `r`, updating `ans` based on specific conditions. It then prints the final value of `ans`, which represents the total distance or adjustments needed to fit the `pos` within the boundaries defined by `l` and `r`, considering also how far `pos` is from the start and end limits of the range. The function does not return any value; it only prints the result.

