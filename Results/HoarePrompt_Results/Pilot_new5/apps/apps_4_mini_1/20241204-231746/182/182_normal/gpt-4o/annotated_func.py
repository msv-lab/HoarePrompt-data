#State of the program right berfore the function call: x is an integer representing the camera rotation angle in degrees, where -10^18 ≤ x ≤ 10^18.
def func():
    x = int(input())
    normalized_angle = x % 360
    turns = (360 - normalized_angle) // 90 % 4
    print(turns)
#Overall this is what the function does:The function accepts an integer input `x`, representing a camera rotation angle in degrees, and calculates the number of 90-degree turns needed to return the camera to its original orientation. It prints this number of turns, which is based on the normalized angle of `x` modulo 360. The function does not handle any input validation and assumes the input is always provided as an integer.

