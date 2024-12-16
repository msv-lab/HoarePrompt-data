#State of the program right berfore the function call: x is an integer such that -10^18 ≤ x ≤ 10^18.
def func():
    x = int(input())
    normalized_angle = x % 360
    turns = (360 - normalized_angle) // 90 % 4
    print(turns)
#Overall this is what the function does:The function reads an integer `x` from the user, normalizes the angle to a range between 0 and 359 degrees, calculates the number of 90-degree turns required to align with a specific orientation, and prints the result.

