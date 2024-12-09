#State of the program right berfore the function call: n, pos, l, and r are integers such that 1 ≤ n ≤ 100, 1 ≤ pos ≤ n, and 1 ≤ l ≤ r ≤ n.
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
            #State of the program after the if-else block has been executed: *`n`, `pos`, `l`, and `r` are integers with `n` between 1 and 100, `pos` between 1 and `n`, `l` between 1 and `r`, `r` between `l` and `n`, `l` not equal to 1, and `r` not equal to `n`. If `r` is equal to `n`, the computed value is `abs(pos - l) + 1`. If `r` is less than `n`, `move_to_l` is equal to `abs(pos - l)`, `move_to_r` is equal to `abs(pos - r)`, and `close_both_sides` is equal to `min(move_to_l + (r - l + 2), move_to_r + (r - l + 2))`, which has been printed.
        #State of the program after the if-else block has been executed: *`n`, `pos`, `l`, and `r` are integers with `n` between 1 and 100, `pos` between 1 and `n`, `l` between 1 and `r`, `r` between `l` and `n`, `l` not equal to 1, and `r` not equal to `n`. If `l` equals 1, the output is `abs(pos - r) + 1`. Otherwise, if `r` equals `n`, the output is `abs(pos - l) + 1`. If `r` is less than `n`, `move_to_l` is equal to `abs(pos - l)`, `move_to_r` is equal to `abs(pos - r)`, and `close_both_sides` is equal to `min(move_to_l + (r - l + 2), move_to_r + (r - l + 2))`, which has been printed.
    #State of the program after the if-else block has been executed: *`n`, `pos`, `l`, and `r` are integers where `n` is between 1 and 100, `pos` is between 1 and `n`, `l` is between 1 and `r`, and `r` is between `l` and `n`. If `l` equals 1 and `r` equals `n`, the function proceeds with this condition. Otherwise, if `l` is not equal to 1 or `r` is not equal to `n`, the output is determined based on the conditions where if `l` equals 1, the output is `abs(pos - r) + 1`. If `r` equals `n`, then the output is `abs(pos - l) + 1`. If `r` is less than `n`, it calculates `move_to_l` as `abs(pos - l)`, `move_to_r` as `abs(pos - r)`, and `close_both_sides` as `min(move_to_l + (r - l + 2), move_to_r + (r - l + 2))`, which is then printed.
#Overall this is what the function does:The function accepts four integer parameters `n`, `pos`, `l`, and `r`, where `1 ≤ n ≤ 100`, `1 ≤ pos ≤ n`, and `1 ≤ l ≤ r ≤ n`. It calculates and prints the minimum number of moves required to reach either end of the segment defined by `l` and `r` from the current position `pos`. If the entire segment (from 1 to n) is covered (i.e., `l == 1` and `r == n`), it prints 0. If `l` is 1, it prints the distance to `r` plus one. If `r` is `n`, it prints the distance to `l` plus one. If both `l` and `r` are between their respective bounds, it computes the minimum distance to move to both ends of the segment and prints that value.

