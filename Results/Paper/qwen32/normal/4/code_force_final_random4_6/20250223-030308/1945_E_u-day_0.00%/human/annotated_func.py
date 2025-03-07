#State of the program right berfore the function call: No variables are present in the function signature of `func_1`. This function is expected to read input from the standard input, split it into integers, and return them as a map object.
def func_1():
    return map(int, input().split())
    #The program returns a map object that contains integers from the input string split by whitespace.
#Overall this is what the function does:The function `func_1` reads a line of input from the standard input, splits it into substrings based on whitespace, converts these substrings into integers, and returns a map object containing these integers.

#State of the program right berfore the function call: This function does not have any parameters as per the provided code snippet. Therefore, there are no variables to describe in terms of their values or relationships.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of calling `func_1()`
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a list that is the result of calling `func_1()`.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, and k is an integer such that 1 <= k <= n.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `pos` is the index of the last occurrence of `k` in `arr`, or -1 if `k` is not found in `arr`.
    low, high = 0, n - 1
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: `pos` is the index of the last occurrence of `k` in `arr`, or -1 if `k` is not found in `arr`; `low` and `high` are two consecutive indices such that `low + 1 == high`; `st` is a set containing all the midpoints calculated during the loop.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: high, pos + 1 (where high is the index right after low, and pos + 1 is the index right after the last occurrence of k in arr, or 0 if k is not found in arr)
    #State: `pos` is the index of the last occurrence of `k` in `arr`, or -1 if `k` is not found in `arr`; `low` and `high` are two consecutive indices such that `low + 1 == high`; `st` is a set containing all the midpoints calculated during the loop. If `arr[low]` is `k`, then `pos` remains unchanged or is updated to `low` if `low` is a higher index than the current `pos`. Otherwise, `arr[low]` is not equal to `k`, and `pos` remains unchanged.
#Overall this is what the function does:The function determines the position of the value `k` in a permutation array `arr` of length `n`. It prints `0` if `k` is found at the position indicated by `low`, otherwise, it prints `1` followed by the indices `low + 1` and `pos + 1`, where `pos` is the index of the last occurrence of `k` in `arr` or `-1` if `k` is not found.

