#State of the program right berfore the function call: n, pos, l, and r are integers such that 1 <= n <= 100, 1 <= pos <= n, 1 <= l <= r <= n.
def func():
    n, pos, l, r = map(int, input().split())
    ans = 0
    if (pos < l) :
        ans += l - pos
    #State of the program after the if block has been executed: *`n` equals the first input integer, `pos` equals the second input integer, `l` equals the third input integer, `r` equals the fourth input integer, with the constraints `1 <= n <= 100`, `1 <= pos <= n`, `1 <= l <= r <= n` that may or may not be satisfied. If `pos` is less than `l`, then `ans` equals `l - pos`. If `pos` is not less than `l`, then the state of `ans` is unchanged, remaining as 0.
    if (pos > r) :
        ans += pos - r
    #State of the program after the if block has been executed: `n` equals the first input integer, `pos` equals the second input integer, `l` equals the third input integer, `r` equals the fourth input integer, with the constraints `1 <= n <= 100`, `1 <= pos <= n`, `1 <= l <= r <= n` that may or may not be satisfied. If `pos` is less than `l`, then `ans` equals `l - pos`. If `pos` is not less than `l` and `pos` is less than or equal to `r`, then `ans` equals 0. If `pos` is greater than `r`, then `ans` equals `pos - r`.
    ans += min(pos - 1, n - r) + max(0, l - 1)
    print(ans)
#Overall this is what the function does:The function accepts four integer parameters `n`, `pos`, `l`, and `r` as input, where `n` represents the total length of a sequence, `pos` represents a position within this sequence, and `l` and `r` define a range within the sequence. The function calculates and returns the minimum number of steps required to move `pos` into the range `[l, r]`. This calculation includes two components: the steps needed to move `pos` into the range `[l, r]` directly (either by moving `pos` to `l` if `pos` is less than `l`, or by moving `pos` to `r` if `pos` is greater than `r`), and the steps needed to adjust `pos` to account for the full range between `1` and `n`, considering the boundaries of `l` and `r` within this range. The function prints the total number of steps as its output. The function's calculations cover all potential edge cases, including when `pos` is within the range `[l, r]`, when `pos` is less than `l`, and when `pos` is greater than `r`, ensuring that the returned value accurately reflects the minimum steps required to align `pos` with the specified range within the sequence of length `n`.

