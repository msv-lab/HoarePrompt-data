#State of the program right berfore the function call: cast is a callable that can convert a string to a specific type (e.g., int, float).
def func_1(cast):
    return map(cast, input().split())
    #The program returns an iterator that applies the `cast` function to each element in the list of strings obtained by splitting the input. Each element in the iterator is the result of converting a string from the input to the specific type defined by `cast`.
#Overall this is what the function does:The function `func_1` accepts a callable `cast` and returns an iterator. This iterator applies the `cast` function to each element in a list of strings obtained by splitting a line of input provided by the user. The final state of the program is that it has an iterator where each element is the result of converting a string from the input to the specific type defined by `cast`.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean.
def func_2(arr, predicate):
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: The loop will terminate with `l` and `r` such that `l + 1 == r`. The value of `l` will be the largest index in `arr` for which `predicate(arr[l])` is `True`, and `r` will be the smallest index in `arr` for which `predicate(arr[r])` is `False`. If no such indices exist, `l` will be the index of the last element for which `predicate` is `True`, and `r` will be the index of the first element for which `predicate` is `False`.
    if predicate(arr[l]) :
        return l
        #The program returns the largest index `l` in `arr` for which `predicate(arr[l])` is `True`. If no such index exists, it returns the index of the last element for which `predicate` is `True`.
    #State: The loop will terminate with `l` and `r` such that `l + 1 == r`. The value of `l` will be the largest index in `arr` for which `predicate(arr[l])` is `True`, and `r` will be the smallest index in `arr` for which `predicate(arr[r])` is `False`. If no such indices exist, `l` will be the index of the last element for which `predicate` is `True`, and `r` will be the index of the first element for which `predicate` is `False`. Additionally, `predicate(arr[l])` is `False`.
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and a predicate function `predicate`. It returns the largest index `l` in `arr` where `predicate(arr[l])` is `True`. If no elements in `arr` satisfy the predicate, it returns `None`.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes a list of integers as an argument and returns a boolean value.
def func_3(arr, predicate):
    return func_2(arr, predicate)
    #The program returns the result of `func_2` applied to the list `arr` and the function `predicate`. The exact value depends on the implementation of `func_2` and the behavior of `predicate` when applied to `arr`.
#Overall this is what the function does:The function `func_3` accepts a list of integers `arr` and a predicate function `predicate`. It returns the result of applying `func_2` to `arr` and `predicate`. The exact return value depends on the implementation of `func_2` and the behavior of `predicate` when applied to `arr`. After the function concludes, the state of `arr` and `predicate` remains unchanged, and the program has the result of `func_2` applied to the provided arguments.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean.
def func_4(arr, predicate):
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program returns the value of `result` plus 1, where `result` is the value returned by `func_2(arr, predicate)`.
    #State: *`arr` is a list of integers, `predicate` is a function that takes an integer and returns a boolean, `result` is the value returned by `func_2(arr, predicate)`, and `result` is `None`.
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_4` accepts a list of integers `arr` and a predicate function `predicate`. It returns the value of `result` plus 1 if `func_2(arr, predicate)` returns a non-None value. If `func_2(arr, predicate)` returns `None`, `func_4` returns `None`.

#State of the program right berfore the function call: n and q are integers such that 2 ≤ n ≤ 2 · 10^5 and 1 ≤ q ≤ 2 · 10^5, a is a list of integers of length n where 0 ≤ a_i < 2^30, l and r are integers such that 1 ≤ l < r ≤ n.
def func_5():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: `n` must be greater than or equal to the number of elements in `a`, `a` is a list of integers of length `n` where 0 ≤ `a_i` < 2^30, `x` is a list of length `n + 1` where each element is the cumulative XOR of the elements in `a` up to that point, and `inds` is a defaultdict with list as the default factory, where each key in `inds` is an element of `x` and the value is a list of indices where that element appears in `x`.
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
        
    #State: `n` is greater than or equal to the number of elements in `a`, `a` is a list of integers of length `n` where 0 ≤ `a_i` < 2^30, `x` is a list of length `n + 1` where each element is the cumulative XOR of the elements in `a` up to that point, `inds` is a defaultdict with list as the default factory, where each key in `inds` is an element of `x` and the value is a list of indices where that element appears in `x`, `q` is the number of iterations the loop has completed, `i` is `q - 1`, `l` and `r` are the values returned by the last call to `func_1(int)`, `lower` is the first index in `inds[x[r]]` that is less than `l` if such an index exists, otherwise `lower` is 0, `upper` is the last index in `inds[x[l - 1]]` that is less than or equal to `r` if such an index exists, otherwise `upper` is 0. If `upper` > `lower`, the loop or conditional block will proceed to the next iteration or step. If `upper` ≤ `lower`, the loop or conditional block will also proceed to the next iteration or step.
#Overall this is what the function does:The function `func_5` processes a list of integers `a` of length `n` and a series of `q` queries, each defined by a pair of integers `l` and `r` (1 ≤ l < r ≤ n). It computes a cumulative XOR list `x` of length `n + 1` where each element is the cumulative XOR of the elements in `a` up to that point. It also maintains a dictionary `inds` where each key is an element from `x` and the value is a list of indices where that element appears in `x`. For each query, the function checks if the cumulative XOR from the start up to `l-1` is equal to the cumulative XOR up to `r`. If they are equal, it prints 'Yes'. Otherwise, it finds the largest index `upper` in `inds[x[l-1]]` that is less than or equal to `r` and the smallest index `lower` in `inds[x[r]]` that is less than `l`. If `upper` is greater than `lower`, it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value.

