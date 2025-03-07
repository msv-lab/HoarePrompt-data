#State of the program right berfore the function call: cast is a callable function that can convert strings to another type, such as int or float.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object that applies the callable function `cast` to each element of the list obtained by splitting the input string.
#Overall this is what the function does:The function `func_1` takes a callable `cast` as an argument and returns a map object. This map object applies the `cast` function to each element of a list derived from splitting an input string.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes a single integer and returns a boolean value. The function `func_2` performs a binary search on the list `arr` to find the largest index `l` such that `predicate(arr[l])` is True.
def func_2(arr, predicate):
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: `arr` is a list of integers with length greater than 1, `predicate` is a function that takes a single integer and returns a boolean value, `l` is the largest index such that `predicate(arr[l])` is `True`, and `r` is the smallest index such that `predicate(arr[r])` is `False`.
    if predicate(arr[l]) :
        return l
        #The program returns `l`, which is the largest index such that `predicate(arr[l])` is `True`.
    #State: `arr` is a list of integers with length greater than 1, `predicate` is a function that takes a single integer and returns a boolean value, `l` is the largest index such that `predicate(arr[l])` is `True`, and `r` is the smallest index such that `predicate(arr[r])` is `False`. Additionally, `predicate(arr[l])` is `False`.
    return None
    #The program returns None
#Overall this is what the function does:The function `func_2` takes a list of integers `arr` and a predicate function `predicate`. It performs a binary search to find the largest index `l` such that `predicate(arr[l])` is `True`. If such an index exists, it returns `l`; otherwise, it returns `None`.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes a list as an argument.
def func_3(arr, predicate):
    return func_2(arr, predicate)
    #The program returns the result of calling `func_2` with `arr` as the first argument and `predicate` as the second argument.
#Overall this is what the function does:The function `func_3` takes a list of integers `arr` and a predicate function `predicate` as inputs, and returns the result of calling `func_2` with `arr` and `predicate` as arguments.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes a list of integers and returns an integer or None.
def func_4(arr, predicate):
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program returns the value of `result` plus 1, where `result` is the value returned by `func_2(arr, predicate)` and is not None.
    #State: `arr` is a list of integers, `predicate` is a function that takes a list of integers and returns an integer or None, `result` is the value returned by `func_2(arr, predicate)`, and `result` is None
    return None
    #The program returns None
#Overall this is what the function does:The function accepts a list of integers `arr` and a function `predicate`. It applies the `predicate` to `arr`. If the result is not `None`, the function returns the result plus one. Otherwise, it returns `None`.

#State of the program right berfore the function call: n and q are integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5. a is a list of integers of length n where each element satisfies 0 <= a_i < 2^30. l and r are integers such that 1 <= l < r <= n.
def func_5():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: `x` is `[0, a[0], 0, a[2], 0, a[4], ..., 0, a[k-1]]` if `k` is odd, or `[0, a[0], 0, a[2], 0, a[4], ..., a[k-1]]` if `k` is even, and `inds` is a defaultdict where `inds[0]` is `[0, 2, 4, ..., 2*floor(k/2)]` and `inds[a[j]]` is `[j]` for odd `j`.
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
        
    #State: `x` is `[0, a[0], 0, a[2], 0, a[4], ..., 0, a[k-1]]` if `k` is odd, or `[0, a[0], 0, a[2], 0, a[4], ..., a[k-1]]` if `k` is even; `inds` is a defaultdict where `inds[0]` is `[0, 2, 4, ..., 2*floor(k/2)]` and `inds[a[j]]` is `[j]` for odd `j`; `q` is greater than 0; `i` is `q-1`; `l` and `r` are the values returned by `func_1(int)` for the last iteration; `lower` is `inds[x[r]][func_4(inds[x[r]], lambda arg: arg < l) or 0]` for the last iteration; `upper` is `inds[x[l - 1]][func_3(inds[x[l - 1]], lambda arg: arg <= r)]` for the last iteration.
#Overall this is what the function does:The function accepts an integer `n`, an integer `q`, a list `a` of `n` integers, and for each of `q` queries, it accepts two integers `l` and `r` representing a range within `a`. It then determines for each query whether there exists an index `i` in the range `[l, r]` such that the XOR of all elements from the start of the list up to `i` is equal to the XOR of all elements from the start up to `r`. The function outputs "Yes" if such an index exists, otherwise "No".

