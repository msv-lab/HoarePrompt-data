#State of the program right berfore the function call: x is an integer such that -10^18 ≤ x ≤ 10^18.
def func():
    x = int(input())
    normalized_angle = x % 360
    turns = (360 - normalized_angle) // 90 % 4
    print(turns)
#Overall this is what the function does:The function reads an integer `x` from the user, normalizes `x` to an angle between 0 and 360 degrees by taking `x % 360`, calculates the number of 90-degree turns required to reach an angle of 0 from the normalized angle, and prints the result. The function does not accept any parameters and returns nothing. It handles the case where `x` is an integer within the range \([-10^{18}, 10^{18}]\). The function also correctly accounts for negative values of `x` by normalizing them to the appropriate positive equivalent within the 0 to 360 degree range.

