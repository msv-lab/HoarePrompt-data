#State of the program right berfore the function call: **
def func():
    n = input()
    p = []
    h = []
    for i in range(n):
        e = map(int, raw_input().split())
        
        p.append(e[0])
        
        h.append(e[1])
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `p` contains a list of the first integers from each input split, `h` contains a list of the second integers from each input split
    pivout = p[0]
    if (n == 1) :
        cont = 1
    else :
        cont = 2
    #State of the program after the if-else block has been executed: *`n` is greater than 0, `p` contains a list of the first integers from each input split, `h` contains a list of the second integers from each input split, `pivout` is the first integer from the list `p`. If `n` is equal to 1, `cont` is assigned the value 1. Otherwise, if `n` is not equal to 1, `cont` is assigned the value 2.
    for i in range(1, len(p) - 1):
        if p[i] - h[i] > pivout:
            cont += 1
            pivout = p[i]
        elif p[i] + h[i] < p[i + 1]:
            cont += 1
            pivout = p[i] + h[i]
        else:
            pivout = p[i]
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `n` is greater than 0, `p` contains at least 3 elements, `h` contains a list of the second integers after the loop execution, `pivout` is the updated value based on the loop conditions, and `cont` is the final value after all iterations. The indices `i` satisfy the required conditions based on the loop executions.
    print(cont)
#Overall this is what the function does:The function reads input, processes it to determine certain conditions based on the input values, and finally prints the calculated result `cont`. The function does not accept any parameters and does not return any value. However, it performs operations on the input lists `p` and `h` to calculate the final value of `cont` based on specific conditions within the loops.

