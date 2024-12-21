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
            #State of the program after the if-else block has been executed: *`n` is `d`, `pos` is `b`, `l` is `c`, and the overall state is as follows: if `r` equals `n`, the output is `abs(b - c) + 1`. Otherwise, `r` equals `d`, `move_to_l` is `abs(b - c)`, `move_to_r` is `abs(b - d)`, and `close_both_sides` is `min(abs(b - c) + (d - c + 2), abs(b - d) + (d - c + 2))`
        #State of the program after the if-else block has been executed: *`n` is `a`, `pos` is `b`, `l` is `1` if the condition `l == 1` is true, otherwise `l` is `c`; `r` is `d`. The output of the program is `abs(b - d) + 1` if `l == 1`. Otherwise, the output is `abs(b - c) + 1` if `r` equals `n`, or `close_both_sides` is `min(abs(b - c) + (d - c + 2), abs(b - d) + (d - c + 2))` if `r` does not equal `n`.
    #State of the program after the if-else block has been executed: `n` is `a`, `pos` is `b`, `l` is `1` if the condition `l == 1` is true, otherwise `l` is `c`; `r` is `d`. The output of the program is `0` if `l == 1 and r == n`. Otherwise, the output is `abs(b - d) + 1` if `l == 1`. If `r` equals `n`, the output is `abs(b - c) + 1`. Otherwise, `close_both_sides` is `min(abs(b - c) + (d - c + 2), abs(b - d) + (d - c + 2))`.
#Overall this is what the function does:The function accepts four parameters \( n \), \( pos \), \( l \), and \( r \), where \( 1 \leq n \leq 100 \), \( 1 \leq pos \leq n \), and \( 1 \leq l \leq r \leq n \). It calculates and returns the minimum number of moves required for a position \( pos \) to reach either end \( l \) or \( r \) of a sequence of length \( n \). If \( l \) is equal to \( r \), the function returns 0. If \( l \) is 1 and \( r \) is \( n \), the function returns 0. Otherwise, it calculates the minimum of two possible scenarios: moving to \( l \) and then to \( r \), or moving to \( r \) and then to \( l \), considering the additional moves needed to cover the distance between \( l \) and \( r \).

