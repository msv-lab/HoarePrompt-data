#State of the program right berfore the function call: cast is a callable that can convert a string to a specific type (e.g., int, float).
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object that applies the `cast` function to each element of the input string split by spaces. The `cast` function can convert a string to a specific type (e.g., int, float).
#Overall this is what the function does:The function `func_1` accepts a callable `cast` and returns a map object that applies the `cast` function to each element of an input string, which is split by spaces. The `cast` function is expected to convert strings to a specific type (e.g., int, float). The final state of the program includes a map object that contains the converted elements from the input string.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean.
def func_2(arr, predicate):
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: `l` is the largest index in `arr` such that `predicate(arr[l])` is `True`, and `r` is the smallest index in `arr` such that `predicate(arr[r])` is `False` or `r` is the length of `arr` if no such index exists.
    if predicate(arr[l]) :
        return l
        #The program returns the largest index `l` in `arr` such that `predicate(arr[l])` is `True`.
    #State: `l` is the largest index in `arr` such that `predicate(arr[l])` is `True`, and `r` is the smallest index in `arr` such that `predicate(arr[r])` is `False` or `r` is the length of `arr` if no such index exists. Additionally, `predicate(arr[l])` is `False`.
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and a predicate function `predicate`. It returns the largest index `l` in `arr` where `predicate(arr[l])` is `True`. If no such index exists, it returns `None`.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes a list of integers and returns a boolean value.
def func_3(arr, predicate):
    return func_2(arr, predicate)
    #The program returns the result of `func_2` when it is called with `arr` and `predicate` as arguments.
#Overall this is what the function does:The function `func_3` accepts a list of integers `arr` and a predicate function `predicate`, and returns the result of calling `func_2` with `arr` and `predicate` as arguments. The final state of the program is that the return value of `func_2` is returned to the caller.

#State of the program right berfore the function call: arr is a list of integers, predicate is a function that takes an integer as input and returns a boolean.
def func_4(arr, predicate):
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program returns the value of `result` plus 1, where `result` is the value returned by `func_2(arr, predicate)`, and `result` is an integer that is not `None`.
    #State: *`arr` is a list of integers, `predicate` is a function that takes an integer as input and returns a boolean, `result` is the value returned by `func_2(arr, predicate)`, and `result` is `None`
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_4` accepts a list of integers `arr` and a predicate function `predicate`. It returns `result + 1` if `func_2(arr, predicate)` returns an integer `result` that is not `None`. Otherwise, it returns `None`. The function does not modify the input `arr` or `predicate`.

#State of the program right berfore the function call: n and q are integers such that 2 ≤ n ≤ 2 · 10^5 and 1 ≤ q ≤ 2 · 10^5. a is a list of integers of length n, where 0 ≤ a_i < 2^30. l and r are integers such that 1 ≤ l < r ≤ n.
def func_5():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: `n` and `q` remain unchanged, `a` remains unchanged, `l` and `r` remain unchanged, `x` is a list of integers where `x[i]` is the cumulative XOR of the first `i` elements of `a`, and `inds` is a defaultdict of lists where each key is an integer from the list `x` and the value is a list of indices where this integer appears in `x`.
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
        
    #State: `n` and `q` remain unchanged, `a` remains unchanged, `l` and `r` remain unchanged, `x` remains unchanged, `inds` remains unchanged.
#Overall this is what the function does:The function `func_5` processes a list of integers `a` of length `n` and a series of `q` queries. Each query consists of two integers `l` and `r`. The function computes a cumulative XOR list `x` from `a` and a dictionary `inds` mapping each cumulative XOR value to the indices where it appears in `x`. For each query, it checks if the cumulative XOR from the start to `l-1` is equal to the cumulative XOR from the start to `r`. If they are equal, it prints 'Yes'. Otherwise, it finds the largest index less than `l` and the smallest index greater than or equal to `r` where the cumulative XOR values match, and if the latter is greater than the former, it prints 'Yes'; otherwise, it prints 'No'. The function does not modify `n`, `q`, `a`, `l`, or `r`.

