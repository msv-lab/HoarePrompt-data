#State of the program right berfore the function call: cast is a callable that can be used to convert strings to a specific type (e.g., int, float).
def func_1(cast):
    return map(cast, input().split())
    #The program returns an iterator that applies the `cast` function to each element in the list of strings obtained by splitting the input.
#Overall this is what the function does:The function `func_1` accepts a callable `cast` and returns an iterator. This iterator applies the `cast` function to each element in the list of strings obtained by splitting an input string provided by the user. The final state of the program is that it has an iterator ready to be consumed, which will yield the converted values as specified by the `cast` function.

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
    #State: *`l` is the largest index such that `predicate(arr[l])` is `True`, and `r` is the smallest index such that `predicate(arr[r])` is `False`. Additionally, `predicate(arr[l])` is `False`.
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and a predicate function `predicate`. It returns the largest index `l` such that `predicate(arr[l])` is `True`. If no such index exists, it returns `None`.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes a list of integers and returns a boolean value.
def func_3(arr, predicate):
    return func_2(arr, predicate)
    #The program returns the result of calling `func_2` with the list `arr` and the function `predicate`. The result is a boolean value based on the evaluation of `predicate` on `arr`.
#Overall this is what the function does:The function `func_3` accepts a list of integers `arr` and a predicate function `predicate`. It returns the boolean result of evaluating `predicate` on `arr`. The state of the program after the function concludes is that `arr` remains unchanged, and the return value is a boolean indicating the result of the predicate evaluation.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean.
def func_4(arr, predicate):
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program returns the value of `result` plus 1, where `result` is the output of `func_2(arr, predicate)` and is not `None`.
    #State: *`arr` is a list of integers, `predicate` is a function that takes an integer and returns a boolean, `result` is the output of `func_2(arr, predicate)`, and `result` is `None`
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_4` accepts a list of integers `arr` and a predicate function `predicate`. It returns the output of `func_2(arr, predicate)` plus 1 if `func_2(arr, predicate)` returns a non-None value. If `func_2(arr, predicate)` returns `None`, `func_4` returns `None`. The function does not modify the input list `arr` or the predicate function.

#State of the program right berfore the function call: n and q are integers such that 2 ≤ n ≤ 2 · 10^5 and 1 ≤ q ≤ 2 · 10^5. a is a list of integers of length n, where each element a_i satisfies 0 ≤ a_i < 2^30. l and r are integers such that 1 ≤ l < r ≤ n.
def func_5():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: `a` is a list of integers returned by `func_1(int)`, `n` and `q` are integers returned by `func_1(int)`, `l` and `r` are integers such that 1 ≤ `l` < `r` ≤ `n`, `x` is a list containing the cumulative XOR of the elements in `a` starting from 0, `inds` is a defaultdict of lists where each key is an XOR value from `x` and the corresponding value is a list of indices where that XOR value appears in `x`.
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
        
    #State: The values of `a`, `n`, `q`, `x`, and `inds` remain unchanged. The loop iterates `q` times, and for each iteration, it prints 'Yes' or 'No' based on the conditions specified in the loop body.
#Overall this is what the function does:The function `func_5` processes a list of integers `a` of length `n` and answers `q` queries about sublists of `a`. For each query defined by indices `l` and `r` (where 1 ≤ l < r ≤ n), it checks if the cumulative XOR from the start of the list up to index `l-1` is equal to the cumulative XOR up to index `r`. If they are equal, it prints 'Yes'. Otherwise, it checks if there is an index in the list `inds` (which maps cumulative XOR values to their indices) that satisfies certain conditions. If these conditions are met, it prints 'Yes'; otherwise, it prints 'No'. The function does not return any values, and the state of `a`, `n`, `q`, `x`, and `inds` remains unchanged after the function execution.

