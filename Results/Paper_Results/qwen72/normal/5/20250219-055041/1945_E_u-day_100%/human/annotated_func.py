#State of the program right berfore the function call: No variables are passed to the function func_1. The function is expected to read input from stdin, which should contain integers separated by spaces.
def func_1():
    return map(int, input().split())
    #The program returns a map object that contains the integers from the input provided, where each integer is converted from a string to an int. The input is expected to be a sequence of integers separated by spaces.
#Overall this is what the function does:The function `func_1` reads a sequence of integers separated by spaces from the standard input. It converts each string in the sequence to an integer and returns a map object containing these integers. The function does not modify any external variables or state.

#State of the program right berfore the function call: None of the variables in the function signature are relevant to the problem description.
def func_2():
    return list(func_1())
    #The program returns an empty list, as `func_1()` is not defined and thus does not provide any values to be converted into a list.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns an empty list. This is because `func_1` is not defined, and thus the call to `list(func_1())` results in an empty list being returned.

#State of the program right berfore the function call: n is a positive integer, k is an integer such that 1 <= k <= n, arr is a list of integers representing a permutation of size n, and pos is an integer that will be the index of k in arr if k is found.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `n` is greater than or equal to its initial value, `i` is `n-1`. If `k` is found in `arr`, `pos` is the index of the first occurrence of `k` in `arr`. Otherwise, `pos` remains -1.
    low, high = 0, n
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: `n` is greater than or equal to its initial value, `i` is `n-1`, `pos` remains -1 if `k` is not found in `arr` or is the index of the first occurrence of `k` in `arr` if `k` is found, `low` is the largest index such that `arr[low] <= k`, `high` is the smallest index such that `arr[high] > k`, `st` is a set containing all the midpoints calculated during the loop, and `mid` is the last midpoint calculated before the loop terminates.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: (low + 1, pos + 1) (where `low + 1` is the index of the first element in `arr` that is greater than `k`, and `pos + 1` is 0 if `k` is not found in `arr`, or the index of the first occurrence of `k` plus one if `k` is found)
    #State: *`n` is greater than or equal to its initial value, `i` is `n-1`, `pos` remains -1 if `k` is not found in `arr` or is the index of the first occurrence of `k` in `arr` if `k` is found, `low` is the largest index such that `arr[low] <= k`, `high` is the smallest index such that `arr[high] > k`, `st` is a set containing all the midpoints calculated during the loop, and `mid` is the last midpoint calculated before the loop terminates. If `arr[low] == k`, then `pos` is the index of the first occurrence of `k` in `arr`. Otherwise, `arr[low]` is not equal to `k` and `pos` remains -1 if `k` is not found in `arr`.
#Overall this is what the function does:The function `func_3` does not accept any parameters and does not return any values. It internally calls `func_1` to obtain `n` and `k`, and `func_2` to obtain a list `arr` of integers representing a permutation of size `n`. The function then searches for the integer `k` in the list `arr`. If `k` is found, `pos` is set to the index of the first occurrence of `k` in `arr`. If `k` is not found, `pos` remains -1. The function also performs a binary search to find the largest index `low` such that `arr[low] <= k` and the smallest index `high` such that `arr[high] > k`. If `k` is found at `arr[low]`, the function prints 0. If `k` is not found, the function prints 1 and then prints the values `low + 1` and `pos + 1`, where `low + 1` is the index of the first element in `arr` that is greater than `k`, and `pos + 1` is 0 if `k` is not found in `arr` or the index of the first occurrence of `k` plus one if `k` is found.

