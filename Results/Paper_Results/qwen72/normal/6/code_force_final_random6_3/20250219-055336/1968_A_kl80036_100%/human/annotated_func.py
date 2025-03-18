#State of the program right berfore the function call: The function should take an integer x as input where 2 ≤ x ≤ 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: `x` is an input integer where 2 ≤ x ≤ 1000, `i` is `input() - 1`, `y` is `x - 1`
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads an integer from the user input, which represents the number of iterations. For each iteration, it reads another integer `x` from the user input, where 2 ≤ x ≤ 1000, and prints `x - 1`. After the function concludes, the program state includes the number of iterations completed and the printed values, which are each one less than the corresponding input integers.

