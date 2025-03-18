#State of the program right berfore the function call: n is an integer between 1 and 100, pos is an integer between 1 and n, l is an integer between 1 and n, and r is an integer between l and n, representing the segment of tabs that need to remain open.
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
            #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100; `pos` is an integer between 1 and `n`; `l` is an integer between 1 and `n` and greater than 1; `r` is an integer between `l` and `n` and is less than `n`. If `r` is equal to `n`, the output of the calculation is `abs(pos - l) + 1`. Otherwise, `move_to_l` is equal to `abs(pos - l)`, `move_to_r` is equal to `abs(pos - r)`, and `close_both_sides` is equal to `min(move_to_l + (r - l + 2), move_to_r + (r - l + 2))`, which has been printed.
        #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100; `pos` is an integer between 1 and `n`; `l` is an integer equal to 1; `r` is an integer between `l` and `n` which is not both equal to `1` and `n`, then the output is `abs(pos - r) + 1`, which evaluates to an integer greater than or equal to 1. If `l` is greater than 1, `r` is an integer between `l` and `n` and less than `n`; if `r` is equal to `n`, the output is `abs(pos - l) + 1`. Otherwise, `move_to_l` is equal to `abs(pos - l)`, `move_to_r` is equal to `abs(pos - r)`, and `close_both_sides` is equal to `min(move_to_l + (r - l + 2), move_to_r + (r - l + 2)`, which has been printed.
    #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100; `pos` is an integer between 1 and `n`; `l` is an integer equal to 1; `r` is an integer between `l` and `n`. If `l` is 1 and `r` is equal to `n`, the output is 0. If `l` equals 1 and `r` is not equal to `n`, the output is `abs(pos - r) + 1`, which is an integer greater than or equal to 1. If `l` is greater than 1 and `r` is equal to `n`, the output is `abs(pos - l) + 1`. If `l` is greater than 1 and `r` is less than `n`, the values `move_to_l` equals `abs(pos - l)`, `move_to_r` equals `abs(pos - r)`, and the value `close_both_sides` equals `min(move_to_l + (r - l + 2), move_to_r + (r - l + 2)` have been printed.
#Overall this is what the function does:The function reads four integers from input: `n`, `pos`, `l`, and `r`. It calculates and prints the minimum number of moves required to make a segment of tabs defined by indices `l` to `r` closed, based on the current position `pos`. The function handles special cases: if the entire range [1, n] is open, it prints 0; if only one end (either `l` or `r`) is at the bounds, it computes moves accordingly. For cases where both `l` and `r` are not on the edges, it calculates the moves required to close both ends of the segment and prints the minimum moves considering the distance to both edges. The output is always a non-negative integer, representing the number of actions needed to achieve the desired state.

