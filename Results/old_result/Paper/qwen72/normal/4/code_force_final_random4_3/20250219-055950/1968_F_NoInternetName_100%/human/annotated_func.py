#State of the program right berfore the function call: cast is a function that can be applied to the elements of the input, typically an int or str function.
def func_1(cast):
    return map(cast, input().split())
    #The program returns an iterator that applies the `cast` function to each element of the input string, which is split by spaces.
#Overall this is what the function does:The function `func_1` accepts a parameter `cast`, which is a function (like `int` or `str`). It reads a line of input from the user, splits the input string by spaces, and returns an iterator that applies the `cast` function to each element of the split input. The final state of the program includes the returned iterator, which can be used to iterate over the casted elements of the input string.

#State of the program right berfore the function call: arr is a list of integers, predicate is a function that takes an integer and returns a boolean.
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
        #The program returns the largest index `l` such that `predicate(arr[l])` is true, and `l + 1 == r` where `r` is the smallest index such that `predicate(arr[r])` is false.
    #State: *`arr` is a list of integers, `predicate` is a function that takes an integer and returns a boolean, `l` is the largest index such that `predicate(arr[l])` is true, `r` is the smallest index such that `predicate(arr[r])` is false, and `l + 1 == r`. Additionally, `predicate(arr[l])` is false.
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and a predicate function `predicate`. It returns the largest index `l` in `arr` where `predicate(arr[l])` is true, and the next index `l + 1` is the smallest index where `predicate(arr[l + 1])` is false. If no such index exists, it returns `None`. The input list `arr` and the predicate function `predicate` remain unchanged after the function call.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes a list of integers and returns a boolean value.
def func_3(arr, predicate):
    return func_2(arr, predicate)
    #The program returns the result of calling `func_2` with the list `arr` and the function `predicate`. The result is a boolean value determined by `predicate` when applied to `arr`.
#Overall this is what the function does:The function `func_3` accepts two parameters: `arr`, which is a list of integers, and `predicate`, which is a function that takes a list of integers and returns a boolean value. It returns the boolean result of applying the `predicate` function to the list `arr`. The state of the program after the function concludes is that `arr` remains unchanged, and the return value is the boolean result of the `predicate` function applied to `arr`.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes a list of integers and returns a boolean value.
def func_4(arr, predicate):
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program returns the value of `result` plus 1, where `result` is the value returned by `func_2(arr, predicate)` and is not `None`.
    #State: *`arr` is a list of integers, `predicate` is a function that takes a list of integers and returns a boolean value, `result` is the value returned by `func_2(arr, predicate)`, and `result` is `None`
    return None
    #The program returns `None`.
#Overall this is what the function does:The function `func_4` accepts a list of integers `arr` and a predicate function `predicate`. It returns the value of `result` plus 1 if `func_2(arr, predicate)` returns a non-None value. If `func_2(arr, predicate)` returns `None`, the function returns `None`. The state of `arr` and `predicate` remains unchanged after the function call.

#State of the program right berfore the function call: n and q are non-negative integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5. a is a list of integers of length n, where each element a_i satisfies 0 <= a_i < 2^30. l and r are non-negative integers such that 1 <= l < r <= n.
def func_5():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: `n` and `q` are the values returned by `func_1(int)`, `a` is a list of integers of length `n` where each element `a_i` satisfies 0 <= `a_i` < 2^30, `l` and `r` are non-negative integers such that 1 <= `l` < `r` <= `n`, `x` is a list containing the integers 0 and the cumulative XOR of the elements of `a` up to each index, `inds` is a defaultdict of lists where each key is an element in `x` and the corresponding value is a list of indices in `x` where that key appears.
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
        
    #State: `n` and `q` are the values returned by `func_1(int)`, `a` is a list of integers of length `n` where each element `a_i` satisfies 0 <= `a_i` < 2^30, `x` is a list containing the integers 0 and the cumulative XOR of the elements of `a` up to each index, `inds` is a defaultdict of lists where each key is an element in `x` and the corresponding value is a list of indices in `x` where that key appears, `i` is equal to `q`, and the loop has completed all its iterations. For each iteration, `l` and `r` were the values returned by `func_1(int)`, `lower` was the smallest index in `inds[x[r]]` that is less than `l` or 0 if no such index exists, and `upper` was the largest index in `inds[x[l - 1]]` that is less than or equal to `r` or 0 if no such index exists. The program printed 'Yes' if `upper` > `lower` and 'No' otherwise.
#Overall this is what the function does:The function `func_5` processes a list `a` of integers and a series of queries `q`. For each query, it checks if the cumulative XOR from the start of the list up to index `l-1` is equal to the cumulative XOR up to index `r`. If they are equal, or if there exists a subsequence within the specified range that satisfies certain conditions, it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value. After the function concludes, the list `a` remains unchanged, and the cumulative XOR list `x` and the index dictionary `inds` are populated based on the elements of `a`. The function has processed all `q` queries.

