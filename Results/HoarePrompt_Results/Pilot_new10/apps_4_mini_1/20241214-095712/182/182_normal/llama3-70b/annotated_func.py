#State of the program right berfore the function call: x is an integer representing the camera rotation angle in degrees, where -10^18 ≤ x ≤ 10^18.
def func():
    x = int(input())
    x = x % 360
    if (x == 0) :
        print(0)
    else :
        print((x + 90 - 1) // 90 % 4)
    #State of the program after the if-else block has been executed: *`x` is an input integer normalized to `x % 360` resulting in a value between 0 and 359. If `x` is 0, the printed value is 0. Otherwise, the printed output is either 0, 1, 2, or 3 depending on the range of `x`.
#Overall this is what the function does:The function accepts an integer input `x`, which represents a camera rotation angle in degrees. It normalizes `x` to a value between 0 and 359 by applying `x % 360`. If the normalized value is 0, it prints 0. For other values, it calculates and prints a number that indicates the quadrant the angle falls into, with results of 1, 2, or 3 corresponding to ranges of angles between 1 to 90, 91 to 180, and 181 to 270 degrees, respectively. The function does not return any values; it only prints the results.

