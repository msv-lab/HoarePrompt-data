#State of the program right berfore the function call: cast is a callable that can convert strings to a desired data type (e.g., int, float), and it is applied to the input split by spaces.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object that applies the callable 'cast' to each element of the input string split by spaces.
#Overall this is what the function does:The function accepts a callable `cast` as input, which is used to convert strings to a desired data type. It reads a string input, splits it into elements based on spaces, and then applies the `cast` function to each element, resulting in a map object that contains the converted values.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean. The predicate function is used to check if the subarray starting from index l is interesting.
def func_2(arr, predicate):
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: Output State: The loop terminates when `l + 1` is no longer less than `r`.
    #
    #In the final state, `l` will be the index of the smallest element in the list `arr` that satisfies the predicate, or it will be 0 if no such element exists. Similarly, `r` will be the next index after the last element in the list `arr` that does not satisfy the predicate, or it will be the length of `arr` if all elements satisfy the predicate. The variable `mid` will hold the last value used in the binary search process, which is `(l + r) // 2`.
    #
    #This means that after all iterations, the range defined by `l` and `r` will contain the largest interval where the predicate is not satisfied, with `l` being the lower bound and `r` being the upper bound.
    if predicate(arr[l]) :
        return l
        #The program returns the index `l` which is the index of the smallest element in the list `arr` that satisfies the predicate, or it will be 0 if no such element exists.
    #State: The loop terminates when `l + 1` is no longer less than `r`. `l` will be the index of the smallest element in the list `arr` that does not satisfy the predicate, or it will be 0 if no such element exists. Similarly, `r` will be the next index after the last element in the list `arr` that satisfies the predicate, or it will be the length of `arr` if all elements do not satisfy the predicate. The variable `mid` will hold the last value used in the binary search process, which is `(l + r) // 2`.
    return None
    #The program returns None
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and a predicate function. It performs a binary search to find the index of the smallest element in `arr` that satisfies the predicate. If such an element exists, it returns its index; otherwise, it returns `None`.

#State of the program right berfore the function call: (n, q) are positive integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5. a is a list of integers where 0 <= a_i < 2^30 for all 1 <= i <= n. l and r are integers such that 1 <= l < r <= n for each query.
def func_3():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: Output State: `inds[0]` now contains the element from index 1 to the total length of `x`, `x` is a list where the first element is 0, and each subsequent element is the cumulative XOR of all previous elements in `a`.
    #
    #In more detail, after all iterations of the loop have finished, `inds[0]` will contain a list of indices starting from 1 up to the length of `x`. This is because every time the loop runs, it appends the current index (which is the length of `x` minus one) to `inds[0]`. The list `x` will contain `n` elements, where the first element is 0, and each subsequent element is the cumulative XOR of all previously seen elements in the list `a`.
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
        
    #State: After all iterations of the loop have finished, `i` will be equal to `q-1`, `q` remains unchanged, `l` and `r` will be the last return values of `func_1(int)` for the respective iterations, `upper` will be `inds[x[l - 1]][upper]`, and `lower` will be `inds[x[r]][lower + 1]`. If `upper > lower` and `l <= upper <= r` and `l <= lower <= r`, the conditions will hold. Otherwise, the conditions will not hold.
#Overall this is what the function does:The function processes a list `a` of integers and handles `q` queries. For each query defined by `l` and `r`, it checks if there exists an index `i` in the range `[l, r]` such that the cumulative XOR of elements from the start of the list `a` to `i` is zero. If such an index exists, it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value but prints the results of the queries.

