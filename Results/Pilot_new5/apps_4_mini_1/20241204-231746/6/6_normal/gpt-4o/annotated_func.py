#State of the program right berfore the function call: n is an integer between 1 and 100, pos is an integer between 1 and n, l is an integer between 1 and n, and r is an integer between l and n, representing the indices of the tabs.
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
            #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100; `pos` is an integer between 1 and `n`; `l` is an integer between 1 and `n` and not equal to 1; `r` is an integer between `l` and `n`. If `r` is equal to `n`, the value printed is `abs(pos - l) + 1`. Otherwise, `move_to_l` is equal to `abs(pos - l)`, `move_to_r` is equal to `abs(pos - r)`, and `close_both_sides` is equal to `min(move_to_l + (r - l + 2), move_to_r + (r - l + 2)` which is printed.
        #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100; `pos` is an integer between 1 and `n`; `l` is an integer between 1 and `n` and not equal to 1; `r` is an integer between `l` and `n`. If `l` is equal to 1, the printed value is `abs(pos - r) + 1`. Otherwise, if `r` is equal to `n`, the value printed is `abs(pos - l) + 1`. If `r` is not equal to `n`, `move_to_l` is equal to `abs(pos - l)`, `move_to_r` is equal to `abs(pos - r)`, and `close_both_sides` is equal to `min(move_to_l + (r - l + 2), move_to_r + (r - l + 2))`, which is printed.
    #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 100; `pos` is an integer between 1 and `n`; `l` is an integer between 1 and `n`; `r` is an integer between `l` and `n`. If `l` is 1 and `r` is equal to `n`, the printed output is 0. Otherwise, if `l` is 1, the printed value is `abs(pos - r) + 1`. If `r` is equal to `n`, the printed value is `abs(pos - l) + 1`. If neither condition holds, `move_to_l` is equal to `abs(pos - l)`, `move_to_r` is equal to `abs(pos - r)`, and `close_both_sides` is equal to `min(move_to_l + (r - l + 2), move_to_r + (r - l + 2))`, which is printed.
#Overall this is what the function does:The function accepts four integer parameters: `n`, `pos`, `l`, and `r`, where `n` is between 1 and 100, `pos` is between 1 and `n`, `l` is between 1 and `n` (not equal to 1), and `r` is between `l` and `n`. It calculates and prints the minimum number of moves required to navigate from position `pos` to the specified tab range defined by `l` and `r`. If the leftmost tab (`l`) is 1 and the rightmost (`r`) is `n`, it prints 0. If only the leftmost tab is 1, it prints the distance to `r` plus one. If only the rightmost tab is `n`, it prints the distance to `l` plus one. If both `l` and `r` are within the range, it calculates the minimal movement considering moving to either `l` or `r` and the distance between them, printing the result.

