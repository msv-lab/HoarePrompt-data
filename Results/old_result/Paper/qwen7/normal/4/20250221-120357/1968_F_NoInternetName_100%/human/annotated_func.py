#State of the program right berfore the function call: cast is a callable object (e.g., int, float), and the input is a space-separated string of integers or other values that can be cast to the specified type.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object containing the casted integers from the input string.
#Overall this is what the function does:The function accepts a callable object `cast` and a space-separated string of integers or other values. It processes the string by splitting it into individual elements, casting each element to the type specified by `cast`, and returns a map object containing these casted integers.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer as input and returns a boolean.
def func_2(arr, predicate):
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: Output State: `arr` is a list of integers, `l` is `mid` from the last iteration, `r` is either `mid` or a value that makes the condition `l + 1 < r` false, and the predicate has been evaluated for all elements between `l` and `r` inclusive, with `l` being the final left boundary and `r` being the final right boundary.
    #
    #In simpler terms, after the loop finishes executing all its iterations, `l` will be the index of the smallest element that satisfies the predicate, and `r` will be the index just beyond the last element that satisfies the predicate, or it could be the point where further division is not possible due to the condition `l + 1 >= r`.
    if predicate(arr[l]) :
        return l
        #The program returns the final left boundary `l` which is the last value `l` was set to before the function returned.
    #State: `arr` is a list of integers, `l` is the index of the smallest element that does not satisfy the predicate, and `r` is the index just beyond the last element that does not satisfy the predicate, or it could be the point where further division is not possible due to the condition `l + 1 >= r`.
    return None
    #The program returns None
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and a predicate function. It uses binary search to find the last index where the predicate function returns `True`. If such an index exists, it returns that index; otherwise, it returns `None`.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean.
def func_3(arr, predicate):
    return func_2(arr, predicate)
    #The program returns a boolean value indicating whether the predicate function returns True for any element in the list 'arr'
#Overall this is what the function does:The function accepts a list of integers `arr` and a predicate function `predicate`. It checks each element in the list `arr` using the predicate function. If the predicate function returns True for any element in the list, the function returns True; otherwise, it returns False.

#State of the program right berfore the function call: arr is a list of integers, predicate is a function that takes an integer and returns a boolean.
def func_4(arr, predicate):
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program returns the value of `result` plus 1, where `result` is the return value of `func_2(arr, predicate)` and is not None.
    #State: `arr` is a list of integers, `predicate` is a function that takes an integer and returns a boolean, `result` is `None`
    return None
    #The program returns None
#Overall this is what the function does:The function accepts a list of integers `arr` and a predicate function `predicate`. It calls another function `func_2(arr, predicate)` and returns the value of `result` plus one if `result` is not `None`. If `func_2(arr, predicate)` returns `None`, the function simply returns `None`.

#State of the program right berfore the function call: (n, q) are positive integers such that 2 ≤ n ≤ 2⋅10^5 and 1 ≤ q ≤ 2⋅10^5. a is a list of integers where 0 ≤ a_i < 2^{30}. l and r are positive integers such that 1 ≤ l < r ≤ n for each query.
def func_5():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: `x` is a list where each element is the cumulative XOR of all elements in `a` up to that point, and `inds[x[-1]]` is a list containing all indices of elements in `x`.
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
        
    #State: `i` is 3, `q` is greater than 0, `l` and `r` are the results of `func_1(int)` for the last iteration, and `upper` is the value of `inds[x[l - 1]][func_3(inds[x[l - 1]], lambda arg: arg <= r)]` for the last iteration.
#Overall this is what the function does:The function accepts two positive integers \( n \) and \( q \), a list of integers \( a \), and processes \( q \) queries. For each query, it checks if there exists an index \( k \) in the range \( l \leq k < r \) such that the cumulative XOR from the start of the list up to index \( k \) is equal to the cumulative XOR from the start of the list up to index \( r \). If such an index exists, it prints 'Yes'; otherwise, it prints 'No'. After processing all queries, the function does not return any value.

