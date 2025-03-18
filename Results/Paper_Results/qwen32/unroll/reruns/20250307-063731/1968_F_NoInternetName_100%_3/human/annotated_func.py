#State of the program right berfore the function call: cast is a callable function that can convert strings to a desired type, such as int or float.
def func_1(cast):
    return map(cast, input().split())
    #The program returns an iterator that applies the function `cast` to each element of the list created by splitting the input string.
#Overall this is what the function does:The function `func_1` takes a callable `cast` as an argument and returns an iterator that applies the `cast` function to each element of a list created by splitting an input string.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean value. The function `func_2` is used to find the largest index `l` in the range `[0, len(arr))` such that `predicate(arr[l])` is True.
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
        #The program returns `l`, which is the largest index such that `predicate(arr[l])` is `True`.
    #State: `l` is the largest index such that `predicate(arr[l])` is `True`, and `r` is the smallest index such that `predicate(arr[r])` is `False`. Additionally, `predicate(arr[l])` is `False`.
    return None
    #The program returns None
#Overall this is what the function does:The function `func_2` takes a list of integers `arr` and a predicate function `predicate`. It returns the largest index `l` in the list such that `predicate(arr[l])` is `True`. If no such index exists, it returns `None`.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes a list as an argument.
def func_3(arr, predicate):
    return func_2(arr, predicate)
    #The program returns the result of func_2(arr, predicate), where arr is a list of integers and predicate is a function that takes a list as an argument.
#Overall this is what the function does:The function accepts a list of integers `arr` and a function `predicate` that takes a list as an argument. It returns the result of applying `predicate` to `arr`.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean value.
def func_4(arr, predicate):
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program returns the integer value of `result` plus 1
    #State: `arr` is a list of integers, `predicate` is a function that takes an integer and returns a boolean value, `result` is the output of `func_2(arr, predicate)` and `result` is `None`.
    return None
    #The program returns None
#Overall this is what the function does:The function `func_4` accepts a list of integers `arr` and a predicate function `predicate`. It returns the integer value of `result` plus 1 if `result` is not `None`; otherwise, it returns `None`.

#State of the program right berfore the function call: n is a positive integer representing the number of elements in the array, q is a positive integer representing the number of queries, a is a list of n integers where each integer is between 0 and 2^30 - 1, l and r are integers representing the start and end indices of the subarray for each query such that 1 <= l < r <= n.
def func_5():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: `n` and `q` are unchanged, `a` is unchanged, `l` and `r` are unchanged, `x` is a list of length `n + 1` where each element is the cumulative XOR up to that point, `inds` is a `defaultdict` mapping each unique XOR result to a list of indices in `x`.
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
        
    #State: `n` and `q` are unchanged, `a` is unchanged, `l` and `r` are unchanged, `x` is a list of length `n + 1` where each element is the cumulative XOR up to that point, `inds` is a `defaultdict` mapping each unique XOR result to a list of indices in `x`.
#Overall this is what the function does:The function processes a list of integers and a series of queries. For each query, it determines if there exists a subarray within the specified range that has a cumulative XOR of zero. It prints "Yes" if such a subarray exists and "No" otherwise. The original list and query parameters remain unchanged throughout the process.

