#State of the program right berfore the function call: No variables are present in the function signature of `func_1`, which is responsible for reading input from the user and returning a map object of integers.
def func_1():
    return map(int, input().split())
    #The program returns a map object containing integers derived from the user's input, where the input is expected to be a string of space-separated numbers.
#Overall this is what the function does:The function `func_1` reads a string of space-separated numbers from the user, converts these numbers into integers, and returns a map object containing these integers.

#State of the program right berfore the function call: This function signature is not provided in the given code snippet. However, based on the context and the problem description, we can infer a possible function signature and its precondition. If we consider a function that might be involved in the process, it could look something like `def rearrange_permutation(p, x):`. In this case, the precondition would be: p is a list representing a permutation of integers from 1 to n, and x is an integer such that 1 <= x <= n.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of converting the return value of `func_1()` to a list.
#Overall this is what the function does:The function returns a list that is the result of converting the return value of `func_1()` to a list.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, and k is an integer such that 1 <= k <= n.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `n` is a positive integer, `1 <= k <= n`, `arr` is the value returned by `func_2()`, and `pos` is the index `i` where `arr[i]` equals `k` if such an `i` exists within the range `[0, n-1]`; otherwise, `pos` remains -1.
    low, high = 0, n - 1
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: `n` is a positive integer, `1 <= k <= n`, `arr` is the value returned by `func_2()`, `pos` is the index `i` where `arr[i]` equals `k` if such an `i` exists within the range `[0, n-1]`; otherwise, `pos` remains -1, `low` is the index where the final `mid` was found or the closest index to `k` if `k` is not in `arr`, `high` is `low + 1`, `st` is a set containing all the `mid` values calculated during the loop.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: low + 1, 0 (where low is the index where the final mid was found or the closest index to k if k is not in arr)
    #State: `n` is a positive integer, `1 <= k <= n`, `arr` is the value returned by `func_2()`, `pos` is the index `low` where `arr[low]` equals `k` if `arr[low]` equals `k`; otherwise, `pos` remains -1, `low` is the index where the final `mid` was found or the closest index to `k` if `k` is not in `arr`, `high` is `low + 1`, `st` is a set containing all the `mid` values calculated during the loop. If `arr[low]` equals `k`, then `pos` is set to `low`; otherwise, `pos` remains -1.
#Overall this is what the function does:The function `func_3` determines the position of an integer `k` within a permutation array `arr` of length `n` and prints whether `k` is found at a specific index or not. If `k` is found, it prints `0`. If `k` is not found, it prints `1` followed by the index of the closest element to `k` and the original position of `k` in the array.

