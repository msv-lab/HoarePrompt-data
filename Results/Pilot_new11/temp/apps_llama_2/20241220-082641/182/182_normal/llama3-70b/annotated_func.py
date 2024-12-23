#State of the program right berfore the function call: the camera angle is an integer in the range -10^18 to 10^18, with positive values denoting clockwise camera rotation and negative values denoting counter-clockwise rotation.
def func():
    x = int(input())
    x = x % 360
    if (x == 0) :
        print(0)
    else :
        print((x + 90 - 1) // 90 % 4)
    #State of the program after the if-else block has been executed: the camera angle is an integer in the range -10^18 to 10^18, `x` is an integer in the range -359 to 359, if `x` is 0, then the integer `0` has been printed at the output, otherwise, the expression `(x + 90 - 1) // 90 % 4` with a value of 0, 1, 2, or 3 has been printed at the output.
#Overall this is what the function does:The function accepts an integer input from the user, representing a camera angle, normalizes it to a value between 0 and 359 by taking the modulus of the input with 360, and then prints a value based on the normalized angle. If the normalized angle is 0, it prints 0; otherwise, it prints a value between 0 and 3, calculated using the expression `(x + 90 - 1) // 90 % 4`, where `x` is the normalized angle. The function does not return any value but instead prints the result directly to the output, and it does not handle any potential exceptions that might occur during the input operation. The state of the program after the function concludes is that the input has been consumed, the normalized angle has been calculated, and the corresponding value has been printed to the output.

