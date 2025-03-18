#State of the program right berfore the function call: The function takes no arguments, but it reads an integer x from the input, where x is the camera angle in degrees, -10^18 ≤ x ≤ 10^18, and a positive value denotes clockwise camera rotation, while a negative value denotes counter-clockwise rotation.
def func():
    x = int(input())
    x = x % 360
    if (x == 0) :
        print(0)
    else :
        print((x + 90 - 1) // 90 % 4)
    #State of the program after the if-else block has been executed: `x` is an integer between -359 and 359 (inclusive), where a positive value denotes clockwise camera rotation and a negative value denotes counter-clockwise rotation. If `x` is 0, it denotes no camera rotation. If `x` is not 0, an integer value between 0 and 3 (inclusive) has been printed based on the expression `(x + 90 - 1) // 90 % 4`.
#Overall this is what the function does:The function reads a camera angle in degrees from the input, normalizes it to an equivalent angle between -359 and 359 degrees, and then outputs 0 if the normalized angle is 0 (indicating no rotation or a full rotation), or otherwise categorizes the rotation into one of four categories based on the expression `(x + 90 - 1) // 90 % 4` and prints the corresponding category number.

