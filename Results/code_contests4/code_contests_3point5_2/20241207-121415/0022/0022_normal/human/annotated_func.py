#State of the program right berfore the function call: **Precondition**: 
- n is an integer such that 1 <= n <= 10^5.
- Each tree is represented by a pair of integers xi and hi where 1 <= xi, hi <= 10^9.
- The pairs are given in ascending order of xi.
- No two trees are located at the same coordinate.
def func():
    n = input()
    p = []
    h = []
    for i in range(n):
        e = map(int, raw_input().split())
        
        p.append(e[0])
        
        h.append(e[1])
        
    #State of the program after the  for loop has been executed: `n` is a valid integer, `p` is a list containing the values at index 0 of the lists obtained from input, `h` is a list containing the values at index 1 of the lists obtained from input
    pivout = p[0]
    if (n == 1) :
        cont = 1
    else :
        cont = 2
    #State of the program after the if-else block has been executed: *`n` is a valid integer, `p` is a list containing the values at index 0 of the lists obtained from input, `h` is a list containing the values at index 1 of the lists obtained from input, `pivout` is assigned the value at index 0 of list `p`. If `n` is equal to 1, `cont` is assigned the value 1. Otherwise, if `n` is not equal to 1, `cont` is assigned the value 2.
    for i in range(1, len(p) - 1):
        if p[i] - h[i] > pivout:
            cont += 1
            pivout = p[i]
        elif p[i] + h[i] < p[i + 1]:
            cont += 1
            pivout = p[i] + h[i]
        else:
            pivout = p[i]
        
    #State of the program after the  for loop has been executed: `n` is a valid integer, `p` is a list containing at least 3 values obtained from input, `h` is a list containing the values at index 1 of the lists obtained from input. The final value of `pivout` is the last updated value based on the conditions in the loop. The final value of `cont` is the total number of times `cont` was incremented throughout the loop.
    print(cont)
#Overall this is what the function does:The function `func` reads input about trees represented by pairs of integers (xi, hi) and processes them based on certain conditions related to their coordinates and heights. It calculates the total number of times a condition is met during processing and prints the final count. The function does not accept any parameters explicitly.

