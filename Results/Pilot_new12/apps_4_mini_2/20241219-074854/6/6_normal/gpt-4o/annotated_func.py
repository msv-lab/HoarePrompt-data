#State of the program right berfore the function call: n is an integer between 1 and 100, pos is an integer such that 1 <= pos <= n, l is an integer such that 1 <= l <= r <= n, and r is an integer such that r <= n.
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
            #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100, `pos` is an integer such that 1 <= `pos` <= `n`, `l` is an integer such that 1 <= `l` <= `r` <= `n`, `r` is an integer such that `r` <= `n`, `l` is not equal to 1, and it is not the case that (`l` == 1 and `r` == `n`). If `r` is equal to `n`, then the expression `abs(pos - l) + 1` has been computed and printed. Otherwise, `move_to_l` is equal to `abs(pos - l)`, `move_to_r` is equal to `abs(pos - r)`, and `close_both_sides` is printed.
        #State of the program after the if-else block has been executed: *`n`, `pos`, `l`, and `r` are integers where `1 <= n <= 100`, `1 <= pos <= n`, `1 <= l <= r <= n`, and `r <= n`. If `l` is equal to 1, the output is `abs(pos - r) + 1`. If `l` is not equal to 1, and if `r` is equal to `n`, then the output is `abs(pos - l) + 1`. Otherwise, `move_to_l` is equal to `abs(pos - l)` and `move_to_r` is equal to `abs(pos - r)` and `close_both_sides` is printed.
    #State of the program after the if-else block has been executed: *`n`, `pos`, `l`, and `r` are integers such that `1 <= n <= 100`, `1 <= pos <= n`, `1 <= l <= r <= n`, and `r <= n`. If `l` equals 1 and `r` equals `n`, then 0 is printed. If `l` equals 1 but `r` is not equal to `n`, the output is `abs(pos - r) + 1`. If `l` is not equal to 1 and `r` equals `n`, then the output is `abs(pos - l) + 1`. Otherwise, the absolute distances `move_to_l` and `move_to_r` are calculated and `close_both_sides` is printed.
#Overall this is what the function does:The function accepts four integer parameters: n (1 <= n <= 100), pos (1 <= pos <= n), l (1 <= l <= r <= n), and r (r <= n). It calculates and prints a distance based on the relative positions of 'pos', 'l', and 'r'. It handles several cases: If l is 1 and r is n, it prints 0; if l is 1 and r is not n, it prints the distance from 'pos' to 'r' plus 1; if l is not 1 and r is n, it prints the distance from 'pos' to 'l' plus 1; otherwise, it calculates the absolute distances from 'pos' to both 'l' and 'r', and prints the minimum total distance needed to traverse between them while accounting for the distance between 'l' and 'r' plus 2. The final output is based on these calculations, representing the shortest movement necessary to transition between the specified positions.

