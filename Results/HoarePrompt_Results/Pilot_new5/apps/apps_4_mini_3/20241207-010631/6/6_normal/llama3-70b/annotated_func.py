#State of the program right berfore the function call: n is an integer between 1 and 100, pos is an integer between 1 and n, l is an integer between 1 and n, and r is an integer between l and n such that 1 ≤ n, 1 ≤ pos, 1 ≤ l ≤ r ≤ n.
def func():
    n, pos, l, r = map(int, input().split())
    ans = 0
    if (pos < l) :
        ans += l - pos
    #State of the program after the if block has been executed: *`n` is an integer between 1 and 100; `pos` is an integer between 1 and `n`; `l` is an integer between 1 and `n`; `r` is an integer between `l` and `n`; `ans` is a positive integer equal to the previous value of `ans` plus `l - pos` if `pos` is less than `l`.
    if (pos > r) :
        ans += pos - r
    #State of the program after the if block has been executed: *`n` is an integer between 1 and 100; `pos` is an integer between 1 and `n`; `l` is an integer between 1 and `n`; `r` is an integer between `l` and `n`; `ans` is a positive integer. If `pos` is greater than `r`, then `ans` is updated to the previous value of `ans` plus `pos - r`.
    ans += min(pos - 1, n - r) + max(0, l - 1)
    print(ans)
#Overall this is what the function does:The function accepts four integer parameters: `n` (between 1 and 100), `pos` (between 1 and `n`), `l` (between 1 and `n`), and `r` (between `l` and `n`). It calculates the total distance that `pos` needs to move to fit within the range `[l, r]`. The result is printed but not returned, and the calculation includes cases where `pos` is less than `l`, greater than `r`, in addition to adjustments based on the minimum and maximum values to determine how far `pos` is from the bounds defined by `l` and `r`.

