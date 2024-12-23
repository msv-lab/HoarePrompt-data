#State of the program right berfore the function call: x is an integer representing the rotation angle of the camera in degrees, where -10^18 ≤ x ≤ 10^18.
def func():
    x = int(input())
    x = x % 360
    if (x == 0) :
        print(0)
    else :
        print((x + 90 - 1) // 90 % 4)
    #State of the program after the if-else block has been executed: *`x` is an integer representing the rotation angle of the camera in degrees, if `x` is equal to 0, the function does not return any value. Otherwise, `x` is not equal to 0 and the result of the expression `(x + 90 - 1) // 90 % 4` is returned, representing the adjusted rotation based on the current angle.
#Overall this is what the function does:The function reads an integer input representing a rotation angle of a camera in degrees, normalizes this angle to the range of 0 to 359 degrees using the modulo operation, and then evaluates the normalized angle. If the normalized angle is 0, it prints 0. For any other normalized angle, it calculates and prints an integer representing the adjusted rotation state based on the normalized angle, specifically the division of the angle adjusted by 90 degrees and then taken modulo 4. The function does not return any value; it only prints results to the output. The potential edge cases include handling of inputs that might initially exceed the expected bounds, and the function solely relies on computed standard inputs without validation of range constraints on the input itself.

