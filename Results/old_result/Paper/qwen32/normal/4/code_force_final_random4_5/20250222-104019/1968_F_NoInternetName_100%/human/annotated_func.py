#State of the program right berfore the function call: cast is a function that can be applied to each element of the input string split by spaces.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object that applies the function `cast` to each element of the input string split by spaces.
#Overall this is what the function does:The function `func_1` takes a function `cast` as an argument, reads a line of input, splits it into substrings based on spaces, and returns a map object that applies the `cast` function to each substring.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean value. The function `func_2` performs a binary search on the list `arr` to find the largest index `l` such that `predicate(arr[l])` is True.
def func_2(arr, predicate):
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: `l` is the index of the last element that was checked, and `r` is `l + 1`.
    if predicate(arr[l]) :
        return l
        #The program returns `l`, which is the index of the last element that was checked.
    #State: `l` is the index of the last element that was checked, and `r` is `l + 1`. The predicate `arr[l]` is false.
    return None
    #The program returns None
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and a predicate function `predicate`. It performs a binary search on `arr` to find the largest index `l` such that `predicate(arr[l])` is True. If such an index `l` exists, the function returns `l`. Otherwise, it returns None.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes a list as an argument.
def func_3(arr, predicate):
    return func_2(arr, predicate)
    #The program returns the result of `func_2(arr, predicate)`
#Overall this is what the function does:The function takes a list of integers `arr` and a predicate function `predicate` as input, and returns the result of applying the predicate function to the list.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean value.
def func_4(arr, predicate):
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program returns the value of `result` plus 1, where `result` is the output of `func_2(arr, predicate)` and is not None.
    #State: `arr` is a list of integers, `predicate` is a function that takes an integer and returns a boolean value, and `result` is the output of `func_2(arr, predicate)`. `result` is `None`.
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_4` takes a list of integers `arr` and a predicate function `predicate`. It returns the value of `result` plus 1, where `result` is the output of `func_2(arr, predicate)` and is not None. If `result` is None, the function returns None.

#State of the program right berfore the function call: n is an integer representing the number of elements in the array, q is an integer representing the number of queries, a is a list of n integers where each integer is in the range [0, 2^30), l and r are integers representing the start and end indices of a subarray such that 1 <= l < r <= n.
def func_5():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: - `a` remains the list returned by `func_1(int)`.
    #- `n` and `q` remain the values returned by `func_1(int)`.
    #- `l` and `r` remain the integers representing the start and end indices of a subarray such that 1 <= l < r <= n.
    #- `x` is `[0] + [cumulative XOR results]` where each element is the XOR of the previous element in `x` with the next element in `a`.
    #- `inds` is a defaultdict of lists where each key is a unique XOR result from `x`, and each value is a list of indices in `x` where that XOR result occurs.
    #
    #Output State:
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
        
    #State: `a` remains the list returned by `func_1(int)`, `n` and `q` remain the values returned by `func_1(int)`, `l` and `r` are the values returned by `func_1(int)` from the last iteration such that `1 <= l < r <= n`, `x` is `[0] + [cumulative XOR results]` where each element is the XOR of the previous element in `x` with the next element in `a`, `inds` is a defaultdict of lists where each key is a unique XOR result from `x`, and each value is a list of indices in `x` where that XOR result occurs, `i` equals `q` indicating all iterations have completed.
#Overall this is what the function does:The function processes a series of queries on an array to determine if the XOR of a specified subarray is zero. It accepts the number of elements in the array, the number of queries, the array itself, and for each query, the start and end indices of a subarray. It prints "Yes" if the XOR of the elements in the subarray is zero, otherwise it prints "No".

