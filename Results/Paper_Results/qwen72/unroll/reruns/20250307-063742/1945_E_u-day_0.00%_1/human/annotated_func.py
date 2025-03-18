#State of the program right berfore the function call: None
def func_1():
    return map(int, input().split())
    #The program returns an iterator that yields integers from the input string, where the input string is split by spaces.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an iterator that yields integers from an input string split by spaces. The input string is provided by the user through the `input()` function. After the function concludes, the program state includes an iterator that can be used to iterate over the integers derived from the user's input.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_2` does not take any parameters.
def func_2():
    return list(func_1())
    #The program returns a list that is the result of calling the function `func_1()`. Since `func_1()` is not defined in the initial state, the specific contents of the list are unknown.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a list that is the result of calling `func_1()`. The specific contents of the list are unknown because `func_1()` is not defined in the provided code.

#State of the program right berfore the function call: n is a positive integer, k is an integer such that 1 <= k <= n, arr is a list of integers representing a permutation of size n, and contains distinct integers from 1 to n.
def func_3():
    n, k = func_1()
    arr = func_2()
    pos = -1
    for i in range(n):
        if arr[i] == k:
            pos = i
        
    #State: `n` and `k` remain unchanged, `arr` remains the result of `func_2()`, `pos` is the index of the element `k` in `arr` if `k` is found in `arr`, otherwise `pos` remains -1.
    low, high = 0, n - 1
    st = set()
    while low + 1 < high:
        mid = (low + high) // 2
        
        st.add(mid)
        
        if arr[mid] > k:
            high = mid
        else:
            low = mid
        
    #State: `n` and `k` remain unchanged, `arr` remains the result of `func_2()`, `pos` remains -1 if `k` is not found in `arr`, otherwise `pos` is the index of `k` in `arr`, `low` is the largest index such that `arr[low] <= k`, `high` is the smallest index such that `arr[high] > k`, `st` contains all the midpoints calculated during the loop execution.
    if (arr[low] == k) :
        print(0)
        #This is printed: 0
    else :
        print(1)
        #This is printed: 1
        print(low + 1, pos + 1)
        #This is printed: high, 0 (where high is the smallest index such that arr[high] > k)
    #State: *`n` and `k` remain unchanged, `arr` remains the result of `func_2()`, `pos` remains -1 if `k` is not found in `arr`, otherwise `pos` is the index of `k` in `arr`, `low` is the largest index such that `arr[low] <= k`, `high` is the smallest index such that `arr[high] > k`, `st` contains all the midpoints calculated during the loop execution. If `arr[low] == k`, the current value of `arr[low]` is equal to `k`. Otherwise, `arr[low]` is not equal to `k`.
#Overall this is what the function does:The function `func_3` does not accept any parameters and does not return any value. It operates on variables `n`, `k`, and `arr` that are obtained from the functions `func_1` and `func_2`. The function searches for the integer `k` in the list `arr`, which is a permutation of integers from 1 to `n`. If `k` is found in `arr`, the function prints `0`. If `k` is not found, the function prints `1` followed by the smallest index `high` such that `arr[high] > k` and the index `pos + 1` (where `pos` is the index of `k` if it were found, otherwise `pos` remains -1). The final state of the program is that `n` and `k` remain unchanged, `arr` remains the result of `func_2()`, `pos` is the index of `k` if `k` is found in `arr` (otherwise `pos` remains -1), `low` is the largest index such that `arr[low] <= k`, `high` is the smallest index such that `arr[high] > k`, and `st` contains all the midpoints calculated during the loop execution.

