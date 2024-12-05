#State of the program right berfore the function call: x is an integer such that -10^18 ≤ x ≤ 10^18, representing the camera angle in degrees, where positive values denote clockwise rotations and negative values denote counter-clockwise rotations.
def func():
    x = int(input())
    x = x % 360
    if (x == 0) :
        print(0)
    else :
        print((x + 90 - 1) // 90 % 4)
    #State of the program after the if-else block has been executed: *`x` is an integer such that -10^18 ≤ `x` ≤ 10^18 and after the operation `x` becomes `x % 360` within the range of -359 to 359. If `x` is 0, it has been printed. Otherwise, `x` is an integer within -359 to 359, not equal to 0, and the output is some integer in {0, 1, 2, 3}.
#Overall this is what the function does:The function accepts an integer input `x`, which represents a camera angle in degrees. It normalizes `x` to the range of [0, 360) by using `x % 360`. If `x` is 0, it prints 0. Otherwise, it calculates and prints the equivalent direction as an integer in the set {0, 1, 2, 3}, based on the normalized value of `x`. This integer corresponds to the 90-degree rotation segment that the angle falls into, where 0 is north, 1 is east, 2 is south, and 3 is west. The function does not return any value; it only prints the results.

