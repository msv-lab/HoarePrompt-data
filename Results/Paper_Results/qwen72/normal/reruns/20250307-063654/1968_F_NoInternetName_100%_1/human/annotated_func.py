#State of the program right berfore the function call: cast is a function that can be used to cast the input values to a specific type, such as int or float.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object that applies the `cast` function to each element in the list of strings obtained by splitting the input. The input is expected to be a space-separated string of values, and `cast` will convert each value to the specified type (such as int or float).
#Overall this is what the function does:The function `func_1` accepts a parameter `cast` and returns a map object that applies the `cast` function to each element in a list of strings obtained by splitting a space-separated input string. The input is expected to be provided by the user, and each value in the input string will be converted to the specified type (such as int or float) using the `cast` function.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean.
def func_2(arr, predicate):
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: `arr` is a list of integers, `predicate` is a function that takes an integer and returns a boolean, `l` is the largest index such that `predicate(arr[l])` is true, `r` is the smallest index such that `predicate(arr[r])` is false, and `l + 1 == r`.
    if predicate(arr[l]) :
        return l
        #The program returns the largest index `l` such that `predicate(arr[l])` is true.
    #State: *`arr` is a list of integers, `predicate` is a function that takes an integer and returns a boolean, `l` is the largest index such that `predicate(arr[l])` is true, `r` is the smallest index such that `predicate(arr[r])` is false, and `l + 1 == r`. Additionally, `predicate(arr[l])` is false.
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and a predicate function `predicate`. It returns the largest index `l` where `predicate(arr[l])` is true. If no such index exists, it returns `None`.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes a list of integers and returns a boolean.
def func_3(arr, predicate):
    return func_2(arr, predicate)
    #The program returns the result of calling `func_2` with the list `arr` and the function `predicate`. The result is a boolean value determined by the `predicate` function applied to the list `arr`.
#Overall this is what the function does:The function `func_3` accepts a list of integers `arr` and a predicate function `predicate`. It returns a boolean value that is the result of applying `predicate` to `arr`. The function does not modify the input list `arr` or the predicate function `predicate`.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean.
def func_4(arr, predicate):
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program returns the value of `result` plus 1, where `result` is the value returned by `func_2(arr, predicate)` and is not `None`.
    #State: *`arr` is a list of integers, `predicate` is a function that takes an integer and returns a boolean, `result` is the value returned by `func_2(arr, predicate)`, and `result` is `None`
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_4` accepts a list of integers `arr` and a predicate function `predicate`. It calls `func_2(arr, predicate)` and if the result is not `None`, it returns this result incremented by 1. If the result is `None`, it returns `None`.

#State of the program right berfore the function call: n and q are integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5, a is a list of integers of length n where 0 <= a_i < 2^30, l and r are integers for each query such that 1 <= l < r <= n.
def func_5():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: `n` and `q` are integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5, `a` is a list of integers of length `n` where 0 <= a_i < 2^30, `a` is now a list of integers converted from the original `a` using `func_1` and `int`, `x` is a list containing `n + 1` elements where each element is the cumulative XOR of the elements in `a` up to that point, `inds` is a defaultdict of lists where each key is a cumulative XOR value from `x` and the corresponding value is a list of indices where this cumulative XOR value appears in `x`.
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
        
    #State: `i` is `q - 1`, `q` is an integer such that 1 <= q <= 2 * 10^5, `l` and `r` are the values returned by `func_1(int)` in the last iteration, `lower` is the first index in `inds[x[r]]` that is less than `l` or 0 if no such index exists, `upper` is the last index in `inds[x[l - 1]]` that is less than or equal to `r`. If `upper` > `lower`, the condition `upper` > `lower` holds. Otherwise, `upper` is less than or equal to `lower`.
#Overall this is what the function does:The function `func_5` processes a list of integers `a` of length `n` and answers `q` queries. Each query consists of two integers `l` and `r` (1 <= l < r <= n). For each query, the function determines if there exists a subarray within `a[l-1]` to `a[r-1]` whose cumulative XOR is zero. If such a subarray exists, it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value, but it modifies the state by printing the results of the queries. After the function concludes, `n` and `q` remain integers within their original constraints, `a` is a list of integers of length `n`, and `x` and `inds` are internal data structures used for query processing.

