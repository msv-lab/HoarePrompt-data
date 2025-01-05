#State of the program right berfore the function call: n is an integer such that 1 <= n <= 20, and each participant number ai is a distinct integer between 1 and n with an associated number of fish caught vi, where 0 <= vi <= 100.
def func_1(readline):
    value = -1
    number = maxsize
    for _ in range(int(readline())):
        a, v = (int(s) for s in readline().split())
        
        if v > value or v == value and a < number:
            number = a
            value = v
        
    #State of the program after the  for loop has been executed: `value` is the maximum `v` encountered during the loop iterations, `number` is the corresponding `a` for that maximum `v`, `a` and `v` are the last positive integers read from input if the loop executed, otherwise `value` is -1 and `number` is maxsize.
    print(number, value)
    exit()
#Overall this is what the function does:The function accepts a `readline` parameter that is used to read input values for a number of participants, each represented by a distinct integer `a` (participant number) and an integer `v` (number of fish caught). It determines the participant who caught the maximum number of fish. If multiple participants caught the same maximum number of fish, it returns the participant with the smallest participant number. If no valid input is provided (e.g., if the loop does not execute), it defaults to `number` as maxsize and `value` as -1, indicating no valid participants were processed. The function prints the participant number and their corresponding catch value, and then exits.

