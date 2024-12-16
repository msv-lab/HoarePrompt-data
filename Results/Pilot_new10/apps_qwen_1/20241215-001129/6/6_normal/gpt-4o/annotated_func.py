#State of the program right berfore the function call: n, pos, l, r are integers such that 1 ≤ n ≤ 100, 1 ≤ pos ≤ n, 1 ≤ l ≤ r ≤ n.
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
            #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100, `pos` is an integer between 1 and `n`, `l` is an integer between 1 and `n`, `r` is an integer between `l` and `n` with `r != n`. If `r == n`, the output is `abs(pos - l) + 1`. Otherwise, `close_both_sides` is defined as `min(abs(pos - l) + (r - l + 2), abs(pos - r) + (r - l + 2))`, `move_to_r` is `abs(pos - r)`, `move_to_l` is `abs(pos - l)`, and `close_both_sides` is printed.
        #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100, `pos` is an integer between 1 and `n`, `l` is an integer between 1 and `n`, and `r` is an integer between `l` and `n` (excluding 1 and `n`). If `l == 1`, the output is `abs(pos - r) + 1`. Otherwise, if `r == n`, the output is `abs(pos - l) + 1`. Otherwise, `close_both_sides` is defined as `min(abs(pos - l) + (r - l + 2), abs(pos - r) + (r - l + 2))`, `move_to_r` is `abs(pos - r)`, `move_to_l` is `abs(pos - l)`, and `close_both_sides` is printed.
    #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100, `pos` is an integer between 1 and `n`, `l` is an integer between 1 and `n`, `r` is an integer between `l` and `n`. After the execution of the if-else block, if `l == 1` and `r == n`, the console displays `0`. Otherwise, if `l == 1`, the console displays `abs(pos - r) + 1`. If `r == n`, the console displays `abs(pos - l) + 1`. Otherwise, `close_both_sides` is defined as the minimum of `abs(pos - l) + (r - l + 2)` and `abs(pos - r) + (r - l + 2)`, `move_to_r` is `abs(pos - r)`, `move_to_l` is `abs(pos - l)`, and `close_both_sides` is printed.
#Overall this is what the function does:The function accepts four integers `n`, `pos`, `l`, and `r` with the constraints 1 ≤ n ≤ 100, 1 ≤ pos ≤ n, 1 ≤ l ≤ r ≤ n. It prints the minimum number of moves required for `pos` to reach either `l` or `r`. Specifically:
- If `l == 1` and `r == n`, it prints `0`.
- If `l == 1`, it prints `abs(pos - r) + 1`.
- If `r == n`, it prints `abs(pos - l) + 1`.
- Otherwise, it calculates `close_both_sides` as the minimum of `abs(pos - l) + (r - l + 2)` and `abs(pos - r) + (r - l + 2)` and prints this value.

