#State of the program right berfore the function call: No variables are present in the function signature of `func_1`, as it directly takes input from the user and returns a map object of integers.
def func_1():
    return map(int, input().split())
    #The program returns a map object containing integers that were input by the user, separated by spaces.
#Overall this is what the function does:The function `func_1` prompts the user to input a series of integers separated by spaces and returns a map object containing these integers.

#State of the program right berfore the function call: The function `func_2` does not take any parameters. It returns a list that is the result of calling another function `func_1`.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of calling the function `func_1`.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a list that is the result of calling the function `func_1`.

#State of the program right berfore the function call: n is a positive integer representing the length of the permutation, and k is an integer such that 1 <= k <= n. arr is a list of integers representing the permutation of size n. pos is an integer representing the index of the element k in arr, if it exists. low and high are integers representing the current search range in the binary search algorithm, with 0 <= low < high <= n-1. st is a set of integers representing the midpoints visited during the binary search.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `n` and `k` are the values returned by `func_1()`, `arr` is the list of integers returned by `func_2()`, `pos` is the index of the first occurrence of `k` in `arr` or -1 if `k` is not in `arr`, `low` and `high` are integers representing the current search range in the binary search algorithm, with 0 <= `low` < `high` <= n-1, `st` is a set of integers representing the midpoints visited during the binary search.
    low, high = 0, n - 1
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: low and high are adjacent indices, and st contains the set of mid values calculated during the loop.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: low + 1, pos + 1 (where low and pos are indices in the array `arr`)
    #State: low and high are adjacent indices, and st contains the set of mid values calculated during the loop. If the value at `arr[low]` is equal to `k`, then `arr[low]` is equal to `k`. Otherwise, `arr[low]` is not equal to `k`.
#Overall this is what the function does:The function performs a binary search on a list `arr` to find the element `k`. It prints `0` if `k` is found at the `low` index, otherwise it prints `1` and the indices `low + 1` and `pos + 1`. Here, `pos` is the index of the first occurrence of `k` in `arr` or `-1` if `k` is not present.

