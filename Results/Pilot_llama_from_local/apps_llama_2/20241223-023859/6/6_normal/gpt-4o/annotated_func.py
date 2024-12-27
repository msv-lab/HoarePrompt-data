#State of the program right berfore the function call: There are four non-negative integer input values: n, pos, l, and r, where n is the total number of tabs, pos is the initial mouse cursor position, and l and r are the start and end indices of the tab segment that needs to be left open, such that 1 <= n <= 100, 1 <= pos <= n, and 1 <= l <= r <= n.
def func():
    n, pos, l, r = map(int, input().split())
    if (l == 1 and r == n) :
        print(0)
    else :
        if (l == 1) :
            print(abs(pos - r) + 1)
        else :
            if (r == n) :
                print(abs(pos - l) + 1)
            else :
                move_to_l = abs(pos - l)
                move_to_r = abs(pos - r)
                close_both_sides = min(move_to_l + (r - l + 2), move_to_r + (r - l + 2))
                print(close_both_sides)
            #State of the program after the if-else block has been executed: `n`, `pos`, `l`, and `r` are input integers, where `n` is the total number of tabs, `pos` is the initial mouse cursor position, and `l` and `r` are the start and end indices of the tab segment that needs to be left open. If `r` equals `n`, the value `abs(pos - l) + 1` has been printed. Otherwise, the value of `close_both_sides`, which is `min(abs(pos - l) + (r - l + 2), abs(pos - r) + (r - l + 2))`, is returned, where `1 <= n <= 100`, `1 <= pos <= n`, and `1 <= l <= r <= n`, and `l` is not 1.
        #State of the program after the if-else block has been executed: *`n`, `pos`, `l`, and `r` are input integers, where `n` is the total number of tabs, `pos` is the initial mouse cursor position, and `l` and `r` are the start and end indices of the tab segment that needs to be left open. If `l` is 1 and `r` is less than `n`, the value `abs(pos - r) + 1` has been returned as output. If `l` is not 1, then if `r` equals `n`, the value `abs(pos - l) + 1` has been printed; otherwise, the value of `min(abs(pos - l) + (r - l + 2), abs(pos - r) + (r - l + 2))` is returned, maintaining the constraints that `1 <= n <= 100`, `1 <= pos <= n`, and `1 <= l <= r <= n`.
    #State of the program after the if-else block has been executed: `n`, `pos`, `l`, and `r` are input integers, where `n` is the total number of tabs, `pos` is the initial mouse cursor position, and `l` and `r` are the start and end indices of the tab segment that needs to be left open. If `l` is 1 and `r` is `n`, the value 0 has been printed. If `l` is 1 and `r` is less than `n`, the value `abs(pos - r) + 1` has been returned as output. If `l` is not 1, then if `r` equals `n`, the value `abs(pos - l) + 1` has been printed; otherwise, the value of `min(abs(pos - l) + (r - l + 2), abs(pos - r) + (r - l + 2))` is returned, maintaining the constraints that `1 <= n <= 100`, `1 <= pos <= n`, and `1 <= l <= r <= n`.
#Overall this is what the function does:The function calculates and prints the minimum number of operations required to close tabs outside the segment [l, r] in a tab strip of length n, given an initial mouse cursor position pos, where 1 <= n <= 100, 1 <= pos <= n, and 1 <= l <= r <= n. The operations are: moving the cursor to a tab and closing it. The function handles four cases: 
- If l is 1 and r is n, it prints 0, as there are no tabs to close outside the segment.
- If l is 1 and r is less than n, it prints the absolute difference between pos and r plus 1, as the cursor needs to move to r and close the tabs to its right.
- If l is not 1 and r is n, it prints the absolute difference between pos and l plus 1, as the cursor needs to move to l and close the tabs to its left.
- If l is not 1 and r is not n, it prints the minimum of two values: 
  - The absolute difference between pos and l plus r-l+2, which represents moving to l, closing the tabs to its left, and then closing the tabs to the right of r.
  - The absolute difference between pos and r plus r-l+2, which represents moving to r, closing the tabs to its right, and then closing the tabs to the left of l.

