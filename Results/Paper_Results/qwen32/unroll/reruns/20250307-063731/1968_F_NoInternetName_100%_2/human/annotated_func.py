#State of the program right berfore the function call: cast is a function that can be applied to each element of the input string split by spaces, typically used to convert strings to integers.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object that contains the result of applying the `cast` function to each element of the input string split by spaces.
#Overall this is what the function does:The function `func_1` takes a function `cast` as a parameter, reads an input string, splits it into elements by spaces, applies the `cast` function to each element, and returns a map object containing the results.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean value. The variables l and r are initialized to 0 and the length of arr, respectively, and are used to perform a binary search on arr.
def func_2(arr, predicate):
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: 
    if predicate(arr[l]) :
        return l
        #The program returns the index `l`, which is the index of an element in the array `arr` that satisfies the predicate `predicate(arr[l])`.
    #State: `arr` is a list, `l` is an index within the bounds of `arr`, and `predicate(arr[l])` is false
    return None
    #The program returns None
#Overall this is what the function does:The function `func_2` takes a list of integers `arr` and a predicate function `predicate` as input. It performs a binary search on `arr` to find an element that satisfies the `predicate`. If such an element is found, it returns the index of that element. If no element satisfies the `predicate`, it returns `None`.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an array as an argument.
def func_3(arr, predicate):
    return func_2(arr, predicate)
    #The program returns the result of `func_2(arr, predicate)`, where `arr` is a list of integers and `predicate` is a function that takes an array as an argument.
#Overall this is what the function does:The function `func_3` takes a list of integers `arr` and a function `predicate` as arguments, and returns the result of calling `func_2` with these same arguments.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes a list of integers as input and returns an integer or None.
def func_4(arr, predicate):
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program returns the value of `result` plus 1, where `result` is the output of `func_2(arr, predicate)` and is not None.
    #State: `arr` is a list of integers, `predicate` is a function that takes a list of integers as input and returns an integer or None, `result` is the output of `func_2(arr, predicate)`. `result` is None
    return None
    #The program returns None
#Overall this is what the function does:The function `func_4` takes a list of integers `arr` and a predicate function `predicate` as input. It applies the predicate to `arr` and returns the result of the predicate plus one if the result is not `None`. If the result is `None`, it returns `None`.

#State of the program right berfore the function call: n and q are integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5, a is a list of integers of length n where each integer is in the range 0 <= a_i < 2^30, l and r are integers such that 1 <= l < r <= n.
def func_5():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: `x` is a list of length `n + 1` where each element is the cumulative XOR result up to that point, starting with `0`. `inds` is a defaultdict where each key is a unique XOR result found in `x`, and the value is a list of indices in `x` where that result appears.
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
        
    #State: `x` is a list of length `n + 1` where each element is the cumulative XOR result up to that point, starting with `0`. `inds` is a defaultdict where each key is a unique XOR result found in `x`, and the value is a list of indices in `x` where that result appears.
#Overall this is what the function does:The function `func_5` processes a list of integers and a series of queries. For each query, it determines whether a specific subarray can be partitioned into two non-empty subarrays with equal XOR values. It prints "Yes" if such a partition is possible for the subarray defined by the query, otherwise it prints "No".

