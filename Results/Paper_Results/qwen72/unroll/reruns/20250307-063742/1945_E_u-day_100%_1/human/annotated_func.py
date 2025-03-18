#State of the program right berfore the function call: None of the variables are used in the function signature.
def func_1():
    return map(int, input().split())
    #The program returns an iterator that converts each element of the input string, split by spaces, into an integer.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an iterator that converts each element of the input string, split by spaces, into an integer. After the function concludes, the program has an iterator that can be used to iterate over the converted integers.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_2` does not take any arguments.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of calling the function `func_1()`.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It returns a list that is the result of calling the function `func_1()`. After the function concludes, the program state includes the returned list, which contains the elements produced by `func_1()`.

#State of the program right berfore the function call: n is a positive integer, k is an integer such that 1 <= k <= n, arr is a list of n distinct integers from 1 to n, and pos is an integer that will be updated to the index of k in arr if k is found.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `pos` is the index of the element `k` in the list `arr`, or -1 if `k` is not found in `arr`. The values of `n`, `k`, and `arr` remain unchanged.
    low, high = 0, n
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: `pos` is the index of the element `k` in the list `arr`, or -1 if `k` is not found in `arr`. The values of `n`, `k`, and `arr` remain unchanged. `low` is the largest index such that `arr[low] <= k`, or `n` if no such index exists. `high` is the smallest index such that `arr[high] > k`, or 0 if no such index exists. `st` contains all the midpoints that were checked during the loop execution.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: (low + 1, pos + 1) (where low + 1 is the index where k would be inserted to maintain the sorted order of arr, and pos + 1 is the index of k plus 1 if k is found, or 0 if k is not found)
    #State: *`pos` is the index of the element `k` in the list `arr`, or -1 if `k` is not found in `arr`. The values of `n`, `k`, and `arr` remain unchanged. `low` is the largest index such that `arr[low] <= k`, or `n` if no such index exists. `high` is the smallest index such that `arr[high] > k`, or 0 if no such index exists. `st` contains all the midpoints that were checked during the loop execution. Additionally, if `arr[low]` is equal to `k`, then `pos` is set to `low`. Otherwise, `arr[low]` is not equal to `k`.
#Overall this is what the function does:The function `func_3` does not accept any parameters and does not return any value. It initializes `n`, `k`, and `arr` by calling `func_1` and `func_2`, respectively. It then searches for the integer `k` in the list `arr` and updates `pos` to the index of `k` if found, otherwise `pos` remains -1. The function also performs a binary search to find the largest index `low` such that `arr[low] <= k` and the smallest index `high` such that `arr[high] > k`. If `k` is found in `arr` (i.e., `arr[low] == k`), it prints `0`. If `k` is not found, it prints `1` followed by the index where `k` would be inserted to maintain the sorted order of `arr` and the index of `k` plus 1 if `k` is found, or 0 if `k` is not found. The final state of the program includes `pos` being the index of `k` in `arr` or -1 if `k` is not found, and `st` containing all the midpoints checked during the binary search.

