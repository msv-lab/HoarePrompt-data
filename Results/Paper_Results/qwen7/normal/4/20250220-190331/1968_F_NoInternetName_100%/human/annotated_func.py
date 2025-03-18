#State of the program right berfore the function call: cast is a callable that can convert strings to integers, and the input is a space-separated sequence of integers representing the array elements or query ranges.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object that applies the 'cast' function to each element in the input string split by spaces. Each element is assumed to be a string representation of an integer.
#Overall this is what the function does:The function accepts a callable parameter `cast` that converts strings to integers. It reads a space-separated sequence of strings from input, converts each string to an integer using the `cast` function, and returns a map object containing these integers.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer as input and returns a boolean.
def func_2(arr, predicate):
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: Output State: `arr` is a list of integers, `l` is either `mid` or 0, `r` is greater than `l + 1`, and `mid` is now `(l + r) // 2`. If `predicate(arr[mid])` is true, then `l` is updated to `(l + r) // 2`. Otherwise, `l` is 0 and `r` is updated to `mid`.
    #
    #This final state indicates that the loop continues to narrow down the search range by updating `l` and `r` based on the result of the predicate function applied to the middle element of the current range. The process repeats until the condition `l + 1 >= r` is met, meaning the search range has been reduced to a single element or the loop has determined that no element satisfies the predicate.
    if predicate(arr[l]) :
        return l
        #The program returns the updated value of `l`, which is now `(l + r) // 2`
    #State: Postcondition: `arr` is a list of integers, `l` is either `mid` or 0, `r` is greater than `l + 1`, and `mid` is now `(l + r) // 2`. The predicate function `predicate(arr[mid])` is false, and `l` is 0 while `r` is updated to `mid`.
    return None
    #The program returns None
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and a predicate function `predicate`. It uses binary search to find the leftmost index where the predicate function returns `True`. If such an index exists, the function returns it; otherwise, it returns `None`.

#State of the program right berfore the function call: arr is a list of integers where each element is in the range [0, 2^30), and predicate is a function that takes an integer and returns a boolean.
def func_3(arr, predicate):
    return func_2(arr, predicate)
    #The program returns a boolean value determined by the function `func_2` applied to the list `arr` and the predicate function.
#Overall this is what the function does:The function accepts a list of integers `arr` and a predicate function. It applies the predicate function to each element in `arr` and returns `True` if all elements satisfy the predicate, otherwise it returns `False`.

#State of the program right berfore the function call: arr is a list of integers where each element is in the range [0, 2^30), and predicate is a function that takes an integer and returns a boolean.
def func_4(arr, predicate):
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program returns the value of `result` plus 1, where `result` is the return value of `func_2(arr, predicate)`
    #State: `arr` is a list of integers where each element is in the range [0, 2^30), `result` is None
    return None
    #The program returns None
#Overall this is what the function does:The function `func_4` accepts a list `arr` of integers and a predicate function `predicate`. It calls another function `func_2` with these arguments. If `func_2` returns a non-None value, the function returns that value incremented by one. If `func_2` returns None, the function returns None.

#State of the program right berfore the function call: n and q are positive integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5. a is a list of integers where each element is in the range 0 <= a_i < 2^30. l and r are positive integers such that 1 <= l < r <= n for each query.
def func_5():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: Output State: The loop will iterate over each element in the list `a`. After all iterations, the list `x` will contain the cumulative XOR results of all elements in `a`, starting from the initial value of `x` which is `[0]`. Specifically, `x` will be transformed as follows: `x[0] = 0`, and for each subsequent index `i`, `x[i]` will be the cumulative XOR of all elements in `a` up to the `i-1`th element. The dictionary `inds` will map each value in `x` (excluding the initial `0`) to a list of indices where that value appears in `x`.
    #
    #In natural language, after all iterations of the loop, the list `x` will contain the cumulative XOR of all elements in `a`, starting from 0, and `inds` will store the indices of each unique value in `x` that results from the XOR operations.
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
        
    #State: The loop has completed all its iterations. `i` is equal to `q`, `x` contains the cumulative XOR results of all elements in `a`, starting from 0. Specifically, `x[0]` is 0, and for each subsequent index `i`, `x[i]` is the cumulative XOR of all elements in `a` up to the `i-1`th element. `inds` is a dictionary that maps each unique value in `x` (excluding the initial `0`) to a list of indices where that value appears in `x`.
#Overall this is what the function does:The function processes a list `a` of integers and for each query defined by `l` and `r`, it checks if the cumulative XOR of the sublist `a[l:r]` is zero. If the cumulative XOR is zero, it prints 'Yes'; otherwise, it prints 'No'. The function also maintains a dictionary `inds` that tracks the indices of each unique cumulative XOR value in the list `x`.

