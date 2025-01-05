#State of the program right berfore the function call: sum and limit are integers such that 1 ≤ sum, limit ≤ 10^5.
def func():
    target, n = map(int, raw_input().split())
    A = []
    s = 0
    for i in range(1, n + 1):
        k = (i & -i) - 1
        
        if i != 1 and k == i - 1:
            k = int(math.log(i, 2))
        
        A.append((2 ** k, i))
        
        s += A[-1][0]
        
    #State of the program after the  for loop has been executed: `sum`, `limit`, `target` are integers; `n` is a positive integer; `A` is a list containing `n` tuples of the form (2^k, i); `s` is the sum of the first elements of all tuples in `A`.
    if (s < target) :
        print(-1)
        exit()
    #State of the program after the if block has been executed: *`sum`, `limit`, `target` are integers; `n` is a positive integer; `A` is a list containing `n` tuples of the form (2^k, i); `s` is the sum of the first elements of all tuples in `A`. If `s` is less than `target`, -1 is printed and the program exits. If `s` is greater than or equal to `target`, the program continues executing beyond this point.
    A.sort()
    selected = []
    for tup in A:
        target -= tup[0]
        
        selected.append(tup[1])
        
        if target <= 0:
            break
        
    #State of the program after the  for loop has been executed: `sum`, `limit`, `target` is decreased by the sum of the first elements of processed tuples in `A`; `n` is a positive integer; `A` is a sorted list of tuples; `s` is the sum of the first elements of all tuples in `A`; `selected` contains the second elements of the processed tuples in `A`.
    print(len(selected))
    print(' '.join(map(str, selected)))
#Overall this is what the function does:The function reads two integers from input, `target` and `n`. It calculates a list of tuples where each tuple contains a power of two and its index. If the sum of the first elements of these tuples is less than `target`, it prints -1 and exits. Otherwise, it selects the indices of tuples whose first elements cumulatively meet or exceed `target` and prints the count of selected indices followed by the indices themselves. If the sum is exactly equal to `target`, it will include all tuples, and if `target` is reduced to zero during selection, it stops adding further indices. The function does not take parameters directly but relies on user input for its operation.

