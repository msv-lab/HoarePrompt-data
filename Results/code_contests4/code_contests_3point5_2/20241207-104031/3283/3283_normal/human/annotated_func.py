#State of the program right berfore the function call: x is an integer such that -109 <= x <= 109.**
def func():
    n = abs(input())
    d = int(ceil((sqrt(1 + 8 * n) - 1) / 2))
    print[[0, 2, 1, 0], [1, 0, 0, 2]][n % 2][d % 4] + d
#Overall this is what the function does:The function calculates a value based on the input `x`, which is an integer within the range -109 to 109. It then prints a value based on the calculations performed on `n` and `d`. The function does not accept any parameters and returns the integer x.

