#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, and each tree is represented by a pair of integers (xi, hi) where 1 ≤ xi, hi ≤ 10^9. The pairs (xi, hi) are given in the order of ascending xi, and no two trees have the same coordinate value xi.
def func():
    n = input()
    p = []
    h = []
    for i in range(n):
        e = map(int, raw_input().split())
        
        p.append(e[0])
        
        h.append(e[1])
        
    #State of the program after the  for loop has been executed: `n` is equal to user input (an integer such that 1 ≤ n ≤ 10^5); `i` is `n`; `p` is a list of `n` integers from the first element of each user input; `h` is a list of `n` integers from the second element of each user input.
    pivout = p[0]
    if (n == 1) :
        cont = 1
    else :
        cont = 2
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 10^5. If `n` is equal to 1, then `i` is set to 1, `pivout` is the first element of list `p`, `cont` is 1. Otherwise, `i` is equal to `n`, `pivout` is the first element of list `p`, and `cont` is set to 2.
    for i in range(1, len(p) - 1):
        if p[i] - h[i] > pivout:
            cont += 1
            pivout = p[i]
        elif p[i] + h[i] < p[i + 1]:
            cont += 1
            pivout = p[i] + h[i]
        else:
            pivout = p[i]
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 10^5, `len(p)` is at least 2, `cont` is the count of conditions met during loop execution, and `pivout` is the last updated value based on the conditions checked in the loop.
    print(cont)
#Overall this is what the function does:The function reads an integer `n` from the input, representing the number of trees, and then reads `n` pairs of integers (`xi`, `hi`) which represent the position and height of each tree, respectively. It calculates the number of trees that can be seen based on their positions and heights. The function returns the count of visible trees, which is printed as output. If `n` is 1, it immediately counts one visible tree. For multiple trees, it checks their positions and heights to determine visibility based on specified conditions, ensuring that the calculations account for overlapping heights and positions.

