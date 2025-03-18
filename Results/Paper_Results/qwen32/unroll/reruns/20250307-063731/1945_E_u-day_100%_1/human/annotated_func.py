#State of the program right berfore the function call: No variables are present in the function signature of `func_1`. This function is expected to read input from the standard input and return a map object containing integers.
def func_1():
    return map(int, input().split())
    #The program returns a map object containing integers that were read from the standard input and split by whitespace.
#Overall this is what the function does:The function `func_1` reads a line of input from the standard input, splits the line into substrings based on whitespace, converts each substring into an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: This function does not have any parameters in its signature, so there are no variables to describe. However, since it calls `func_1()` and returns its result as a list, it is implied that `func_1()` should return an iterable that can be converted to a list.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of converting the iterable returned by `func_1()` to a list.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It calls `func_1()` and returns the result as a list.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, and k is an integer such that 1 <= k <= n.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `n` is a positive integer, `k` is an integer such that 1 <= k <= n, `arr` is the value returned by `func_2()`, `pos` is the index of the last occurrence of `k` in `arr` or -1 if `k` is not found.
    low, high = 0, n
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: low is the greatest index where arr[low] <= k, high is the smallest index where arr[high] > k, and st contains all mid values calculated during the loop.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: low + 1, pos + 1 (where low is the greatest index where arr[low] <= k and pos is an index related to the search for k in arr)
    #State: `low` is the greatest index where `arr[low] <= k`, `high` is the smallest index where `arr[high] > k`, and `st` contains all mid values calculated during the loop. Additionally, `arr[low]` is either equal to `k` or not equal to `k`.
#Overall this is what the function does:The function determines the position of a specified integer `k` within a permutation of length `n` and prints specific values based on whether `k` is found in the permutation. If `k` is found, it prints `0`. If `k` is not found, it prints `1` followed by the greatest index where the elements are less than or equal to `k` and the position of `k` in the array, adjusted by 1.

