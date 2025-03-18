#State of the program right berfore the function call: cast is a callable function that can convert strings to a desired data type (e.g., int, float), and it is applied to the result of input().split() which returns a list of strings.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object that applies the callable function 'cast' to each element of the list obtained from the user input split by spaces.
#Overall this is what the function does:The function accepts a callable function `cast` and processes user input by splitting it into a list of strings. It then applies the `cast` function to each element of this list, resulting in a map object that contains the transformed values.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer as input and returns a boolean.
def func_2(arr, predicate):
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: l is the index of the smallest element in arr that satisfies the predicate, or l is equal to the length of arr if no such element exists.
    if predicate(arr[l]) :
        return l
        #The program returns the index of the smallest element in the list `arr` that satisfies the predicate, or the length of `arr` if no such element exists.
    #State: l is the index of the smallest element in arr that does not satisfy the predicate, or l is equal to the length of arr if no such element exists
    return None
    #None
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and a predicate function that takes an integer and returns a boolean. It performs a binary search to find the index of the smallest element in `arr` that satisfies the predicate. If such an element exists, it returns its index; otherwise, it returns the length of `arr`. If no element satisfies the predicate, it returns `None`.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer as input and returns a boolean.
def func_3(arr, predicate):
    return func_2(arr, predicate)
    #The program returns the result of calling `func_2` with `arr` and `predicate` as arguments.
#Overall this is what the function does:The function accepts a list of integers (`arr`) and a predicate function (`predicate`) as inputs. It then calls another function (`func_2`) with these inputs and returns the result of that call. The final state of the program is that it has returned either `True` or `False` based on the output of `func_2`.

#State of the program right berfore the function call: arr is a list of integers, predicate is a function that takes an integer and returns a boolean.
def func_4(arr, predicate):
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program returns the value of `result` plus 1, where `result` is the return value of `func_2(arr, predicate)` and is not None
    #State: arr is a list of integers, predicate is a function that takes an integer and returns a boolean, result is `None`
    return None
    #The program returns None
#Overall this is what the function does:The function `func_4` accepts a list of integers `arr` and a predicate function `predicate`. It calls another function `func_2(arr, predicate)`. If `func_2` returns a non-None value, `func_4` returns that value incremented by one. If `func_2` returns `None`, `func_4` returns `None`.

#State of the program right berfore the function call: n and q are positive integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5. a is a list of integers where each element is in the range [0, 2^30). l and r are positive integers such that 1 <= l < r <= n for each query.
def func_5():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: Output State: `inds` is a defaultdict where the default factory is list, `n` is a positive integer such that 2 <= n <= 2 * 10^5, `q` is a positive integer such that 1 <= q <= 2 * 10^5, `a` is a list of integers where each element is in the range [0, 2^30), `l` and `r` are positive integers such that 1 <= l < r <= n for each query, `x` is a list where each element is the result of XORing the previous element with the corresponding element from list `a`, and `inds[0]` contains a list of indices where the value 0 appears in list `x`. Each index in `inds[0]` corresponds to the position in list `x` where the cumulative XOR operation results in 0.
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
        
    #State: The output state will consist of 'Yes' or 'No' printed for each query based on the conditions inside the loop. Specifically, for each query (i) in the range of q, if either of the following conditions is met:
    #1. The elements at positions l-1 and r in list x are equal.
    #2. There exists an index in the range [l, r] where the cumulative XOR operation results in 0 and the upper bound is greater than the lower bound.
#Overall this is what the function does:The function processes a list `a` of integers using cumulative XOR operations and then handles `q` queries. For each query defined by indices `l` and `r`, it checks if the elements at positions `l-1` and `r` in the cumulative XOR list `x` are equal or if there exists an index within the range `[l, r]` where the cumulative XOR operation results in 0. If either condition is met, it prints 'Yes'; otherwise, it prints 'No'. The function takes two positive integers `n` and `q` (with constraints 2 ≤ n ≤ 2 * 10^5 and 1 ≤ q ≤ 2 * 10^5), a list `a` of integers (each in the range [0, 2^30]), and for each query, two more positive integers `l` and `r` (with constraints 1 ≤ l < r ≤ n). The function does not return any value but prints 'Yes' or 'No' for each query.

