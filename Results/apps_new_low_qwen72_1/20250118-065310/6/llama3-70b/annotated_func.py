#State of the program right berfore the function call: n, pos, l, r are integers such that 1 ≤ n ≤ 100, 1 ≤ pos ≤ n, 1 ≤ l ≤ r ≤ n.
def func():
    n, pos, l, r = map(int, input().split())

ans = 0
    if (pos < l) :
        ans += l - pos
    #State of the program after the if block has been executed: *`n`, `pos`, `l`, `r` are integers such that 1 ≤ `n` ≤ 100, 1 ≤ `pos` ≤ `n`, 1 ≤ `l` ≤ `r` ≤ `n`. If `pos` < `l`, `ans` is set to `l - pos`. Otherwise, `ans` remains 0.
    if (pos > r) :
        ans += pos - r
    #State of the program after the if block has been executed: *`n`, `pos`, `l`, `r` are integers such that 1 ≤ `n` ≤ 100, 1 ≤ `pos` ≤ `n`, 1 ≤ `l` ≤ `r` ≤ `n`. If `pos` < `l`, `ans` is set to `l - pos`. If `pos` > `r`, `ans` is set to `pos - r`. Otherwise, `ans` remains 0.
    ans += min(pos - 1, n - r) + max(0, l - 1)

print(ans)
#Overall this is what the function does:The function `func` reads four integers `n`, `pos`, `l`, and `r` from the input, where `1 ≤ n ≤ 100`, `1 ≤ pos ≤ n`, and `1 ≤ l ≤ r ≤ n`. It calculates a value `ans` based on the following rules:
- If `pos` is less than `l`, `ans` is increased by `l - pos`.
- If `pos` is greater than `r`, `ans` is increased by `pos - r`.
- `ans` is further increased by `min(pos - 1, n - r) + max(0, l - 1)`.

The final value of `ans` is printed. The function does not return any value. After the function concludes, `ans` represents the calculated result based on the input parameters.

