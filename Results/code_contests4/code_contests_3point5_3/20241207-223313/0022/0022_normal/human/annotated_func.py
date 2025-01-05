#State of the program right berfore the function call: **
def func():
    n = input()
    p = []
    h = []
    for i in range(n):
        e = map(int, raw_input().split())
        
        p.append(e[0])
        
        h.append(e[1])
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `p` contains all the integer values from the input split, `h` contains all the corresponding integer values from the input split, and both lists have a length equal to `n`
    pivout = p[0]
    if (n == 1) :
        cont = 1
    else :
        cont = 2
    #State of the program after the if-else block has been executed: *`n` is greater than 0, `p` and `h` contain all the integer values from the input split with a length equal to `n`, `pivout` is the first integer value of `p`. If `n` is equal to 1, `cont` is equal to 1. If `n` is not equal to 1, `cont` is equal to 2.
    for i in range(1, len(p) - 1):
        if p[i] - h[i] > pivout:
            cont += 1
            pivout = p[i]
        elif p[i] + h[i] < p[i + 1]:
            cont += 1
            pivout = p[i] + h[i]
        else:
            pivout = p[i]
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `p` and `h` contain all the integer values from the input split with a length equal to `n`, `i` is equal to len(p) - 1, `cont` is the total number of times either p[i] - h[i] > pivout or p[i] + h[i] < p[i + 1] was true, `pivout` contains the maximum value from the conditions in the loop.
    print(cont)
#Overall this is what the function does:The function reads an integer input `n`, then reads `n` pairs of integers into lists `p` and `h`. It calculates a value `cont` based on conditions involving elements of `p` and `h`, and prints the final value of `cont`.

