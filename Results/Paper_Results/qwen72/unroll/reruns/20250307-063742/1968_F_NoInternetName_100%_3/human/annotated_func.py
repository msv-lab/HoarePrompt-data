#State of the program right berfore the function call: cast is a callable that can convert strings to the desired type (e.g., int, float).
def func_1(cast):
    return map(cast, input().split())
    #The program returns an iterator that applies the `cast` function to each element in the list of strings obtained by splitting the user input.
#Overall this is what the function does:The function `func_1` accepts a callable `cast` and returns an iterator that applies the `cast` function to each element in the list of strings obtained by splitting the user input. The user input is expected to be a single line of space-separated values. The final state of the program after the function concludes is that the returned iterator is ready to be consumed, yielding the results of applying `cast` to each string in the input.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean.
def func_2(arr, predicate):
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: `l` is the largest index such that `predicate(arr[l])` is `True`, and `r` is the smallest index such that `predicate(arr[r])` is `False`.
    if predicate(arr[l]) :
        return l
        #The program returns the largest index `l` such that `predicate(arr[l])` is `True`.
    #State: `l` is the largest index such that `predicate(arr[l])` is `True`, and `r` is the smallest index such that `predicate(arr[r])` is `False`. Additionally, `predicate(arr[l])` is `False`.
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and a predicate function `predicate`. It returns the largest index `l` where `predicate(arr[l])` is `True`. If no such index exists, it returns `None`.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes a list of integers and returns a boolean value.
def func_3(arr, predicate):
    return func_2(arr, predicate)
    #The program returns the result of `func_2` applied to `arr` and `predicate`. The result is a boolean value, which is determined by the `predicate` function based on the elements in the list `arr`.
#Overall this is what the function does:The function `func_3` accepts a list of integers `arr` and a predicate function `predicate`. It returns the boolean result of applying the `predicate` function to `arr`. The final state of the program includes the returned boolean value, which reflects whether the predicate condition is met by the elements in `arr`.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean.
def func_4(arr, predicate):
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program returns the value of `result` plus 1, where `result` is the value returned by `func_2(arr, predicate)` and is not `None`.
    #State: *`arr` is a list of integers, `predicate` is a function that takes an integer and returns a boolean, `result` is the value returned by `func_2(arr, predicate)`, and `result` is `None`
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_4` accepts a list of integers `arr` and a predicate function `predicate`. It calls `func_2(arr, predicate)` and if `func_2` returns a non-None value, `func_4` returns that value plus 1. If `func_2` returns `None`, `func_4` returns `None`.

#State of the program right berfore the function call: n and q are integers such that 2 ≤ n ≤ 2 · 10^5 and 1 ≤ q ≤ 2 · 10^5. a is a list of n integers where 0 ≤ a_i < 2^30. l and r are integers such that 1 ≤ l < r ≤ n.
def func_5():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: `n` and `q` remain unchanged, `a` remains unchanged, `l` and `r` remain unchanged, `x` is a list of integers where each element is the cumulative XOR of the elements in `a` up to that point, and `inds` is a defaultdict with lists as values, where each key in `inds` corresponds to a value in `x` and the list contains the indices at which that value appears in `x`.
    for i in range(q):
        l, r = func_1(int)
        
        if x[l - 1] == x[r]:
            print('Yes')
            continue
        
        lower = inds[x[r]][func_4(inds[x[r]], lambda arg: arg < l) or 0]
        
        upper = inds[x[l - 1]][func_3(inds[x[l - 1]], lambda arg: arg <= r)]
        
        if upper > lower:
            print('Yes')
        else:
            print('No')
        
    #State: The values of `n`, `q`, `a`, `l`, and `r` remain unchanged. The list `x` and the defaultdict `inds` also remain unchanged. The loop prints 'Yes' or 'No' for each iteration based on the conditions specified in the loop body.
#Overall this is what the function does:The function `func_5` processes a list of integers `a` of length `n` and a number of queries `q`. For each query, it checks if the cumulative XOR of the elements in `a` from the start up to index `l-1` is equal to the cumulative XOR up to index `r`. If they are equal, or if there exists a subarray within the specified range where the cumulative XOR is the same, it prints 'Yes'. Otherwise, it prints 'No'. The function does not modify the input parameters `n`, `q`, `a`, `l`, or `r`, and it does not return any value.

