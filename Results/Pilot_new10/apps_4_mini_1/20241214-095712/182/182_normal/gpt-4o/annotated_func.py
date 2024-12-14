#State of the program right berfore the function call: x is an integer representing the camera rotation angle in degrees, where -10^18 ≤ x ≤ 10^18.
def func():
    x = int(input())
    normalized_angle = x % 360
    turns = (360 - normalized_angle) // 90 % 4
    print(turns)
#Overall this is what the function does:The function accepts an integer input representing a camera rotation angle in degrees, normalizes this angle by taking its modulo with 360, and calculates the number of 90-degree turns required to return to the original position, which it then prints. The function does not return a value.

