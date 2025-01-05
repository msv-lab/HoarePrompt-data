#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 20. ai is a positive integer representing the participant number, and vi is a non-negative integer representing the number of fish caught by participant ai.
def func_1(readline):
    value = -1
    number = maxsize
    for _ in range(int(readline())):
        a, v = (int(s) for s in readline().split())
        
        if v > value or v == value and a < number:
            number = a
            value = v
        
    #State of the program after the  for loop has been executed: `value` is an integer, `number` is a positive integer. The loop iterates over user input values, updating `value` to the maximum `v` encountered and `number` to the corresponding `a` value. If the loop does not execute, `value` remains -1 and `number` remains unknown.
    print(number, value)
    exit()
#Overall this is what the function does:The function `func_1` reads input values representing participant numbers and the number of fish they caught. It then iterates through the input values and finds the participant with the highest number of fish caught. If multiple participants have caught the same maximum number of fish, it selects the one with the lowest participant number. The function prints out the participant number and the corresponding number of fish caught. The function does not have a specific return value mentioned.

