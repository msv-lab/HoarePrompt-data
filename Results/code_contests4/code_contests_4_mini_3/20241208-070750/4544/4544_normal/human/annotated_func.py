#State of the program right berfore the function call: n is an integer between 1 and 20, participant numbers ai are distinct integers between 1 and n, and vi is an integer between 0 and 100 representing the number of fish caught by participant ai.
def func_1(readline):
    value = -1
    number = maxsize
    for _ in range(int(readline())):
        a, v = (int(s) for s in readline().split())
        
        if v > value or v == value and a < number:
            number = a
            value = v
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 20; `value` is the maximum number of fish caught among all participants, and `number` is the participant number associated with that maximum catch.
    print(number, value)
    exit()
#Overall this is what the function does:The function accepts a function `readline` that provides input for participant numbers and the number of fish caught by each participant. It determines the participant who caught the maximum number of fish, returning their participant number and the corresponding catch. In case of a tie in the number of fish caught, it selects the participant with the lower participant number. The function does not return any values but prints the result and exits.

