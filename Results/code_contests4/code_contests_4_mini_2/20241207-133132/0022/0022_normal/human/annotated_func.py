#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100000), and each tree is represented by a pair of integers (xi, hi) where 1 ≤ xi, hi ≤ 10^9, with all xi being distinct and given in ascending order.
def func():
    n = input()
    p = []
    h = []
    for i in range(n):
        e = map(int, raw_input().split())
        
        p.append(e[0])
        
        h.append(e[1])
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is `n`, `p` contains `n` integers from the first elements of the input pairs, `h` contains `n` integers from the second elements of the input pairs.
    pivout = p[0]
    if (n == 1) :
        cont = 1
    else :
        cont = 2
    #State of the program after the if-else block has been executed: *`n` is a positive integer. If `n` is equal to 1, then `i` is set to 1, `p` and `h` each contain 1 integer, `pivout` is the first element of `p`, and `cont` is initialized to 1. If `n` is greater than 1, then `i` is set to `n`, `p` contains `n` integers, `h` contains `n` integers, `pivout` is the first element of `p`, and `cont` is set to 2.
    for i in range(1, len(p) - 1):
        if p[i] - h[i] > pivout:
            cont += 1
            pivout = p[i]
        elif p[i] + h[i] < p[i + 1]:
            cont += 1
            pivout = p[i] + h[i]
        else:
            pivout = p[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `cont` is the count of conditions met during the loop, `pivout` is the last computed value based on the loop's logic.
    print(cont)
#Overall this is what the function does:The function accepts a positive integer `n`, representing the number of trees, and processes pairs of integers (xi, hi) that represent the position and height of each tree respectively. It counts and prints the number of trees that can be "seen" based on specific conditions regarding their heights and positions. If there is only one tree, it counts it as visible; otherwise, it checks if a tree is either not obstructed by the previous tree or if it can be seen beyond the height of the previous trees. The function does not handle any input validation or edge cases explicitly, such as when `n` is less than 1, but it assumes `n` will always be within the specified range (1 ≤ n ≤ 100000).

