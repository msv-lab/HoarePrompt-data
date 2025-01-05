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
        
    #State of the program after the  for loop has been executed: `sum` is an integer, `limit` is an integer, `n` is a positive integer, `i` is `n`, `k` is the last computed value for `k` with `i = n`, `A` contains `n` tuples of the form `(2^k, i)` for each `i` from 1 to `n`, and `s` is the sum of all the first elements of the tuples in `A`.
    if (s < target) :
        print(-1)
        exit()
    #State of the program after the if block has been executed: *`sum`, `limit`, `n`, `i`, `k`, `A`, and `s` are integers. If `s` is less than `target`, then `-1` has been printed.
    A.sort()
    selected = []
    for tup in A:
        target -= tup[0]
        
        selected.append(tup[1])
        
        if target <= 0:
            break
        
    #State of the program after the  for loop has been executed: `sum`, `limit`, `n`, `i`, `k`, `A` is a list with at least `m` elements where `m` is the number of elements in `A` processed until `target` is less than or equal to 0; `s` is less than `target` before the loop starts; `selected` contains the second elements of the tuples from `A` processed until `target` is less than or equal to 0; `target` has been decreased by the sum of the first elements of the tuples in `A` processed until `target` is less than or equal to 0.
    print(len(selected))
    print(' '.join(map(str, selected)))
#Overall this is what the function does:The function reads two integers, `target` and `n`, from input, calculates a list of tuples based on powers of two and their corresponding indices, and then attempts to select indices whose corresponding powers of two sum to at least `target`. If the sum of all possible powers of two is less than `target`, it outputs -1. If a sufficient sum is found, it prints the number of selected indices and their values. The function does not accept parameters directly and relies on user input for the values of `target` and `n`.

