#State of the program right berfore the function call: n is a positive integer representing the number of tabs (1 ≤ n ≤ 100), pos is an integer representing the current position of the cursor (1 ≤ pos ≤ n), l is a positive integer representing the left index of the segment to keep open (1 ≤ l ≤ r ≤ n), and r is a positive integer representing the right index of the segment to keep open (1 ≤ r ≤ n).
def func():
    n, pos, l, r = map(int, input().split())
    ans = 0
    if (pos < l) :
        ans += l - pos
    #State of the program after the if block has been executed: *`n` is an input positive integer (1 ≤ n ≤ 100), `pos` is an input integer (1 ≤ pos ≤ n), `l` is an input positive integer (1 ≤ l ≤ r ≤ n), `r` is an input positive integer (1 ≤ r ≤ n), and `ans` is 0. If `pos` is less than `l`, then `ans` is set to `l - pos`. Otherwise, `ans` remains 0.
    if (pos > r) :
        ans += pos - r
    #State of the program after the if block has been executed: *`n` is a positive integer (1 ≤ n ≤ 100), `pos` is an integer (1 ≤ pos ≤ n), `l` is a positive integer (1 ≤ l ≤ r ≤ n), `r` is a positive integer (1 ≤ r ≤ n), and `ans` is 0. If `pos` is greater than `r`, then `ans` is set to `pos - r`. Otherwise, `ans` remains 0.
    ans += min(pos - 1, n - r) + max(0, l - 1)
    print(ans)
#Overall this is what the function does:The function accepts four integers: `n`, `pos`, `l`, and `r`, where `n` represents the total number of tabs (1 ≤ n ≤ 100), `pos` is the current cursor position (1 ≤ pos ≤ n), `l` is the left index of a segment to keep open (1 ≤ l ≤ r ≤ n), and `r` is the right index of the same segment. It calculates the number of tabs that need to be closed based on the cursor's position relative to the specified segment `[l, r]`. Specifically, if the cursor is outside the segment, it adds to the count the distance to the nearest boundary of the segment. Additionally, it accounts for tabs to the left of `l` and to the right of `r`, ensuring that any adjustments are made based on the cursor's position, and prints the total number of tabs to close.

