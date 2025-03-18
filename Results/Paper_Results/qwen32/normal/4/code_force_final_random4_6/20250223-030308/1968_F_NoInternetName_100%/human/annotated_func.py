#State of the program right berfore the function call: cast is a callable function that can convert strings to a specified type, such as int or float.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object that applies the function 'cast' to each element of the list created by splitting the input string.
#Overall this is what the function does:The function `func_1` takes a callable `cast` as an argument and returns a map object that applies the `cast` function to each element of a list created by splitting an input string.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean value.
def func_2(arr, predicate):
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: `l` is the largest index such that `predicate(arr[l])` is `True`, and `r` is `l + 1`.
    if predicate(arr[l]) :
        return l
        #The program returns `l` which is the largest index such that `predicate(arr[l])` is `True`.
    #State: `l` is the largest index such that `predicate(arr[l])` is `True`, and `r` is `l + 1`. Additionally, `predicate(arr[l])` is `False`.
    return None
    #The program returns None
#Overall this is what the function does:The function `func_2` takes a list of integers `arr` and a predicate function `predicate` that returns a boolean. It returns the largest index `l` in `arr` for which `predicate(arr[l])` is `True`. If no such index exists, it returns `None`.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes a list as input and returns a value.
def func_3(arr, predicate):
    return func_2(arr, predicate)
    #The program returns the result of func_2(arr, predicate)
#Overall this is what the function does:The function `func_3` accepts a list of integers `arr` and a function `predicate` as parameters. It returns the result of calling another function `func_2` with `arr` and `predicate` as arguments.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean value.
def func_4(arr, predicate):
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program attempts to return `result + 1`, which would result in a TypeError as you cannot add an integer to a list directly.
    #State: `arr` is a list of integers, `predicate` is a function that takes an integer and returns a boolean value, `result` is `None`
    return None
    #The program returns None
#Overall this is what the function does:The function `func_4` takes a list of integers `arr` and a predicate function `predicate`. It calls another function `func_2` with these parameters. If `func_2` returns a non-None value, the function attempts to add 1 to this value and return it, which could lead to a TypeError if the returned value is not an integer. If `func_2` returns `None`, or if a TypeError occurs, the function returns `None`.

#State of the program right berfore the function call: n and q are integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5, a is a list of integers of length n where each element a_i satisfies 0 <= a_i < 2^30, l and r are integers such that 1 <= l < r <= n.
def func_5():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: `n` and `q` are new integers returned by `func_1`, `a` is a new list of integers returned by `func_1(int)`, `l` and `r` are integers such that 1 <= `l` < `r` <= `n`, `x` is a list containing `n+1` elements where the first element is `0` and each subsequent element is the cumulative XOR of the elements in `a` up to that point, `inds` is a defaultdict of lists where each key is a unique value in `x` and the value is a list of indices in `x` where that value appears.
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
        
    #State: `i` is equal to `q`; `l` and `r` are the values returned by `func_1(int)` in the last iteration; `lower` is `inds[x[r]][func_4(inds[x[r]], lambda arg: arg < l) or 0]` from the last iteration; `upper` is `inds[x[l - 1]][func_3(inds[x[l - 1]], lambda arg: arg <= r)]` from the last iteration. The values of `n`, `a`, `x`, and `inds` remain unchanged.
#Overall this is what the function does:The function `func_5` processes a list of integers `a` of length `n` and a series of `q` queries, each defined by a pair of integers `l` and `r`. For each query, it determines whether there exists a subarray `a[l-1:r]` whose XOR is zero and prints "Yes" if such a subarray exists, otherwise it prints "No".

