#State of the program right berfore the function call: None of the variables are passed in the function signature. The function reads input from the standard input, expecting a line of space-separated integers.
def func_1():
    return map(int, input().split())
    #The program returns a map object that contains the integers from the line of space-separated integers read from the standard input.
#Overall this is what the function does:The function `func_1` reads a line of space-separated integers from the standard input and returns a map object containing these integers. The map object can be iterated over to access the integers.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_2` does not take any parameters.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of calling the function `func_1()`. Since no information is provided about what `func_1()` returns, the output state is a list containing the values returned by `func_1()`.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It returns a list containing the values returned by the function `func_1()`. The final state of the program after `func_2` concludes is a list that is the result of `func_1()`.

#State of the program right berfore the function call: n is a positive integer, k is an integer such that 1 <= k <= n, arr is a list of integers representing a permutation of size n, and contains distinct integers from 1 to n.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `n` is the same as the initial value, `i` is `n-1`, and `pos` is the index of the first occurrence of `k` in `arr`, or -1 if `k` is not found in `arr`.
    low, high = 0, n - 1
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: `n` is greater than 2, `i` is `n-1`, `pos` is the index of the first occurrence of `k` in `arr`, or -1 if `k` is not found in `arr`, `st` is a set containing all the midpoints calculated during the loop, `low` is the index just before the first occurrence of `k` in `arr` or the last index if `k` is greater than all elements in `arr`, `high` is the index of the first occurrence of `k` in `arr` or `n` if `k` is greater than all elements in `arr`.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: (pos, pos + 1) if `k` is found in `arr`; otherwise (n, 0) (where `pos` is the index of the first occurrence of `k` in `arr` or -1 if `k` is not found, and `n` is the length of `arr`)
    #State: *`n` is greater than 2, `i` is `n-1`, `pos` is the index of the first occurrence of `k` in `arr`, or -1 if `k` is not found in `arr`, `st` is a set containing all the midpoints calculated during the loop, `low` is the index just before the first occurrence of `k` in `arr` or the last index if `k` is greater than all elements in `arr`, and `high` is the index of the first occurrence of `k` in `arr` or `n` if `k` is greater than all elements in `arr`. If `arr[low]` is equal to `k`, then the condition `arr[low] == k` holds true. Otherwise, `arr[low]` is not equal to `k`.
#Overall this is what the function does:The function `func_3` does not accept any parameters directly but relies on the outputs of `func_1` and `func_2` to obtain `n`, `k`, and `arr`. It searches for the first occurrence of `k` in the list `arr` and stores its index in `pos` (or -1 if `k` is not found). It then performs a binary search on `arr` to find the position where `k` would be inserted to maintain the sorted order. If `k` is found at `low`, it prints 0. Otherwise, it prints 1 followed by the indices `low + 1` and `pos + 1`. The final state of the program includes `n` (unchanged), `pos` (index of `k` or -1), `st` (a set of midpoints from the binary search), `low` (the index just before the first occurrence of `k` or the last index if `k` is greater than all elements), and `high` (the index of the first occurrence of `k` or `n` if `k` is greater than all elements).

