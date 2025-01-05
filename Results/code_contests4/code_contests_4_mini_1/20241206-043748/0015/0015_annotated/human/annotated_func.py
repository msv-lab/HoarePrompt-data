#State of the program right berfore the function call: n is a positive integer representing the number of citizens in the city, x is a non-negative integer representing the number of wizards (0 <= x <= n), and y is a non-negative integer representing the percentage required for the demonstration (1 <= y <= 10^4).
def func():
    c = raw_input()
    p = c.split()
    num = []
    for i in p:
        num.append(int(i))
        
    #State of the program after the  for loop has been executed: `num` contains the integer values of all words in `p`, `p` is a list of words, and `n`, `x`, and `y` retain their initial states.
    y = float(num[0] * num[2]) / float(100) - num[1]
    if (y % 1 == 0) :
        print(int(y))
    else :
        print(int(y) + 1)
    #State of the program after the if-else block has been executed: *`num` contains the integer values of all words in `p`; `p` is a list of words; `n`, `x`, and `y` retain their initial states; `y` is assigned the value of (num[0] * num[2]) / 100 - num[1]. If `y` is an integer, the output is the integer value of `y` printed. If `y` is not an integer (y % 1 ≠ 0), the program prints the result of int(y) + 1, which is an integer greater than int(y).
#Overall this is what the function does:The function accepts input for the number of citizens, the number of wizards, and the required percentage for a demonstration. It calculates the number of additional wizards needed based on the formula (n * y / 100) - x, where n is the number of citizens, x is the number of wizards, and y is the required percentage. If the result is an integer, it prints that value; if it is not, it prints the next higher integer. The function does not return any value but prints the result directly. It does not handle any edge cases for invalid input or negative values for the parameters, assuming all inputs are valid as per the initial conditions stated.

