#State of the program right berfore the function call: cast is a callable object (such as int or float) that can be applied to a sequence of string representations of numbers.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object that applies the callable object 'cast' to each element in the sequence of string representations of numbers entered by the user.
#Overall this is what the function does:The function accepts a callable object `cast` and a sequence of string representations of numbers. It applies the `cast` function to each element in the sequence and returns a map object containing the results.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean.
def func_2(arr, predicate):
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: Output State: The list `arr` is a list of integers with at least 2 elements, `l` is either `mid` or 0, `mid` is the final midpoint calculated by `(l + r) // 2`, `r` is the length of `arr`, and it must be greater than `mid + 1`. After all iterations of the loop, the variable `l` will be the index of the smallest element in the subarray defined by `l` and `r-1` that satisfies the predicate, or it will be 0 if no such element exists. The variable `r` will be the original length of the array, indicating the range in which the search was performed.
    if predicate(arr[l]) :
        return l
        #The program returns the index of the smallest element in the subarray defined by 'l' and 'r-1' that satisfies the predicate, or it returns 0 if no such element exists.
    #State: The list `arr` is a list of integers with at least 2 elements, `l` is either `mid` or 0, `mid` is the final midpoint calculated by `(l + r) // 2`, `r` is the original length of `arr` and is greater than `mid + 1`, and the predicate does not hold for `arr[l]`.
    return None
    #The program returns None
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and a predicate function. It performs a binary search to find the index of the smallest element in the specified subarray that satisfies the predicate. If such an element exists, it returns its index; otherwise, it returns `None`.

#State of the program right berfore the function call: n and q are positive integers such that 2 ≤ n ≤ 2⋅10^5 and 1 ≤ q ≤ 2⋅10^5. a is a list of integers where 0 ≤ a_i < 2^{30}. l and r are positive integers such that 1 ≤ l < r ≤ n for each query.
def func_3():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: Output State: `a` is an empty list, `x` is a list where each element is the cumulative bitwise XOR of all elements in `a` up to that point, and `inds[x[-1]]` is a list containing all indices from 0 to the length of `x` - 1.
    #
    #Explanation: After all iterations of the loop have finished, the list `a` will be exhausted since it is iterated over completely. For each element `i` in `a`, the variable `x` appends the current value of `x[-1]` bitwise XORed with `i`. This means that `x` will contain the cumulative bitwise XOR of all elements in `a` up to the current step. The dictionary `inds` maps each value in `x` to a list of indices where that value appears in `x`, which will include all indices from 0 to the length of `x` - 1 because each new value in `x` is added immediately after the previous value.
    for i in range(q):
        l, r = func_1(int)
        
        if x[l - 1] == x[r]:
            print('Yes')
            continue
        
        lower = func_2(inds[x[r]], lambda arg: arg < l) or -1
        
        upper = func_2(inds[x[l - 1]], lambda arg: arg <= r)
        
        lower = inds[x[r]][lower + 1]
        
        upper = inds[x[l - 1]][upper]
        
        if upper > lower and l <= upper <= r and l <= lower <= r:
            print('Yes')
        else:
            print('No')
        
    #State: `i` is equal to `q`, `a` is an empty list, `x` is a list where each element is the cumulative bitwise XOR of all elements in `a` up to that point, and `inds[x[-1]]` is a list containing all indices from 0 to the length of `x` - 1.
#Overall this is what the function does:The function processes a list `a` of integers and handles `q` queries. For each query defined by indices `l` and `r`, it checks if there exists any subarray within `a[l-1:r]` whose cumulative bitwise XOR equals the cumulative bitwise XOR of the entire array `a`. If such a subarray exists, it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value but prints the results for each query.

