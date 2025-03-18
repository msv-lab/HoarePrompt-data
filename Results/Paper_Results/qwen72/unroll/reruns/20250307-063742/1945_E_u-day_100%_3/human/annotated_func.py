#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_1():
    return map(int, input().split())
    #The program returns a map object that converts each element of the input string, split by spaces, into an integer.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads a line of input from the user, splits the input string by spaces, and returns a map object that converts each split element into an integer. The final state of the program after the function concludes is that it has a map object containing the integer representations of the input elements.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_2` does not take any parameters.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of calling the function `func_1()`. Since `func_1()` is not defined in the initial state, we do not know the specific values or structure of the list, but it is the list that `func_1()` produces.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a list that is the result of calling the function `func_1()`. The specific values or structure of the list are determined by the implementation of `func_1()`, which is not provided in the initial state. After the function concludes, the program state includes the returned list, which is the output of `func_1()`.

#State of the program right berfore the function call: n is a positive integer, k is an integer such that 1 <= k <= n, arr is a list of integers representing a permutation of size n where 1 <= arr[i] <= n for all 0 <= i < n, and pos is an integer that will be the index of k in arr if k is found.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `pos` is the index of the last occurrence of `k` in `arr`, or -1 if `k` is not found in `arr`. `n` and `arr` remain unchanged.
    low, high = 0, n
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: `pos` is the index of the last occurrence of `k` in `arr`, or -1 if `k` is not found in `arr`. `n` and `arr` remain unchanged. `low` is the largest index such that `arr[low] <= k`, or `n-1` if no such index exists. `high` is the smallest index such that `arr[high] > k`, or `n` if no such index exists. `st` contains all the midpoints calculated during the loop execution.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: (low + 1, pos + 1) (where low + 1 is the index of the first element in arr that is greater than k, and pos + 1 is the index immediately after the last occurrence of k, or (n, 0) if k is not found in arr)
    #State: *`pos` is the index of the last occurrence of `k` in `arr`, or -1 if `k` is not found in `arr`. `n` and `arr` remain unchanged. `low` is the largest index such that `arr[low] <= k`, or `n-1` if no such index exists. `high` is the smallest index such that `arr[high] > k`, or `n` if no such index exists. `st` contains all the midpoints calculated during the loop execution. If `arr[low]` is equal to `k`, then `arr[low]` is equal to `k`. Otherwise, `arr[low]` is not equal to `k`.
#Overall this is what the function does:The function `func_3` does not accept any parameters and does not return any value. It uses the values of `n` and `k` obtained from `func_1` and the list `arr` obtained from `func_2` to find the index of the last occurrence of `k` in `arr` and store it in `pos`. If `k` is not found in `arr`, `pos` remains -1. The function then performs a binary search to find the largest index `low` such that `arr[low] <= k` and the smallest index `high` such that `arr[high] > k`. If `arr[low]` is equal to `k`, the function prints 0. Otherwise, it prints 1 followed by the indices `low + 1` and `pos + 1`. The final state of the program is that `pos` is the index of the last occurrence of `k` in `arr` (or -1 if `k` is not found), `n` and `arr` remain unchanged, and `st` contains all the midpoints calculated during the binary search loop.

