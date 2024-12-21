#State of the program right berfore the function call: n, pos, l, and r are integers such that 1 <= n <= 100, 1 <= pos <= n, 1 <= l <= r <= n.
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
            #State of the program after the if-else block has been executed: *`n` equals the first input integer, `pos` equals the second input integer, `l` equals the third input integer, `r` equals the fourth input integer, 1 <= `n` <= 100, 1 <= `pos` <= `n`, 1 <= `l` <= `r` <= `n`, `l` is not equal to 1, if `r` equals `n`, then a value `abs(pos - l) + 1` has been returned and printed at the output, otherwise, `move_to_l` equals `abs(pos - l)`, `move_to_r` equals `abs(pos - r)`, `close_both_sides` equals `min(abs(pos - l) + (r - l + 2), abs(pos - r) + (r - l + 2))`, and `close_both_sides` has been returned
        #State of the program after the if-else block has been executed: `n` equals the first input integer, `pos` equals the second input integer, `l` equals the third input integer, `r` equals the fourth input integer, 1 <= `n` <= 100, 1 <= `pos` <= `n`, 1 <= `l` <= `r` <= `n`, and either `l` is not equal to 1 or `r` is not equal to `n`. If `l` equals 1 and `r` is not equal to `n`, then the value `abs(pos - r) + 1` has been printed. If `l` is not equal to 1, then if `r` equals `n`, the value `abs(pos - l) + 1` has been returned and printed, otherwise, the minimum value between `abs(pos - l) + (r - l + 2)` and `abs(pos - r) + (r - l + 2)` has been returned.
    #State of the program after the if-else block has been executed: *`n` equals the first input integer, `pos` equals the second input integer, `l` equals the third input integer, `r` equals the fourth input integer, 1 <= `n` <= 100, 1 <= `pos` <= `n`, 1 <= `l` <= `r` <= `n`. If `l` equals 1 and `r` equals `n`, then the value 0 has been printed. If `l` equals 1 and `r` is not equal to `n`, then the value `abs(pos - r) + 1` has been printed. If `l` is not equal to 1 and `r` equals `n`, then the value `abs(pos - l) + 1` has been returned and printed. Otherwise, the minimum value between `abs(pos - l) + (r - l + 2)` and `abs(pos - r) + (r - l + 2)` has been returned.
#Overall this is what the function does:The function calculates and prints the minimum number of steps required to move an object from a position `pos` to a specific range `[l, r]` within a total length `n`, where `1 <= n <= 100`, `1 <= pos <= n`, and `1 <= l <= r <= n`. The function accepts no parameters explicitly but takes four integers as input: `n`, `pos`, `l`, and `r`, representing the total length, current position, left boundary, and right boundary of the range, respectively. After execution, the program will have printed the minimum number of steps required, considering three cases: (1) if the range covers the entire length (`l == 1` and `r == n`), it prints `0`; (2) if the object is already at or beyond one end of the range, it calculates and prints the absolute difference plus one; (3) otherwise, it calculates and prints the minimum of two options: moving to the left boundary and then to the right boundary, or moving to the right boundary and then to the left boundary, both of which account for the distance between the boundaries plus two. The function does not return a value but prints the result directly to the output.

