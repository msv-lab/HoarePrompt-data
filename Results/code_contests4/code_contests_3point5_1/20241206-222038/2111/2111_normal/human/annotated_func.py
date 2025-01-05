#State of the program right berfore the function call: **
def func():
    N = input()
    S = raw_input.split()
    for i in range(N):
        if S[i] == 'Y':
            print('Four')
            N = -1
            break
        
    #State of the program after the  for loop has been executed: Output State: *Error: 'raw_input' is not defined. If the loop does execute, it will only execute once at most. If `S` contains the character 'Y' at any index, 'Four' is printed, and `N` is set to -1. The loop will not execute again after encountering 'Y' in `S`.
    if (N == -1) :
        print('Three')
    #State of the program after the if block has been executed: *Output State: Error: 'raw_input' is not defined. The loop will execute at most once. If `S` contains the character 'Y' at any index, 'Four' is printed, and `N` is set to -1. After encountering 'Y' in `S`, the loop will not execute again. 'Three' is printed if `N` is -1.
#Overall this is what the function does:The function `func` reads an input value `N`, then tries to split `raw_input` which is not defined causing an error. It iterates over `N` elements in the list `S`, and if it finds the character 'Y', it prints 'Four', sets `N` to -1, and breaks out of the loop. If `N` is set to -1 during the loop, it prints 'Three' after the loop ends. The function does not accept any parameters and returns specific outputs based on the conditions met during execution.

