#State of the program right berfore the function call: sum and limit are integers such that 1 ≤ sum, limit ≤ 105.**
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
        
    #State of the program after the  for loop has been executed: `sum` and `limit` are integers such that 1 ≤ `sum`, `limit` ≤ 105; `target` and `n` are assigned values from the input; `A` is a list containing tuples where each tuple consists of a power of 2 calculated from `i-1` and the corresponding `i`; `s` is the sum of all elements in list `A`; `n` is greater than or equal to 1; `i` is not equal to 1 and `k` is equal to the integer logarithm base 2 of `i` for each `i` in the list.
    if (s < target) :
        print(-1)
        exit()
    #State of the program after the if block has been executed: *`sum`, `limit`, `target`, `n`, `A`, `s`, `i`, `k` are integers. If the sum of elements in list `A` is less than `target`, there is no change in the state as the program exits immediately without affecting any variables.
    A.sort()
    selected = []
    for tup in A:
        target -= tup[0]
        
        selected.append(tup[1])
        
        if target <= 0:
            break
        
    #State of the program after the  for loop has been executed: `sum`, `limit`, `n`, `A`, `s`, `i`, `k`, `selected`, `tup`, `target` are integers. The loop has executed at least once with `A` having at least 1 element. If the loop executed fully, `target` is less than or equal to 0, `selected` contains the `tup[1]` values for all tuples until `target` becomes less than or equal to 0. If the loop did not execute, `selected` is an empty list.
    print(len(selected))
    print(' '.join(map(str, selected)))
#Overall this is what the function does:The function `func` reads input values for `target` and `n`, calculates a list `A` where each element is a tuple containing a power of 2 and its corresponding index, then sorts the list `A` and selects elements from it until the sum of the selected elements is greater than or equal to `target`. The selected indices are printed along with their count. If the sum of elements in list `A` is less than `target`, it prints -1 and exits.

