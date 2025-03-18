#State of the program right berfore the function call: cast is a callable that can convert string inputs to the desired type, typically int or float.
def func_1(cast):
    return map(cast, input().split())
    #The program returns an iterator that applies the `cast` function to each element in the list of strings obtained from splitting the user input. Each element in the iterator is the result of converting a string from the input into the type specified by `cast`.
#Overall this is what the function does:The function `func_1` accepts a single parameter `cast`, which is expected to be a callable (e.g., `int`, `float`). It reads a line of input from the user, splits the input into a list of strings based on whitespace, and then returns an iterator. This iterator applies the `cast` function to each string in the list, converting each string to the type specified by `cast`. The final state of the program includes the returned iterator, which can be used to access the converted values one by one.

#State of the program right berfore the function call: arr is a list of integers, predicate is a function that takes an integer and returns a boolean.
def func_2(arr, predicate):
    l, r = 0, len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        
        if predicate(arr[mid]):
            l = mid
        else:
            r = mid
        
    #State: The loop terminates when `l + 1 >= r`. At this point, `l` and `r` are such that `l` is the largest index where `predicate(arr[l])` is `True`, and `r` is the smallest index where `predicate(arr[r])` is `False`, or vice versa depending on the initial conditions and the behavior of the `predicate` function. The values of `arr` and `predicate` remain unchanged.
    if predicate(arr[l]) :
        return l
        #The program returns the largest index `l` where `predicate(arr[l])` is `True`.
    #State: The loop terminates when `l + 1 >= r`. At this point, `l` and `r` are such that `l` is the largest index where `predicate(arr[l])` is `True`, and `r` is the smallest index where `predicate(arr[r])` is `False`, or vice versa depending on the initial conditions and the behavior of the `predicate` function. The values of `arr` and `predicate` remain unchanged. Additionally, `predicate(arr[l])` is `False`.
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and a predicate function `predicate`. It returns the largest index `l` where `predicate(arr[l])` is `True`. If no such index exists, it returns `None`. The function does not modify the input list `arr` or the predicate function `predicate`.

#State of the program right berfore the function call: n and q are positive integers where 2 ≤ n ≤ 2 · 10^5 and 1 ≤ q ≤ 2 · 10^5. a is a list of n integers where 0 ≤ a_i < 2^30. l and r are integers such that 1 ≤ l < r ≤ n.
def func_3():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: `n` is the same as the initial value, `a` remains a list of `n` integers where \(0 \leq a_i < 2^{30}\), `x` is a list with `n + 1` elements where each element is the cumulative XOR of the elements in `a` up to that point, and `inds` is a defaultdict where each key is an element from `x` and the value is a list of indices where that element appears in `x`.
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
        
    #State: `n` is the same as the initial value, `a` remains a list of `n` integers where \(0 \leq a_i < 2^{30}\), `x` is a list with `n + 1` elements where each element is the cumulative XOR of the elements in `a` up to that point, `inds` is a defaultdict where each key is an element from `x` and the value is a list of indices where that element appears in `x`, `i` is `q`, `q` is the same as the initial value, and the values of `l`, `r`, `lower`, and `upper` are undefined or reset after the loop completes.
#Overall this is what the function does:The function `func_3` processes a list `a` of `n` integers and a series of `q` queries, each defined by two integers `l` and `r`. For each query, it determines whether there exists a subarray within `a` from index `l-1` to `r-1` (inclusive) whose cumulative XOR is zero. If such a subarray exists, it prints 'Yes'; otherwise, it prints 'No'. After processing all queries, the function maintains the original values of `n` and `q`, and the list `a` remains unchanged. The list `x` contains the cumulative XOR of elements in `a` up to each index, and `inds` is a dictionary mapping each unique XOR value to the indices where it occurs in `x`.

