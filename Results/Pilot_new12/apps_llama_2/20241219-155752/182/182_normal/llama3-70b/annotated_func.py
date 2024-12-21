#State of the program right berfore the function call: no input parameters are explicitly defined in the function, but it is implied that the function will receive an integer x as input where -10^18 ≤ x ≤ 10^18, representing the camera angle in degrees.
def func():
    x = int(input())
    x = x % 360
    if (x == 0) :
        print(0)
    else :
        print((x + 90 - 1) // 90 % 4)
    #State of the program after the if-else block has been executed: *`x` is an integer between -359 and 359 (inclusive), representing the camera angle in degrees modulo 360. If `x` is 0, the value 0 has been printed. If `x` is not 0, the value of `(x + 90 - 1) // 90 % 4` has been printed.
#Overall this is what the function does:The function accepts an implied integer parameter x, representing the camera angle in degrees, within the range -10^18 ≤ x ≤ 10^18. It normalizes this angle to a value between 0 and 359 by taking the modulus of the input angle with 360. If the normalized angle is 0, it prints 0. For any other normalized angle, it calculates and prints the value of (x + 90 - 1) // 90 % 4, which effectively categorizes the angle into one of four quadrants. The function does not handle any potential exceptions that may occur during the input process, such as non-integer inputs. The final state of the program is that it has printed an integer value based on the calculated quadrant of the normalized camera angle, and the input angle x has been consumed and is no longer accessible.

