#State of the program right berfore the function call: n is an integer between 1 and 100, pos is an integer between 1 and n, and l and r are integers such that 1 ≤ l ≤ r ≤ n.
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
            #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100, `pos` is an integer between 1 and `n`, `l` is an integer between 1 and `n`, `r` is an integer between `l` and `n`. If `r == n`, the printed value is `abs(pos - l) + 1`. Otherwise, `r` is an integer between `l` and `n` with `(r != n)`, `move_to_l` is `abs(pos - l)`, `move_to_r` is `abs(pos - r)`, and the printed value is `min(move_to_l + (r - l + 2), move_to_r + (r - l + 2))`.
        #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100, `pos` is an integer between 1 and `n`, `l` is an integer between 1 and `n`, `r` is an integer between `l` and `n`. If `l == 1`, the output is `abs(pos - r) + 1`. Otherwise, if `r == n`, the output is `abs(pos - l) + 1`. If `r != n`, the output is the minimum of `abs(pos - l) + (r - l + 2)` and `abs(pos - r) + (r - l + 2)`.
    #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100, `pos` is an integer between 1 and `n`, `l` is an integer between 1 and `n`, `r` is an integer between `l` and `n`. If `l == 1` and `r == n`, the program prints `0`. Otherwise, if `l == 1`, the output is `abs(pos - r) + 1`. If `r == n`, the output is `abs(pos - l) + 1`. If `r != n`, the output is the minimum of `abs(pos - l) + (r - l + 2)` and `abs(pos - r) + (r - l + 2)`.
#Overall this is what the function does:The function takes no explicit parameters but operates within a predefined context where `n` is an integer between 1 and 100, `pos` is an integer between 1 and `n`, and `l` and `r` are integers such that `1 ≤ l ≤ r ≤ n`. It determines the minimum number of moves required to move a position `pos` to either end of the range `[l, r]`. If `l == 1` and `r == n`, it prints `0` indicating no moves are needed. If `l == 1`, it calculates the moves to reach `r` and prints the result. If `r == n`, it calculates the moves to reach `l` and prints the result. Otherwise, it calculates the moves to reach both ends and prints the minimum of the two. The function returns nothing but prints the result directly.

