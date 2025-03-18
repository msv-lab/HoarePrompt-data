#State of the program right berfore the function call: None of the variables in the function signature are used, as the function takes no arguments.
def func_1():
    return map(int, input().split())
    #The program returns an iterator that converts the input values, which are separated by spaces, into integers.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an iterator that converts space-separated input values into integers. The state of the program after the function concludes is that the iterator is available for further processing, and it will yield integer values when iterated over.

#State of the program right berfore the function call: None of the variables in the function signature are used.
def func_2():
    return list(func_1())
    #The program returns an empty list, as `func_1()` is called without using any of the variables in the function signature, and there is no information provided about what `func_1()` returns, so it is assumed to return an empty list.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a list. The content of the list depends on what `func_1()` returns. If `func_1()` returns an iterable, `func_2` will return a list containing the elements of that iterable. If `func_1()` returns a non-iterable or nothing, `func_2` will return an empty list.

#State of the program right berfore the function call: n is a positive integer, k is an integer such that 1 <= k <= n, arr is a list of integers representing a permutation of size n, where each element in arr is unique and within the range 1 to n.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `n` is greater than or equal to its initial value, `i` is `n-1`. If `k` is found in `arr`, `pos` is set to the index of `k` in `arr`. Otherwise, `pos` remains -1.
    low, high = 0, n - 1
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: `n` is greater than or equal to its initial value, `i` is `n-1`, `low` and `high` are such that `low + 1 >= high`, `pos` is -1 if `k` is not found in `arr` otherwise it is the index of `k` in `arr`, `st` is a set containing the midpoints calculated during the loop iterations, and `mid` is the last calculated midpoint.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: [low + 1], [pos + 1] (where low + 1 is at least high or greater, and pos + 1 is 0 if k is not found in arr, or the index of k plus one if k is found in arr)
    #State: *`n` is greater than or equal to its initial value, `i` is `n-1`, `low + 1 >= high`, `pos` is -1 if `k` is not found in `arr` otherwise it is the index of `k` in `arr`, `st` is a set containing the midpoints calculated during the loop iterations, and `mid` is the last calculated midpoint. If `arr[low]` is equal to `k`, then `pos` is set to `low`. Otherwise, `pos` remains -1.
#Overall this is what the function does:The function `func_3` does not accept any parameters and does not return any values. It uses the values of `n` and `k` obtained from `func_1` and a list `arr` obtained from `func_2`. The function searches for the integer `k` in the list `arr` and prints a message indicating whether `k` was found. If `k` is found at index `low` in `arr`, it prints `0`. If `k` is not found, it prints `1` followed by the values `low + 1` and `pos + 1`, where `low` is the index of the closest element less than or equal to `k` and `pos` is the index of `k` if found, or -1 if not found. The function also maintains a set `st` containing the midpoints calculated during the search process.

