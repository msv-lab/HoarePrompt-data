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
            #State of the program after the if-else block has been executed: `n`, `pos`, `l`, and `r` are integers such that `n` = input integer 1, `pos` = input integer 2, `l` = input integer 3, `r` = input integer 4, where `l` is not equal to 1, and it is not the case that `l` equals 1 and `r` equals `n`. If `r` equals `n`, then a value equal to `abs(pos - l) + 1` has been printed. Otherwise, `l` is not equal to 1, `r` is not equal to `n`, and the value 4 has been printed.
        #State of the program after the if-else block has been executed: *`n`, `pos`, `l`, and `r` are integers such that `n` = input integer 1, `pos` = input integer 2, `l` = input integer 3, `r` = input integer 4. If `l` equals 1, the value `abs(pos - r) + 1` has been returned. If `l` does not equal 1 and `r` equals `n`, the value `abs(pos - l) + 1` has been printed. If `l` is not equal to 1 and `r` is not equal to `n`, the value 4 has been printed.
    #State of the program after the if-else block has been executed: `n`, `pos`, `l`, and `r` are integers such that `n` = input integer 1, `pos` = input integer 2, `l` = input integer 3, `r` = input integer 4. If `l` equals 1 and `r` equals `n`, then 0 is returned and printed. If `l` equals 1 but `r` does not equal `n`, then the value `abs(pos - r) + 1` has been returned. If `l` does not equal 1 but `r` equals `n`, then the value `abs(pos - l) + 1` has been printed. If neither `l` equals 1 nor `r` equals `n`, then the value 4 has been printed.
#Overall this is what the function does:The function accepts four integers `n`, `pos`, `l`, and `r`, calculates a value based on the position `pos` relative to the range `[l, r]` within the bounds of `n`, and prints this value, with specific calculations for different cases of `l` and `r` in relation to `n` and the position `pos`.

