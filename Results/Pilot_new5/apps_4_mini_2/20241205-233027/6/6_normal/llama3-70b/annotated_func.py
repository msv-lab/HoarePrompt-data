#State of the program right berfore the function call: n is an integer representing the number of tabs, pos is an integer representing the current position of the cursor (1 ≤ pos ≤ n), l is an integer representing the starting index of the segment to keep open (1 ≤ l ≤ r ≤ n), and r is an integer representing the ending index of the segment to keep open (1 ≤ r ≤ n).
def func():
    n, pos, l, r = map(int, input().split())
    ans = 0
    if (pos < l) :
        ans += l - pos
    #State of the program after the if block has been executed: *`n`, `pos`, `l`, `r` are integers with `1 ≤ pos ≤ n`, `1 ≤ l ≤ r ≤ n`, and `1 ≤ r ≤ n`. If `pos` is less than `l`, then `ans` is equal to `l - pos`; otherwise, `ans` remains 0.
    if (pos > r) :
        ans += pos - r
    #State of the program after the if block has been executed: *`n`, `pos`, `l`, `r` are integers with `1 ≤ pos ≤ n`, `1 ≤ l ≤ r ≤ n`, and `1 ≤ r ≤ n`. If `pos` is greater than `r`, then `ans` is equal to `pos - r`. If `pos` is less than or equal to `r`, then `ans` remains unchanged as 0.
    ans += min(pos - 1, n - r) + max(0, l - 1)
    print(ans)
#Overall this is what the function does:The function accepts four integers `n`, `pos`, `l`, and `r`, representing the total number of tabs, the current cursor position, and the segment of tabs to keep open defined by indices `l` and `r`. It calculates the number of tabs to close based on the cursor's position relative to the open segment and prints this number. If the cursor is left of the open segment, it counts how many tabs need to be opened to reach `l`. If it's right of the segment, it counts how many tabs need to be closed to reach `r`. Additionally, it accounts for the tabs preceding `l` and succeeding `r`, ensuring it handles edge cases where the cursor is outside the defined segment.

