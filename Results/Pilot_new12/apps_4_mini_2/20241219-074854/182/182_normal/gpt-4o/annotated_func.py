#State of the program right berfore the function call: x is an integer such that -10^18 ≤ x ≤ 10^18.
def func():
    x = int(input())
    normalized_angle = x % 360
    turns = (360 - normalized_angle) // 90 % 4
    print(turns)
#Overall this is what the function does:The function reads an integer input from the user, representing an angle in degrees. It normalizes this angle to a value between 0 and 359 degrees. Then it calculates the number of 90-degree turns needed to align the normalized angle to 0 degrees. The result is printed as an integer representing the number of clockwise 90-degree turns. Note that the function does not handle edge cases for non-integer inputs or values outside the specified range directly, and the function's return type is void since it only prints the result.

