#State of the program right berfore the function call: cast is a function that can be applied to each element of the input string split by spaces, typically used to convert strings to integers.
def func_1(cast):
    return map(cast, input().split())
    #The program returns a map object that applies the function `cast` to each element of the input string split by spaces.
#Overall this is what the function does:The function `func_1` takes a function `cast` as an argument, reads a line of input from the user, splits this input into substrings separated by spaces, applies the `cast` function to each substring, and returns a map object containing the results.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer as input and returns a boolean value. The function `func_2` is used to find the largest index `l` such that `predicate(arr[l])` is True, with the search range being from 0 to the length of `arr`.
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
        #The program returns the index `l` which is within the bounds of the list `arr` and satisfies the condition `predicate(arr[l])` being true.
    #State: `arr` is a list, `l` is an index within the bounds of `arr`, and `predicate(arr[l])` is false.
    return None
    #The program returns None
#Overall this is what the function does:The function `func_2` takes a list of integers `arr` and a predicate function `predicate`. It returns the largest index `l` in `arr` for which `predicate(arr[l])` is True. If no such index exists, it returns None.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes a list as an argument.
def func_3(arr, predicate):
    return func_2(arr, predicate)
    #The program returns the result of `func_2(arr, predicate)`, where `arr` is a list of integers and `predicate` is a function that takes a list as an argument.
#Overall this is what the function does:The function `func_3` takes a list of integers `arr` and a function `predicate` as parameters, and returns the result of applying the `predicate` function to the `arr` list.

#State of the program right berfore the function call: arr is a list of integers, and predicate is a function that takes an integer and returns a boolean value.
def func_4(arr, predicate):
    result = func_2(arr, predicate)
    if (result is not None) :
        return result + 1
        #The program attempts to return `result + 1`, where `result` is a list of integers from `arr` that satisfy `predicate`. This operation would result in a TypeError in a real Python environment.
    #State: `arr` is a list of integers, `predicate` is a function that takes an integer and returns a boolean value, `result` is a list of integers from `arr` that satisfy `predicate`. `result` is None
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_4` takes a list of integers `arr` and a predicate function `predicate`. It attempts to return a value that results from adding 1 to a list of integers from `arr` that satisfy `predicate`, which would cause a TypeError. If this operation fails, it returns `None`.

#State of the program right berfore the function call: n is a positive integer representing the number of elements in the array, q is a positive integer representing the number of queries, a is a list of integers where each integer is in the range [0, 2^30), l and r are integers such that 1 <= l < r <= n.
def func_5():
    n, q = func_1(int)
    a = list(func_1(int))
    x = [0]
    inds = defaultdict(list)
    inds[0].append(0)
    for i in a:
        x.append(x[-1] ^ i)
        
        inds[x[-1]].append(len(x) - 1)
        
    #State: 
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
        
    #State: The variables `l` and `r` will hold the values from the last iteration of the loop. The output will consist of a series of 'Yes' or 'No' printed statements based on the conditions checked in each iteration.
#Overall this is what the function does:The function processes an array of integers and performs a series of queries to determine if there exists a subarray within specified ranges that has a XOR value of zero. For each query, it prints 'Yes' if such a subarray exists and 'No' otherwise.

