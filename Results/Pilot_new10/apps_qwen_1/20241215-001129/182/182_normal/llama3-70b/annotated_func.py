#State of the program right berfore the function call: x is an integer such that -10^18 ≤ x ≤ 10^18.
def func():
    x = int(input())
    x = x % 360
    if (x == 0) :
        print(0)
    else :
        print((x + 90 - 1) // 90 % 4)
    #State of the program after the if-else block has been executed: *`x` is an integer in the range 0 to 359. If `x` equals 0, "0" is printed on the screen. If `x` is not 0, "0" or "1" is printed on the screen.
#Overall this is what the function does:The function takes an integer input `x` and reduces it modulo 360 to get a value in the range [0, 359]. If the reduced value is 0, it prints 0. Otherwise, it prints 1, 2, 3, or 0 depending on the value of `x` in its reduced form.

