#State of the program right berfore the function call: No variables are present in the function signature. This function is expected to read input from the standard input and return a map object that contains integers.
def func_1():
    return map(int, input().split())
    #The program returns a map object that contains integers, which are the integer representations of the space-separated values provided as input through standard input.
#Overall this is what the function does:The function `func_1` reads a line of space-separated values from the standard input, converts these values into integers, and returns a map object containing these integers.

#State of the program right berfore the function call: This function signature is not provided in the problem description. However, based on the context and the function name `func_2` returning a list from `func_1`, we can infer that `func_1` likely returns some form of data that can be converted to a list. No specific precondition can be given without the actual function signature of `func_2` or `func_1`.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of converting the output of `func_1()` to a list.
#Overall this is what the function does:The function `func_2` accepts no parameters and returns a list that is the result of converting the output of `func_1()` to a list.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, and k is an integer such that 1 <= k <= n. arr is a list of integers representing the permutation of length n.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `n` is the first value returned by `func_1()`, `k` is the second value returned by `func_1()`, `arr` is the list returned by `func_2()`, and `pos` is the index of the first occurrence of `k` in `arr` if `k` is present, otherwise `pos` is -1.
    low, high = 0, n - 1
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: `low` and `high` are adjacent indices, `st` contains all `mid` values calculated during the iterations.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: low + 1, pos + 1 (where low + 1 is the 1-based index corresponding to the low index, and pos + 1 is the 1-based index corresponding to the pos index)
    #State: `low` and `high` are adjacent indices, `st` contains all `mid` values calculated during the iterations. If `arr[low]` is equal to `k`, then `arr[low]` is equal to `k`. Otherwise, `arr[low]` is not equal to `k`.
#Overall this is what the function does:The function determines the position of a specified integer `k` in a permutation list `arr` of length `n`. It prints `0` if `k` is found at the position indicated by a binary search's lower bound index. If `k` is not found at that position, it prints `1` followed by the 1-based indices of the lower bound and the first occurrence of `k` in the list.

