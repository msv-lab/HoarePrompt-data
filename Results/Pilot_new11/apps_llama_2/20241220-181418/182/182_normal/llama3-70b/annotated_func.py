#State of the program right berfore the function call: the camera angle in degrees is an integer between -10^18 and 10^18 (inclusive), where positive values denote clockwise camera rotation and negative values denote counter-clockwise rotation.
def func():
    x = int(input())
    x = x % 360
    if (x == 0) :
        print(0)
    else :
        print((x + 90 - 1) // 90 % 4)
    #State of the program after the if-else block has been executed: The camera angle in degrees is an integer between -10^18 and 10^18 (inclusive), `x` is an integer between -359 and 359 (inclusive). If `x` is 0, the value 0 has been printed and returned. If `x` is not equal to 0, the printed value is an integer between 0 and 3 (inclusive) equal to `(x + 89) // 90 % 4`.
#Overall this is what the function does:The function takes an integer input from the user, representing a camera angle in degrees, which can be any integer between -10^18 and 10^18 (inclusive). It then normalizes this angle to a value between 0 and 359 (inclusive) by taking the modulus of the input with 360. If the normalized angle is 0, the function prints and returns 0. For non-zero normalized angles, it calculates and prints a value between 0 and 3 (inclusive) using the formula `(x + 90 - 1) // 90 % 4`, effectively categorizing the camera angle into one of four quadrants. However, the function does not include an explicit return statement for non-zero angles, implying that it will return `None` in such cases. Additionally, the function does not handle any potential exceptions that may occur during the input process, such as non-integer inputs. Overall, the function appears to be designed to classify a camera angle into one of four categories based on its normalized value, but its behavior is not fully defined for all possible inputs and edge cases.

