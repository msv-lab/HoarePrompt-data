#State of the program right berfore the function call: n is an integer representing the number of tabs (1 ≤ n ≤ 100), pos is an integer representing the current cursor position (1 ≤ pos ≤ n), l is an integer representing the left index of the segment that needs to remain open (1 ≤ l ≤ r ≤ n), and r is an integer representing the right index of the segment that needs to remain open (1 ≤ l ≤ r ≤ n).
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
            #State of the program after the if-else block has been executed: *`n`, `pos`, `l`, and `r` are integers representing the number of tabs, the current cursor position, and the left and right indices of the segment that needs to remain open, respectively. If `r` is equal to `n`, the value printed is `abs(pos - l) + 1`. Otherwise, if `r` is less than `n`, `move_to_l` is equal to `abs(pos - l)` and `move_to_r` is equal to `abs(pos - r)`; `close_both_sides` is printed as the minimum of `move_to_l + (r - l + 2)` and `move_to_r + (r - l + 2)`.
        #State of the program after the if-else block has been executed: *`n`, `pos`, `l`, and `r` are integers representing the number of tabs, the current cursor position, and the left and right indices of the segment that needs to remain open, respectively. If `l` is equal to 1, the output is `abs(pos - r) + 1`. Otherwise, if `r` is equal to `n`, the printed value is `abs(pos - l) + 1`. If `r` is less than `n`, the program calculates `move_to_l` as `abs(pos - l)` and `move_to_r` as `abs(pos - r)`, and prints `close_both_sides` as the minimum of `move_to_l + (r - l + 2)` and `move_to_r + (r - l + 2)`.
    #State of the program after the if-else block has been executed: *`n`, `pos`, `l`, and `r` are integers representing the number of tabs, the current cursor position, and the left and right indices of the segment that needs to remain open, respectively. If `l` is equal to 1 and `r` is equal to `n`, the entire segment of tabs from 1 to `n` remains open and the output printed is 0. If `l` is equal to 1, the output printed is `abs(pos - r) + 1`. If `r` is equal to `n`, the output printed is `abs(pos - l) + 1`. If `r` is less than `n`, the program calculates `move_to_l` as `abs(pos - l)` and `move_to_r` as `abs(pos - r)`, and prints `close_both_sides` as the minimum of `move_to_l + (r - l + 2)` and `move_to_r + (r - l + 2)`.
#Overall this is what the function does:The function accepts four integers: `n` (total number of tabs), `pos` (current cursor position), `l` (left index of the segment that needs to remain open), and `r` (right index of the segment that needs to remain open). It prints the minimum number of moves required to close the tabs outside the segment [l, r], based on the current cursor position. If the entire range of tabs (from 1 to n) is to remain open, it returns 0. If `l` is 1, it computes the distance from `pos` to `r` and adds one. If `r` is n, it computes the distance from `pos` to `l` and adds one. If both `l` and `r` are within the bounds of the tabs, it calculates the moves to both ends of the segment and takes the minimum total move required to close the remaining tabs. All inputs are constrained to valid ranges.

