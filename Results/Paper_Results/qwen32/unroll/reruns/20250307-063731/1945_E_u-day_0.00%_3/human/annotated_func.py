#State of the program right berfore the function call: No variables are present in the function signature of `func_1`. It is assumed that this function is used to read input values from the standard input and return them as a map of integers.
def func_1():
    return map(int, input().split())
    #The program returns a map object that contains integers, which are the result of splitting the input string by whitespace and converting each split substring to an integer.
#Overall this is what the function does:The function `func_1` reads a line of input from the standard input, splits it into substrings based on whitespace, converts each substring to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: This function does not have any parameters, so there are no variables or relationships to describe.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of calling the function `func_1()`.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a list that is the result of calling the function `func_1()`.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, and k is an integer such that 1 <= k <= n.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `n` is a positive integer returned by `func_1()`, `k` is an integer such that `1 <= k <= n` returned by `func_1()`, `arr` is the value returned by `func_2()`, `pos` is the index of the last occurrence of `k` in `arr` or `-1` if `k` is not found.
    low, high = 0, n - 1
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: `low` is the largest index such that `arr[low] <= k` and `high` is the smallest index such that `arr[high] > k`. The set `st` contains all midpoints checked during the loop.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: low + 1, pos + 1 (where low is the largest index such that arr[low] <= k and pos is the index where k would be placed in the sorted array arr)
    #State: `low` is the largest index such that `arr[low] <= k` and `high` is the smallest index such that `arr[high] > k`. The set `st` contains all midpoints checked during the loop. Additionally, if `arr[low]` is equal to `k`, then `arr[low]` is equal to `k`; otherwise, `arr[low]` is not equal to `k`.
#Overall this is what the function does:The function determines the position of a specified integer `k` within a permutation array `arr` of length `n`. It prints `0` if `k` is found in the array, otherwise it prints `1` followed by the position where `k` would fit in the sorted array and the actual position of `k` if it were to be inserted in the sorted order.

